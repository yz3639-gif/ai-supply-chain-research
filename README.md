# AI 供应链研究包

日期：2026-05-25  
状态：已升级为 v3.4 执行优化系统。旧报告没有删除，已移入归档。

## 快速入口

当前默认使用：

- `00_active_system/execution_plan_v3_4.md`：v3.4 执行方案，当前默认入口。
- `00_active_system/lean_decision_system_v1.md`：默认精简决策规则。
- `00_active_system/pre_confirmation_signal_log_v1.csv`：确认前早期信号日志。
- `00_active_system/prospective_event_ledger_v2.csv`：增强前瞻事件账本，加入估值状态、信息质量、主题 beta 和叙事漂移。
- `00_active_system/no_trade_checklist_v1.csv`：不做清单，防止模型为了交易而交易。
- `00_active_system/model_validation_protocol_v1.md`：模型有效性验证协议，拆分方向、公司 alpha 和执行时点。
- `00_active_system/realtime_report_2026-05-25.md`：基于最新公开信息生成的实时信息层报告。
- `00_active_system/simple_event_checklist_v1.csv`：最小事件 checklist。
- `00_active_system/decision_journal_simple_v1.md`：简单复盘日志。
- `00_active_system/framework_validity_audit_v1.md`：有效性审计。
- `00_active_system/self_reflection_v3_2.md`：自省记录。
- `00_active_system/model_self_reflection_v3_3.md`：模型层面的自省，重点是早期发现能力、估值赔率、主题 beta 和叙事漂移。
- `00_active_system/optimization_plan_v3_3.md`：v3.3 优化方案，作为上一版参考。
- `00_active_system/AI供应链完整深挖总报告_v3_决策系统版.md`：总报告。

## 目录说明

| 目录 | 内容 |
|---|---|
| `00_active_system/` | 当前默认规则和前瞻验证工具 |
| `01_reference_models/` | 瓶颈指数、公司模型、估值、事件 checklist、压力测试等参考材料 |
| `02_company_deep_dives/` | ACMR、CAMT、HPS、MXL、ONTO、SMTC/MTSI/VECO/POWL/MOD/FORM 等公司深挖 |
| `03_backtests_and_scripts/` | walk-forward、主题回测、事件研究脚本和结果 |
| `04_watchlists_strategy/` | watchlist、策略名册、催化剂日历、战术/组合表 |
| `99_archive_superseded/` | v3.3 之前的旧报告、根目录重复文件和缓存 |

## 使用原则

1. 默认从 `00_active_system/` 开始，不再从旧 v1/v2 报告做决策。
2. `01_reference_models/` 只作研究辅助，不直接触发交易。
3. 每个新想法先写入 `pre_confirmation_signal_log_v1.csv`；只有出现 A/B 级确认后，才升级到 `prospective_event_ledger_v2.csv`。
4. 每个交易前先跑 `no_trade_checklist_v1.csv`；如果只是主题 beta 或估值赔率差，默认不加仓。
5. 每个事件后按方向、公司 alpha、执行时点三层复盘，不能只用股价涨跌证明模型有效。
6. 旧文件保留在 `99_archive_superseded/`，需要时可以恢复。

## 整理记录

详见 `整理清单_2026-05-25.md`。
