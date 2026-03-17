# draw-io — AI Agent 的图表工程化技能

> 让 Agent 像编辑代码一样管理架构图：直接操作 XML 源码，自动转换为高保真 PNG，确保每一张图表都达到出版级质量。

## 这个 Skill 能做什么

| 核心能力 | 说明 |
|---------|------|
| **XML 源码编辑** | Agent 直接读写 `.drawio` 文件的 XML 结构，实现像素级精准定位 |
| **自动化 PNG 转换** | 通过脚本一键生成 2 倍分辨率、透明背景的 PNG 成品图 |
| **AWS 架构图支持** | 内置官方 AWS 图标搜索工具，快速定位 600+ 服务图标 |
| **专业视觉规范** | 预设字体、间距、分层等设计准则，输出即专业 |

## 适用场景

- 需要创建或修改 AWS / 通用架构图
- 需要将图表集成到演示文稿（Quarto / reveal.js）中
- 需要批量调整元素布局与对齐
- 需要确保团队图表风格统一

## 快速上手

### 1. 安装依赖

- **draw.io CLI**：[下载地址](https://github.com/jgraph/drawio-desktop/releases)
- **Python 3.x**：用于 AWS 图标搜索脚本

### 2. 搜索 AWS 图标

```bash
python scripts/find_aws_icon.py ec2
# 输出：Service: Amazon EC2 / resIcon: mxgraph.aws4.ec2
```

### 3. 转换图表为 PNG

```bash
# 方式一：通过 pre-commit 钩子(推荐)
mise exec -- pre-commit run convert-drawio-to-png --files your-diagram.drawio

# 方式二：直接运行脚本
bash scripts/convert-drawio-to-png.sh your-diagram.drawio
```

## 设计理念：图表即代码

传统绘图依赖拖拽操作，难以保证像素级对齐和团队风格一致。本 Skill 采用 **Diagram as Code** 的思路：

1. **源码可控**：`.drawio` 本质是 XML，可以用文本编辑器精准调整坐标。
2. **版本可追踪**：XML 文件纳入 Git 管理，变更一目了然。
3. **输出可自动化**：通过 CI/CD 或 pre-commit 钩子，"提交即产出"。

## 文件结构

```
draw-io/
├── SKILL.md                          # Agent 操作指令集（英文）
├── README.md                         # 面向开发者的介绍文档（本文件）
├── scripts/
│   ├── convert-drawio-to-png.sh     # PNG 转换脚本
│   └── find_aws_icon.py             # AWS 图标搜索工具
└── references/
    ├── layout-guidelines.md         # 布局与间距规范
    └── aws-icons.md                 # AWS 图标速查目录（600+）
```

## Agent 如何使用此 Skill

Agent 在被要求创建或编辑图表时，会自动加载 `SKILL.md` 中的操作指令。核心工作流：

1. 读取或创建 `.drawio` XML 文件
2. 按照 `SKILL.md` 中的布局规范（30px 边距等）编辑 `mxCell` 元素
3. 调用转换脚本生成 PNG
4. 按照质量检查清单逐项验证

> 详细的操作规则、XML 代码示例和质量检查清单见 [SKILL.md](SKILL.md)。

## 参考

- [draw.io 官方文档](https://www.drawio.com/doc/)
- [AWS Architecture Icons](https://aws.amazon.com/architecture/icons/)
- [draw.io GitHub](https://github.com/jgraph/drawio)
