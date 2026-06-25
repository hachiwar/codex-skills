# 中文文档风格与排版技能

## 1. 技能概述

本仓库分别提供 Codex 与 Claude Code 版本：

- [`chinese-document-style`](../chinese-document-style/)：适用于 Codex；
- [`claude-chinese-document-style`](../claude-chinese-document-style/)：适用于 Claude Code。

两个技能用于创建、审校和修订简体中文文档，强调学术性、技术性、规范性与排版一致性。技能在修订文本时保留原有事实、论证、引用、专业术语和技术语义，不以文体优化为由改变结论强度。

## 2. 适用场景

技能适用于：

- 学术报告、课程报告和研究型项目文档；
- 技术报告、设计说明和技术规范；
- 项目 README、开发者文档和知识库；
- 产品说明、帮助文档和正式中文文案；
- 中文 Markdown 文件的格式与语言审校；
- 口语化、宣传化和模式化 AI 表达的识别与修订。

## 3. 主要能力

### 3.1 语言风格

- 使用客观、正式和基于证据的表达；
- 区分事实、推测、建议和强制要求；
- 保留实验条件、限制、不确定性和负面结果；
- 避免无依据的“最佳”“最先进”“显著领先”等表述；
- 删除口号、反问、过度情绪和缺少信息量的模式化衔接语；
- 统一术语、人称和论证强度。

### 3.2 排版规范

- 处理中英文与数字之间的空格；
- 统一全角、半角和中文标点；
- 规范数字、日期、时间、单位和范围符号；
- 保留代码、URL、路径、公式和标识符的固定语法；
- 统一引号、括号、省略号和破折号；
- 检查标题层级、段落结构、列表和表格。

### 3.3 学术与技术完整性

- 保留引用键、脚注、参考文献和直接引语；
- 保留公式、图表编号和交叉引用；
- 不虚构标准、日期、数据或文献；
- 不将相关关系改写为因果关系；
- 不将推荐性表述改写为强制性表述；
- 在未指定引用格式时保留文档现有格式。

## 4. 规范依据

技能的规则体系主要参考：

1. [sparanoid/chinese-copywriting-guidelines](https://github.com/sparanoid/chinese-copywriting-guidelines)
2. [yikeke/zh-style-guide](https://github.com/yikeke/zh-style-guide)
3. Hindy Hong 的《[写给大家看的中文排版指南](https://zhuanlan.zhihu.com/p/20506092)》
4. [hachiwar/Chinese-Document-Style-and-Typography-Guidelines](https://github.com/hachiwar/Chinese-Document-Style-and-Typography-Guidelines)

技能对不同来源的规则进行了分级处理：

- 法律法规、国家标准、行业标准和机构要求优先；
- 产品、协议和专有名词采用官方写法；
- 项目内部已经声明的术语与格式优先于通用建议；
- 存在多种合理方案时，将规则视为项目选项，不将个人偏好表述为错误。

## 5. 安装

### 5.1 Codex

将 Codex 技能目录复制到用户技能目录：

```powershell
Copy-Item -Recurse chinese-document-style "$HOME\.codex\skills\"
```

重新启动 Codex 后，可以显式调用：

```text
使用 $chinese-document-style 审校这份中文技术报告。
```

### 5.2 Claude Code

将 Claude Code 技能复制到项目级或用户级技能目录。项目级示例：

```powershell
New-Item -ItemType Directory -Force ".claude\skills" | Out-Null
Copy-Item -Recurse claude-chinese-document-style ".claude\skills\"
```

调用示例：

```text
使用 claude-chinese-document-style 审校这份中文技术报告。
```

## 6. 使用示例

### 6.1 全文审校

```text
使用 $chinese-document-style 审校 report.md。
保持引用和实验结论不变，修正中文排版，并将语言调整为学术报告风格。
```

### 6.2 仅检查问题

```text
使用 $chinese-document-style 检查 README.md。
不要修改文件，按正确性、一致性和可读性分类报告问题。
```

### 6.3 规范团队文档

```text
使用 $chinese-document-style 统一 docs/ 下的中文文档。
保留代码、链接、路径和产品官方名称，并检查 Markdown 标题层级。
```

## 7. 文件结构

Codex 版本：

```text
chinese-document-style/
├── SKILL.md
├── agents/
│   └── openai.yaml
└── references/
    └── chinese-style-guide.md
```

Claude Code 版本：

```text
claude-chinese-document-style/
├── SKILL.md
└── references/
    └── chinese-style-guide.md
```

`SKILL.md` 保存核心工作流与触发条件，`references/chinese-style-guide.md` 保存按需加载的详细规范。
