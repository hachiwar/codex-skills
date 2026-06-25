# codex-skills

面向 Codex 与 Claude Code 的可复用技能集合。

## 现有技能

| 能力 | Codex | Claude Code | 说明 |
| --- | --- | --- | --- |
| Unicode 编码诊断与修复 | [`fix-unicode-decode`](fix-unicode-decode/) | [`claude-fix-unicode-decode`](claude-fix-unicode-decode/) | 诊断并修复解码异常、中文乱码和跨平台编码问题 |
| 中文文档风格与排版 | [`chinese-document-style`](chinese-document-style/) | [`claude-chinese-document-style`](claude-chinese-document-style/) | 审校学术、技术与规范性中文文档；参见[技能介绍](docs/chinese-document-style.md) |

## 目录约定

- Codex 技能包含 `SKILL.md`、按需加载的 `references/`，以及可选的 `agents/openai.yaml`。
- Claude Code 技能包含 `SKILL.md` 和按需加载的 `references/`。
- 技能的详细介绍、安装方法与使用示例统一放在 [`docs/`](docs/) 目录。
