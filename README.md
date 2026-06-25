# codex-skills

面向 Codex 与 Claude Code 的可复用技能集合。

## Skills

| 能力 | Codex | Claude Code |
| --- | --- | --- |
| Unicode 编码诊断与修复 | [`fix-unicode-decode`](fix-unicode-decode/) | [`claude-fix-unicode-decode`](claude-fix-unicode-decode/) |
| 中文文档风格与排版 | [`chinese-document-style`](chinese-document-style/) | [`claude-chinese-document-style`](claude-chinese-document-style/) |

## 中文文档风格与排版

`chinese-document-style` 与 `claude-chinese-document-style` 用于创建、审校和修订简体中文文档，主要覆盖：

- 学术性、技术性和规范性语言风格；
- 中英文与数字之间的空格；
- 全角、半角和中文标点；
- 数字、日期、单位和范围符号；
- 专有名词、英文缩略语和术语一致性；
- 标题、句子、段落、列表、表格、链接和代码；
- 引用、参考文献、论证强度和学术完整性；
- 口语化、宣传化和模式化 AI 表达的识别与修订。

规范依据主要参考：

1. [sparanoid/chinese-copywriting-guidelines](https://github.com/sparanoid/chinese-copywriting-guidelines)
2. [yikeke/zh-style-guide](https://github.com/yikeke/zh-style-guide)
3. Hindy Hong 的《[写给大家看的中文排版指南](https://zhuanlan.zhihu.com/p/20506092)》
4. [hachiwar/Chinese-Document-Style-and-Typography-Guidelines](https://github.com/hachiwar/Chinese-Document-Style-and-Typography-Guidelines)

## 安装

### Codex

将目标技能目录复制到 Codex 技能目录：

```powershell
Copy-Item -Recurse chinese-document-style "$HOME\.codex\skills\"
```

重新启动 Codex 后，可以显式调用：

```text
使用 $chinese-document-style 审校这份中文技术报告。
```

### Claude Code

将 Claude 版技能复制到项目或用户级技能目录。项目级示例：

```powershell
New-Item -ItemType Directory -Force ".claude\skills" | Out-Null
Copy-Item -Recurse claude-chinese-document-style ".claude\skills\"
```

调用示例：

```text
使用 claude-chinese-document-style 审校这份中文技术报告。
```

## 目录约定

- Codex 技能包含 `SKILL.md`、按需加载的 `references/`，以及用于界面展示的 `agents/openai.yaml`。
- Claude Code 技能包含 `SKILL.md` 和按需加载的 `references/`。
- 详细规则放入 `references/`，避免在每次触发技能时占用不必要的上下文。

## 现有技能

### Unicode 编码诊断与修复

- [`fix-unicode-decode`](fix-unicode-decode/)：诊断并修复 `UnicodeDecodeError`、中文乱码和跨平台文本编码问题。
- [`claude-fix-unicode-decode`](claude-fix-unicode-decode/)：面向 Claude Code 的 Unicode 解码与中文乱码诊断技能。
