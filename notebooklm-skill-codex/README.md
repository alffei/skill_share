# NotebookLM Codex Skill

这是一个面向 Codex 的本地 NotebookLM skill，用于通过浏览器自动化访问 Google NotebookLM，并基于用户已上传的资料获得带来源约束的回答。

## 这个 skill 能做什么

- 通过可见浏览器完成 Google / NotebookLM 登录
- 在本地维护 NotebookLM notebook 列表
- 对指定 notebook 发起提问
- 基于 NotebookLM 返回结果继续追问，再综合输出最终答案
- 尽量减少直接喂文档给模型带来的上下文消耗与幻觉风险

## 适用环境

请只在本地 Codex 环境中使用，并确保当前环境能够：

- 执行 shell 命令
- 创建 Python 虚拟环境
- 安装 Python 依赖
- 访问外网
- 打开可见浏览器窗口

如果当前环境无法联网、无法安装依赖，或者无法启动浏览器，这个 skill 就不能正常工作。

## 安装方式

将本目录放到 Codex 的 skill 目录下，目录名建议为 `notebooklm`：

```bash
mkdir -p ~/.codex/skills
cd ~/.codex/skills
git clone <repo-url> notebooklm
```

如果不是通过 Git，也可以手动复制目录。最终结构应类似：

```text
~/.codex/skills/notebooklm/
├── SKILL.md
├── agents/openai.yaml
├── scripts/
├── references/
└── requirements.txt
```

## 工作方式

当用户提到 NotebookLM、提供 NotebookLM 链接，或要求从已上传资料中获得更可靠答案时，Codex 会触发这个 skill。

典型流程如下：

1. 读取 [SKILL.md](./SKILL.md)
2. 通过 `python scripts/run.py ...` 调用脚本
3. 首次使用时自动创建 `.venv`
4. 自动安装依赖与 Patchright 所需的 Chrome
5. 打开 NotebookLM，读取回答
6. 必要时继续追问，再整理成最终答复

## 首次使用

建议先检查认证状态：

```bash
python scripts/run.py auth_manager.py status
```

首次执行会自动：

- 创建 `.venv`
- 安装 `requirements.txt` 中的依赖
- 安装 Patchright 使用的 Chrome 运行时

如果之前初始化被中断，重新执行同一个命令即可。新的启动逻辑会识别并修复“不完整 `.venv`”。

如果尚未登录，执行：

```bash
python scripts/run.py auth_manager.py setup
```

浏览器会打开，用户需要手动完成 Google 登录。

## 安装行为与镜像源

依赖安装现在会直接输出 `pip` 日志，不再长时间静默停在 `Installing dependencies...`。

如果你的网络无法访问 `pypi.org`，可以先指定镜像源再运行命令：

```bash
export NOTEBOOKLM_PIP_INDEX_URL=https://pypi.tuna.tsinghua.edu.cn/simple
python scripts/run.py auth_manager.py status
```

也支持调整 pip 超时和重试次数：

```bash
export NOTEBOOKLM_PIP_TIMEOUT=15
export NOTEBOOKLM_PIP_RETRIES=1
```

默认策略会尽快失败并给出提示，避免首次安装在无输出状态下长时间等待。

## 常用命令

列出已保存的 notebooks：

```bash
python scripts/run.py notebook_manager.py list
```

直接对 notebook 链接提问：

```bash
python scripts/run.py ask_question.py \
  --question "这个 notebook 关于 React hooks 是怎么说明的？" \
  --notebook-url "https://notebooklm.google.com/notebook/..."
```

更多命令可查看：

- [references/commands.md](./references/commands.md)

排障可查看：

- [references/troubleshooting-codex.md](./references/troubleshooting-codex.md)

## 说明

- skill 数据保存在当前 skill 目录下的 `data/`
- 首次运行会自动生成 `.venv`
- `.venv/.notebooklm-skill-ready` 用于标记初始化是否完整
- 当前实现使用 Patchright，并安装 `chrome` 运行时
- 每次提问默认会打开新的浏览器会话
- 如果 NotebookLM 页面结构变化，脚本中的选择器可能需要更新

## 适用边界

这个 skill 适合本地 Codex 调用，不是 MCP server 版本。

如果你的目标是：

- 让多个 agent / 工具共用 NotebookLM 能力
- 通过标准 MCP 方式接入更多客户端
- 使用更强的持久会话能力

那么更适合考虑原作者提供的 MCP 方案，而不是这个本地 skill 版本。



## 致谢与来源

本 skill 的适配版本修改自原项目：

- [PleasePrompto/notebooklm-skill](https://github.com/PleasePrompto/notebooklm-skill)

感谢原作者提供完整的 NotebookLM skill 设计、脚本实现和思路基础。本仓库在其工作之上，调整为更适合 Codex 使用的本地 skill 结构与说明。
