# Encoding Playbook

## Contents

- Python file I/O
- CSV and JSON
- Subprocesses and terminals
- HTTP and databases
- Mojibake repair
- Repository migration
- Failure patterns

## Python file I/O

Always make the boundary explicit:

```python
with open(path, "r", encoding="utf-8", errors="strict", newline="") as stream:
    text = stream.read()
```

`locale.getencoding()` describes a platform default, not the file. Do not use it as evidence of file encoding. `PYTHONUTF8=1` and `python -X utf8` make Python defaults more consistent but do not convert legacy data.

Use binary mode for detection:

```python
raw = Path(path).read_bytes()
text = raw.decode("gb18030", errors="strict")
```

Decode with the verified source codec, then write UTF-8 as a separate operation. Never read a legacy file with a guessed codec and overwrite it in place before inspecting the result.

## CSV and JSON

- Pass `encoding="utf-8"` to `open()` before `csv.reader` or `csv.writer`.
- Use `utf-8-sig` for CSV exported by or intended for software that requires a BOM.
- JSON exchanged over modern APIs should be UTF-8. `json.load()` receives text from an explicitly encoded stream; `json.loads()` accepts an already decoded string.
- Set `ensure_ascii=False` only to make Chinese readable in JSON output. It changes escaping, not the output stream's encoding.

```python
with open(path, "w", encoding="utf-8", newline="") as stream:
    json.dump(data, stream, ensure_ascii=False, indent=2)
```

## Subprocesses and terminals

The parent must decode with the encoding emitted by the child. On Windows, this may differ from the active console code page and from Python's file default.

1. Prefer a child option that emits UTF-8.
2. Set `encoding="utf-8"` in `subprocess.run` when that contract is known.
3. Otherwise capture bytes with `text=False`, inspect them, and decode using the child's documented encoding.

For interactive PowerShell, inspect `[Console]::InputEncoding`, `[Console]::OutputEncoding`, and `$OutputEncoding`. Changing the console to UTF-8 can fix display and pipe boundaries, but it does not convert existing GBK files.

Display corruption and file corruption are different. Verify by redirecting raw output to a file or inspecting code points before editing stored data.

## HTTP and databases

- Prefer the protocol declaration (`Content-Type; charset=...`) when it matches raw-byte evidence.
- For Python `requests`, inspect `response.content`, `response.encoding`, headers, and only then use `response.text`. Override `response.encoding` when the server declaration is demonstrably wrong.
- Do not encode/decode database strings again. Configure the driver and connection charset, and keep application values as Unicode strings.

## Mojibake repair

Mojibake is valid Unicode produced by decoding bytes with the wrong codec. Derive the inverse transformation from the history rather than stacking `encode`/`decode` calls blindly.

Example: UTF-8 bytes decoded as Latin-1:

```python
broken = "ä¸­æ–‡"
repaired = broken.encode("latin-1").decode("utf-8")
assert repaired == "中文"
```

Apply a repair only when all characters can be encoded back with the mistaken codec and the recovered bytes decode strictly with the intended codec. Validate several samples. If the text contains `�` (`U+FFFD`) or characters were discarded with `errors="ignore"`, recovery may be impossible without original bytes.

Strings resembling `涓枃` often indicate UTF-8 bytes decoded through a Chinese legacy codec and later re-encoded, but the exact reversal depends on every step. Recover from the original file or transport capture whenever possible.

## Repository migration

1. Check `.gitattributes`, `.editorconfig`, tool configs, and language-specific encoding declarations.
2. Inventory only text files in scope and detect BOMs or legacy encodings from raw bytes.
3. Convert one verified source encoding to UTF-8 with a script that uses strict decoding.
4. Preserve newline policy unless normalization is intentional.
5. Run tests and inspect diffs for mass replacement, deleted characters, or binary files accidentally treated as text.
6. Add an `.editorconfig` setting such as `charset = utf-8` when the repository wants a durable policy.

Source code encoding declarations, such as Python's coding cookie, describe the source file. They do not control runtime files, HTTP bodies, subprocess output, or terminal rendering.

## Failure patterns

| Symptom | Likely boundary | Correct response |
| --- | --- | --- |
| `UnicodeDecodeError: 'utf-8'` | Non-UTF-8 bytes read as UTF-8 | Inspect bytes and producer; use verified source codec |
| `UnicodeDecodeError: 'gbk'` on Windows | Implicit locale default | Specify the file or process encoding explicitly |
| `UnicodeEncodeError` while printing | Output stream cannot encode text | Configure the output stream/terminal; do not alter the string |
| `���` or `�` | Lossy replacement already occurred | Recover original bytes or backup |
| `ä¸­æ–‡` | UTF-8 decoded as Latin-1/Windows-1252 | Reverse only after proving the transformation |
| Correct file, wrong terminal display | Rendering/output configuration | Fix terminal encoding/font, leave file bytes unchanged |
