# Execution Plan v3.4

日期：2026-05-25  
目标：把 v3.3 的模型自省转成可执行优化，补上早期发现、估值赔率、主题 beta 剥离、叙事漂移和 no-trade 纪律。  
说明：这是研究框架，不是个人投资建议。

## 1. 本轮优化原则

v3.4 不追求更多公司，也不追求更复杂估值。  
本轮只补五件事：

1. 早期信号：记录确认前的弱信号，但不让弱信号直接触发大仓位。
2. 估值赔率：把“thesis 变强”和“现在能不能买”分开。
3. 主题 beta 剥离：判断个股是否真的跑赢主题篮子。
4. 叙事漂移：买入理由和持有理由变了，必须标记。
5. 不做规则：让模型明确输出 no-trade，而不是永远寻找交易。

## 2. 新增文件

| 文件 | 用途 |
|---|---|
| `pre_confirmation_signal_log_v1.csv` | 记录财报确认前的弱信号和升级条件 |
| `prospective_event_ledger_v2.csv` | 增强前瞻事件账本，加入估值、信息质量、主题 beta、叙事漂移 |
| `no_trade_checklist_v1.csv` | 强制记录不做条件 |
| `model_validation_protocol_v1.md` | 定义方向、公司 alpha、执行时点三层验证 |

## 3. 执行流程

### Step 1: 先入早期信号日志

任何还没有被财报或订单确认的想法，先进入 `pre_confirmation_signal_log_v1.csv`。

允许动作：

- `research_only`
- `watch`
- `tiny_tracking_only`

不允许动作：

- 加重仓。
- 因 C/D 级信息买入。
- 用多个假设把故事讲圆。

### Step 2: 触发条件升级后才进入事件账本

早期信号只有在出现 A/B 级信息后，才进入 `prospective_event_ledger_v2.csv`。

A/B 级信息包括：

- 官方订单、backlog、guide、10-Q/10-K。
- 客户/供应商交叉验证。
- 产品认证、样品、量产、复购。
- 同赛道大客户路线图明确变化。

### Step 3: 每个事件先跑 no-trade checklist

如果 `no_trade_checklist_v1.csv` 命中硬性条件，即使 thesis 变强，也默认不做或只观察。

### Step 4: 事件后拆三层评价

每个事件后不只看涨跌，而是拆成：

1. 方向识别：主题篮子是否跑赢 QQQ/SMH。
2. 公司 alpha：个股是否跑赢主题篮子。
3. 执行时点：行动是否改善收益/回撤。

只有三层都通过，才说明模型真的有 edge。

## 4. 当前优先动作

短期先不扩名单，只把已有候选放进新结构：

- `SMTC`：事件账本 v2，测试主题 beta 剥离。
- `MOD`：事件账本 v2，测试 power/cooling 主题 beta 剥离。
- `POET`：早期信号日志，样品/量产/客户确认前不升级。
- `AXTI`：早期信号日志，InP 需求和出口许可需要进一步验证。
- `PPSI`：早期信号日志，PRYMUS 订单和现金流验证前只观察。
- `FORM`：早期信号日志，HBM/probe thesis 需客户或订单确认。

## 5. 完成标准

v3.4 不以“文件完成”为成功。成功标准是：

- 每个新想法先被分到 early signal 或 event ledger。
- 每个交易前都能写出 no-trade 是否命中。
- 每个结果都能拆出 theme beta 和 company alpha。
- 每次 thesis 改变都能标记 drift。
- 10 个事件后能删掉无用字段，而不是继续加字段。
