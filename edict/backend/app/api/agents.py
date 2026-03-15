"""Agents API — Agent 配置和状态查询。"""

import json
import logging
from pathlib import Path

from fastapi import APIRouter

log = logging.getLogger("edict.api.agents")
router = APIRouter()

# Agent 元信息（对应 agents/ 目录下的 SOUL.md）
AGENT_META = {
    "zaochao": {"name": "数据简报", "role": "数据采集与报表生成", "icon": "📈"},
    "shangshu": {"name": "项目经理", "role": "任务派发与进度管理", "icon": "📊"},
    "zhongshu": {"name": "产品经理", "role": "需求分析与方案设计", "icon": "📋"},
    "menxia": {"name": "质量审核", "role": "审核与质量把关", "icon": "✅"},
    "libu": {"name": "内容运营", "role": "内容策划与文案撰写", "icon": "📝"},
    "hubu": {"name": "财务", "role": "财务与资源管理", "icon": "💰"},
    "gongbu": {"name": "运维部", "role": "工程与技术实施", "icon": "🔧"},
    "xingbu": {"name": "合规部", "role": "规范与质量审查", "icon": "⚖️"},
    "bingbu": {"name": "研发部", "role": "技术攻关与系统开发", "icon": "💻"},
    "live_ops": {"name": "直播运营", "role": "直播间运营与主播管理", "icon": "🎬"},
    "store_ops": {"name": "店铺运营", "role": "店铺日常运营与优化", "icon": "🏪"},
    "sourcing": {"name": "选品", "role": "商品选品与市场分析", "icon": "🎯"},
    "procurement": {"name": "采购跟单", "role": "采购执行与供应商管理", "icon": "📦"},
}


@router.get("")
async def list_agents():
    """列出所有可用 Agent。"""
    agents = []
    for agent_id, meta in AGENT_META.items():
        agents.append({
            "id": agent_id,
            **meta,
        })
    return {"agents": agents}


@router.get("/{agent_id}")
async def get_agent(agent_id: str):
    """获取 Agent 详情。"""
    meta = AGENT_META.get(agent_id)
    if not meta:
        return {"error": f"Agent '{agent_id}' not found"}, 404

    # 尝试读取 SOUL.md
    soul_path = Path(__file__).parents[4] / "agents" / agent_id / "SOUL.md"
    soul_content = ""
    if soul_path.exists():
        soul_content = soul_path.read_text(encoding="utf-8")[:2000]

    return {
        "id": agent_id,
        **meta,
        "soul_preview": soul_content,
    }


@router.get("/{agent_id}/config")
async def get_agent_config(agent_id: str):
    """获取 Agent 运行时配置。"""
    config_path = Path(__file__).parents[4] / "data" / "agent_config.json"
    if not config_path.exists():
        return {"agent_id": agent_id, "config": {}}

    try:
        configs = json.loads(config_path.read_text(encoding="utf-8"))
        agent_config = configs.get(agent_id, {})
        return {"agent_id": agent_id, "config": agent_config}
    except (json.JSONDecodeError, IOError):
        return {"agent_id": agent_id, "config": {}}
