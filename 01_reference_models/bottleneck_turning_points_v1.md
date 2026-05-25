# Bottleneck Turning Points v1

日期：2026-05-25  
用途：把 AI 供应链瓶颈迁移从事后叙事改为公开可见转折点记录。  
说明：这是研究框架，不是个人投资建议。

## 方法原则

v3 不做 GPU 月度产能缺口的伪精确估算。公开市场无法稳定取得 NVIDIA GPU 月度出货、TSMC/Samsung HPC 月度产能释放、真实 hyperscaler 未公开订单。因此，瓶颈系统分两层：公开转折点和辅助指数。

## 四个已验证转折点

| 阶段 | 时间窗口 | 主瓶颈 | 可见证据 | 不能知道的盲区 |
|---|---|---|---|---|
| TP1 | 2023Q4-2024Q2 | GPU 主瓶颈 | NVIDIA FY2024/FY2025 数据中心加速，H100/H200 需求强，TSMC/先进封装产能紧张被公开讨论 | 真实 hyperscaler 逐月订单、GPU 实际交期 |
| TP2 | 2024Q3 起 | HBM/先进封装接力 | HBM、CoWoS、advanced packaging、probe/inspection 订单与行业报告增强 | 每家 HBM 客户实际 allocation、良率曲线 |
| TP3 | 2024Q4-2025 | 光通信升温 | 800G/1.6T 光模块、PMD/TIA/DSP、InP laser、CPO/NPO 公开订单和产品语言增强 | hyperscaler 内部网络架构切换节奏 |
| TP4 | 2024Q4 至今 | 电力散热 backlog 拉长 | POWL/MOD/AAON/FIX/VRT/HPS backlog、订单、数据中心需求披露增强 | 项目取消率、真实交付瓶颈、客户建设节奏 |

## 使用规则

- 转折点用于定义阶段，不用于单票买入。
- 辅助指数用于回答该阶段是否仍在增强、是否已经拥挤、是否需要等待下一次事件确认。
- 如果 `hard_data_ratio < 50%`，即使分数高，也只能标为潜在瓶颈，不得标主瓶颈。
- 管理层 Q&A 只做备注，不进入核心权重。
