# Chinese Document Style Reference

## Contents

- Rule priority
- Formal academic style
- Spacing and character width
- Punctuation
- Numbers, dates, and units
- English, abbreviations, and names
- Document structure
- Links, code, and citations
- Review checklist

## Rule Priority

Apply rules in this order:

1. Legal, national, industry, institutional, journal, or delivery requirements.
2. Official product, protocol, trademark, and proper-name spellings.
3. Declared project terminology and style.
4. General rules in this reference.
5. Personal preference.

Classify rules as mandatory, recommended, or optional. Do not present a visual preference as a correctness error.

## Formal Academic Style

- State the research object, method, evidence, result, limitation, and conclusion explicitly.
- Prefer neutral verbs such as “表明”“显示”“观察到”“结果为”.
- Avoid unsupported superlatives such as “最佳”“最先进”“完全解决”“显著领先”.
- Quantify comparisons and identify the baseline, metric, sample, and conditions.
- Preserve uncertainty. Do not turn “可能”“结果提示”“在本实验条件下” into categorical claims.
- Avoid slogans, rhetorical questions, reader manipulation, excessive first person, and conversational filler.
- Avoid repeated formulaic transitions such as “值得注意的是”“综上所述”“不难发现” when they add no logical information.
- Keep terminology stable and define uncommon abbreviations at first occurrence.
- Use “必须” for requirements, “建议/推荐” for guidance, and “可以” for options.

## Spacing and Character Width

Add one half-width space:

- between Chinese and English: `使用 GitHub 登录`;
- between Chinese and Arabic numerals: `包含 12 个样本`;
- between a number and most units: `10 GB`, `8 km`, `256 MB`.

Do not add a space:

- before `%`, `°`, or `°C`: `15%`, `90°`, `37°C`;
- around full-width Chinese punctuation;
- inside official names, URLs, email addresses, code, paths, identifiers, formulas, models, or version strings.

Use full-width Chinese punctuation in Chinese sentences. Use half-width Latin letters and Arabic numerals. Preserve half-width punctuation inside complete English sentences and fixed-syntax content.

Do not use full-width spaces in ordinary body text or repeated spaces for visual layout.

## Punctuation

### Comma and Enumeration Comma

Use `，` for clause-level pauses and `、` for parallel words or short phrases.

> 支持 Windows、macOS 和 Linux。

> 先备份数据，再升级系统。

Do not put `、` immediately before “和”“与”“或” in a simple enumeration.

### Semicolon and Colon

Use `；` between long parallel clauses. Use `：` to introduce explanations, examples, conclusions, or lists. Avoid nested colons in one sentence.

### Quotation Marks

Mainland standards commonly use `“”` and `‘’`. Some publications and products use `「」` and `『』`. Follow the target standard; otherwise select one system and keep it consistent.

Use quotation marks for direct quotations, interface text, and errors. Use inline code for commands, parameters, fields, paths, and identifiers.

### Parentheses

Ordinary Chinese prose should generally use full-width parentheses:

> 应用程序接口（API）

Some technical styles use half-width parentheses around pure English:

> 应用程序接口 (API)

Treat this as an optional project choice. Do not mix both conventions without reason.

### Ellipsis, Em Dash, and Ranges

- Chinese ellipsis: `……`
- Chinese em dash: `——`, without surrounding spaces
- Numeric range: `10～20 GB`
- Time, place, or sequence span: `2020—2026 年`
- Hyphen in compounds, filenames, models, or ISO dates: `UTF-8`, `2026-06-25`

Do not stack `！！！`, `？？？`, or similar punctuation.

Avoid closing punctuation at line start and opening punctuation at line end. Do not split numbers from units or break English words arbitrarily.

## Numbers, Dates, and Units

Use Arabic numerals for measurements, calculations, percentages, dates, times, versions, identifiers, and comparable data.

Use Chinese numerals for approximate quantities, established expressions, traditional dates, or deliberately formal short expressions.

Keep the same numeric function in one form:

> 第一章、第二章、第三章

Use grouping for long integers when helpful:

> 12,345; 12,345.6789

Recommended formats:

- prose date: `2026 年 6 月 25 日`;
- machine field or filename: `2026-06-25`;
- time: `14:30` or `14 时 30 分`;
- cross-time-zone event: include the time zone or use ISO 8601.

Distinguish:

- “增加了 100%” from “增加到原来的 2 倍”;
- “降低了 80%” from “降低到原来的 20%”.

Do not write “降低 3 倍”.

## English, Abbreviations, and Names

- Preserve official capitalization: GitHub, JavaScript, TypeScript, MySQL, macOS, iPhone, ChatGPT.
- Do not invent abbreviations such as `Ts`, `nextjs`, `10w`, or `16c32g`.
- Explain an uncommon abbreviation on first use:

  > 内容分发网络（Content Delivery Network，CDN）

- Use an official Chinese translation when stable and appropriate for the audience.
- On first use, pair an unfamiliar official Chinese translation with its official English name.
- Do not invent unofficial transliterations.

## Document Structure

### Headings, Sentences, and Paragraphs

- Do not skip heading levels; generally keep four levels or fewer.
- Make headings concise, descriptive, and parallel with peers.
- Use verb-object headings for procedures: `配置数据库`.
- Do not normally end headings with a period.
- Keep one main judgment per sentence.
- Treat 100 Chinese characters as a review threshold, not a mechanical maximum.
- Keep one topic per paragraph and place the topic sentence near the beginning.
- Treat 50–200 Chinese characters as a common paragraph range, not a hard limit.

### Lists and Tables

- Use ordered lists for sequence, ranking, or later numbered reference.
- Use unordered lists for non-sequential parallel information.
- Keep grammar, granularity, and punctuation parallel.
- Avoid more than three nesting levels.
- Split procedures longer than about nine steps into phases.
- Give tables explicit headers and stable column names.
- Define empty values such as “无”“不适用” or `—`.
- Move long explanations out of cells and do not use “同上”.

## Links, Code, and Citations

Use descriptive link text instead of “点击这里” or unexplained raw filenames. Validate anchors, permissions, redirects, and external dependencies.

Use inline code for commands, parameters, filenames, paths, fields, variables, and identifiers. Label fenced code blocks with a language. Separate commands from output. Explain placeholders and warn before destructive commands.

Preserve citation keys, footnotes, bibliography entries, quotations, equations, table and figure numbering, and cross-references.

Do not:

- fabricate or infer bibliographic details;
- strengthen causal claims beyond the research design;
- remove experimental conditions, sample size, uncertainty, limitations, or negative results;
- replace “最新”“目前”“近期” with a concrete date unless the date is supplied or verified;
- invent a citation style when none is specified.

## Review Checklist

- Facts, data, dates, versions, names, links, and citations are accurate.
- Terminology, person, quotation marks, parentheses, dates, ranges, and numbering are consistent.
- Chinese-English and Chinese-number spacing is correct.
- Units and exception symbols are formatted correctly.
- Chinese punctuation is full-width and has no surrounding spaces.
- Headings do not skip levels.
- Long sentences and overloaded paragraphs have been reviewed.
- Lists and tables are parallel and explicit.
- Code, URLs, paths, formulas, identifiers, and quotations remain unchanged unless intentionally edited.
- Promotional or formulaic AI language has been removed without deleting substantive claims.
- The revision has not changed modality, causality, uncertainty, limitations, or citation meaning.
