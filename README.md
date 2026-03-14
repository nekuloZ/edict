<h1 align="center">🏪 电商 Agent 运营系统</h1>

<p align="center">
  <strong>专为电商公司设计的 AI 多 Agent 协作系统<br>实时看板 · 质量审核 · 完全可观测</strong>
</p>

<p align="center">
  <sub>15 个专业 Agent 组成完整运营团队：前台分拣、产品经理规划、质量审核把关、项目经理派发、各部门并行执行。<br>比 CrewAI 多一层<b>制度性审核</b>，比 AutoGen 多一个<b>实时看板</b>。</sub>
</p>

<p align="center">
  <a href="#-快速体验">🚀 快速体验</a> ·
  <a href="#-架构">🏛️ 架构</a> ·
  <a href="#-功能全景">📋 功能</a> ·
  <a href="#-agent-列表">🤖 Agent</a> ·
  <a href="docs/task-dispatch-architecture.md">📚 架构文档</a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/OpenClaw-Required-blue?style=flat-square" alt="OpenClaw">
  <img src="https://img.shields.io/badge/Python-3.9+-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Agents-15_Specialized-8B5CF6?style=flat-square" alt="Agents">
  <img src="https://img.shields.io/badge/Dashboard-Real--time-F59E0B?style=flat-square" alt="Dashboard">
  <img src="https://img.shields.io/badge/License-MIT-22C55E?style=flat-square" alt="License">
</p>

---

## 🤔 为什么选择电商 Agent 运营系统？

大多数 Multi-Agent 框架的问题是：

> *"来，你们几个 AI 自己聊，聊完把结果给我。"*

然后你拿到一坨不知道经过了什么处理的结果，无法复现，无法审计，无法干预。

**电商 Agent 运营系统完全不同**：

```
用户 → 前台(分拣) → 产品经理(规划) → 质量审核(把关) → 项目经理(派发) → 各部门(执行) → 汇报
                                            ↑____驳回____|
```

这是**真正的分权制衡**：

| | CrewAI | MetaGPT | AutoGen | **电商 Agent 运营系统** |
|---|:---:|:---:|:---:|:---:|
| **审核机制** | ❌ 无 | ⚠️ 可选 | ⚠️ Human-in-loop | **✅ 质量审核专职把关 · 可驳回** |
| **实时看板** | ❌ | ❌ | ❌ | **✅ 运营中心 Kanban + 时间线** |
| **任务干预** | ❌ | ❌ | ❌ | **✅ 叫停 / 取消 / 恢复** |
| **流转审计** | ⚠️ | ⚠️ | ❌ | **✅ 完整报告存档** |
| **Agent 监控** | ❌ | ❌ | ❌ | **✅ 心跳 + 活跃度检测** |
| **热切换模型** | ❌ | ❌ | ❌ | **✅ 看板内一键切换 LLM** |
| **技能管理** | ❌ | ❌ | ❌ | **✅ 查看 / 添加 Skills** |
| **部署难度** | 中 | 高 | 中 | **低 · 一键安装 / Docker** |

> **核心差异：制度性审核 + 完全可观测 + 实时可干预**

---

## 🚀 快速体验

### Docker 一键启动

```bash
docker run -p 7891:7891 nekuloZ/ecommerce-agent-ops
```

打开 http://localhost:7891 即可体验运营中心看板。

### 本地安装

**前置条件：**
- [OpenClaw](https://openclaw.ai) 已安装
- Python 3.9+
- Node.js 18+（可选，用于构建前端）

```bash
git clone https://github.com/nekuloZ/ecommerce-agent-ops.git
cd ecommerce-agent-ops
chmod +x install.sh && ./install.sh
```

安装脚本自动完成：
- ✅ 创建 15 个 Agent Workspace
- ✅ 写入各部门 SOUL.md（角色定义）
- ✅ 注册 Agent 及权限矩阵
- ✅ 构建前端（如已安装 Node.js）
- ✅ 重启 Gateway 使配置生效

**启动服务：**

```bash
# 终端 1：数据刷新循环
bash scripts/run_loop.sh

# 终端 2：看板服务器
python3 dashboard/server.py

# 打开浏览器
open http://127.0.0.1:7891
```

---

## 🏛️ 架构

```
┌───────────────────────────────────┐
│ 👤 用户                            │
│ Feishu · Telegram · Signal        │
└─────────────────┬─────────────────┘
                  │ 下发任务
┌─────────────────▼─────────────────┐
│ 🤵 前台 (taizi)                    │
│ 分拣：闲聊直接回 / 任务建单        │
└─────────────────┬─────────────────┘
                  │ 传达需求
┌─────────────────▼─────────────────┐
│ 📜 产品经理 (zhongshu)             │
│ 接需求 → 规划 → 拆解子任务         │
└─────────────────┬─────────────────┘
                  │ 提交审核
┌─────────────────▼─────────────────┐
│ 🔍 质量审核 (menxia)               │
│ 审议方案 → 通过 / 驳回 🚫          │
└─────────────────┬─────────────────┘
                  │ 通过 ✅
┌─────────────────▼─────────────────┐
│ 📮 项目经理 (shangshu)             │
│ 派发任务 → 协调各部门 → 汇总汇报   │
└───┬──────┬──────┬──────┬──────┬───┘
    │      │      │      │      │
    ▼      ▼      ▼      ▼      ▼
┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐
│💰   │ │📝   │ │⚔️   │ │⚖️   │ │🔧   │
│财务 │ │内容 │ │研发 │ │合规 │ │运维 │
└─────┘ └─────┘ └─────┘ └─────┘ └─────┘
    │      │
    ▼      ▼
┌─────┐ ┌─────┐
│🎬   │ │🏪   │
│直播 │ │店铺 │
└─────┘ └─────┘
    │      │
    ▼      ▼
┌─────┐ ┌─────┐
│🎯   │ │📦   │
│选品 │ │采购 │
└─────┘ └─────┘
```

---

## 🤖 Agent 列表

### 核心流程

| 部门 | Agent ID | 职责 |
|------|----------|------|
| 前台 | taizi | 消息分拣、需求整理 |
| 产品经理 | zhongshu | 规划拆解、方案设计 |
| 质量审核 | menxia | 审核把关、驳回 |
| 项目经理 | shangshu | 派发协调、进度跟踪 |

### 执行部门

| 部门 | Agent ID | 职责 |
|------|----------|------|
| 财务 | hubu | 成本核算、财务报表、资金管理 |
| 内容运营 | libu | 内容策划、文案撰写、社交媒体 |
| 研发部 | bingbu | 代码开发、系统维护 |
| 合规部 | xingbu | 合规检查、风险控制 |
| 运维部 | gongbu | 基础设施、部署监控 |
| 人力资源 | libu_hr | 人事管理、Agent管理 |

### 电商专项

| 部门 | Agent ID | 职责 |
|------|----------|------|
| 直播运营 | live_ops | 直播策划、主播管理、直播数据 |
| 店铺运营 | store_ops | 店铺管理、活动策划、商品运营 |
| 选品 | sourcing | 商品选品、市场分析、竞品调研 |
| 采购跟单 | procurement | 采购流程、供应商对接、订单跟进 |
| 数据简报 | zaochao | 店铺数据、直播数据、销售报表 |

---

## 📋 功能全景

### 运营中心看板（10 个功能面板）

| 面板 | 功能 |
|------|------|
| **任务看板** | 按状态列展示、部门过滤、心跳徽章、任务干预 |
| **部门调度** | 任务数量可视化、Agent 健康状态实时卡片 |
| **报告阁** | 已完成任务归档、五阶段时间线、Markdown 导出 |
| **任务模板** | 预设模板、参数表单、一键下发 |
| **模型配置** | 每个 Agent 独立切换 LLM |
| **技能配置** | 查看/添加 Skills |
| **会话监控** | 实时会话列表、消息预览 |
| **数据简报** | 每日运营数据汇总 |

---

## 📊 任务流转

```
用户 → 前台分拣 → 产品经理规划 → 质量审核审议 → 已派发 → 执行中 → 待审查 → ✅ 已完成
                    ↑____驳回____|                    阻塞 Blocked
```

---

## 🔧 技术栈

- **前端**: React 18 + TypeScript + Vite + Zustand
- **后端**: Python stdlib (http.server)，零依赖
- **看板**: 单文件 dashboard.html
- **平台**: [OpenClaw](https://openclaw.ai)

---

## 📁 项目结构

```
ecommerce-agent-ops/
├── agents/                 # 15 个 Agent 角色定义
│   ├── taizi/SOUL.md       # 前台
│   ├── zhongshu/SOUL.md    # 产品经理
│   ├── menxia/SOUL.md      # 质量审核
│   ├── shangshu/SOUL.md    # 项目经理
│   ├── hubu/SOUL.md        # 财务
│   ├── libu/SOUL.md        # 内容运营
│   ├── bingbu/SOUL.md      # 研发部
│   ├── xingbu/SOUL.md      # 合规部
│   ├── gongbu/SOUL.md      # 运维部
│   ├── libu_hr/SOUL.md     # 人力资源
│   ├── live_ops/SOUL.md    # 直播运营
│   ├── store_ops/SOUL.md   # 店铺运营
│   ├── sourcing/SOUL.md    # 选品
│   ├── procurement/SOUL.md # 采购跟单
│   └── zaochao/SOUL.md     # 数据简报
├── dashboard/
│   ├── dashboard.html      # 运营中心看板
│   └── server.py           # API 服务器
├── scripts/                # 工具脚本
├── docs/                   # 文档
└── install.sh              # 一键安装
```

---

## 📄 License

[MIT](LICENSE) · Forked from [cft0808/edict](https://github.com/cft0808/edict)

---

## 🙏 致谢

本项目基于 [Edict (三省六部制)](https://github.com/cft0808/edict) 改造，将古代角色术语替换为现代企业术语，并新增电商公司特有部门，更适合电商场景使用。
