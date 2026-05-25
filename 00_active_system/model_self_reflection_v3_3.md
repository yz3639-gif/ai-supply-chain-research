# Model Self Reflection v3.3

日期：2026-05-25  
用途：自省 AI 供应链决策模型本身的缺陷，不讨论 GitHub 或文件管理。  
说明：这是研究框架，不是个人投资建议。

## 1. 当前模型真实状态

v3.3 比 v2/v3 更诚实，但仍然不是成熟投资模型。

它现在更像一个“决策卫生系统”：

- 防止伪精确。
- 防止同主题过度下注。
- 强制事件前记录 thesis 和证伪条件。
- 用前瞻事件账本积累样本。

但它还不是“发现系统”或“可证明有 edge 的交易系统”。

这一区分非常重要。  
如果我们想提前押注 AI 供应链卡点，仅靠财报后的 `beat / raise / thesis evidence` 是不够的。那会让模型偏向确认后买入，而不是提前识别未被定价的瓶颈。

## 2. 当前最大的模型缺口

### 2.1 它偏事件确认，不偏早期发现

Lean checklist 问的是：

- 结果是否 beat？
- outlook 是否 raise？
- thesis 是否有新证据？

这适合避免追错，但不一定适合提前发现。

真正的早期机会往往发生在：

- 公司还没 beat。
- guide 还没 raise。
- 财报语言还含糊。
- 市场还没把它归入 AI supply chain。

如果模型只等确认，它可能更安全，但会错过高赔率早期位置。

修正方向：

新增一个“pre-confirmation signal”层，但不能伪精确。它只记录观察，不触发大仓位。

可观察信号包括：

- 上游订单或 capex 先动，而目标公司收入还没动。
- 客户产品路线图变更。
- 交付周期或 backlog 语言开始变长。
- 供应链小公司招聘、产能、认证、样品、合作公告出现。
- 同赛道大公司 call 中反复提到某个组件或 bottleneck。
- 目标公司开始被客户生态引用，但 sell-side 还没覆盖。

### 2.2 它没有处理“好公司但已经太贵”

当前系统有 portfolio risk 问题，但估值纪律还不够硬。  
`beat + raise + thesis evidence` 仍然可能是坏买点，因为市场已经提前定价。

需要把每个事件分成两件事：

1. thesis 是否变强。
2. 当前价格是否还有赔率。

如果 thesis 变强但赔率变差，正确动作可能是“不买”。

修正方向：

每个事件账本增加一列：

- `valuation_state`: cheap / fair / stretched / extreme
- `price_reaction_risk`: low / medium / high

### 2.3 它没有区分“主题 beta”和“公司 alpha”

很多 AI supply chain 股票上涨，不一定是公司判断对了，可能只是主题 beta。  
如果我们不拆分，会误以为模型有效。

例子：

- 光通信整组涨，SMTC/MTSI/MXL 全涨，这不证明选股有效。
- 电力散热整组涨，POWL/MOD/AAON/FIX/VRT 同涨，这不证明某个小公司 thesis 被验证。

修正方向：

前瞻账本必须记录：

- individual_return
- theme_basket_return
- QQQ_return
- SMH_return
- alpha_vs_theme

只有 `alpha_vs_theme` 为正，且 thesis 被验证，才能说公司判断有效。

### 2.4 它没有约束“叙事漂移”

AI 供应链研究很容易发生叙事漂移：

原 thesis：光通信材料卡点。  
后来股价没动，于是改成：AI networking 长周期。  
再后来又改成：机器人/端侧/磁材。

如果 thesis 可以随时改，模型永远不会错。

修正方向：

每条事件必须有：

- `original_thesis`
- `allowed_thesis_update`
- `thesis_drift_flag`

如果买入理由和持有理由不同，必须标记 drift。  
drift 不一定错，但它不能被当作原 thesis 成功。

### 2.5 它还没有区分“信息质量”

当前只说 official / derived / proxy，但还不够。  
真正做决策时，信息质量至少要分：

| 等级 | 信息类型 | 用途 |
|---|---|---|
| A | 官方订单、backlog、guide、10-Q/10-K | 可作为核心证据 |
| B | 客户/供应商交叉验证、行业报告、产品认证 | 可增强 thesis |
| C | 管理层泛泛语言、媒体报道、sell-side 评论 | 只能提示方向 |
| D | 论坛、传闻、无来源 market share | 不进入决策 |

如果一个 thesis 主要由 C/D 信息支撑，只能是观察仓或研究任务，不能是投资结论。

### 2.6 它没有明确“何时不做”

一个好模型最重要的输出之一是：不做。

当前系统虽然说“默认不加仓”，但还不够明确。应该有硬性 no-trade 条件：

- 事件前价格已经极端延展，但没有新证据。
- 同主题仓位已经过高。
- thesis 主要靠 C/D 级信息。
- 公司现金流恶化但 narrative 变强。
- 只能用 3 个以上假设才能讲通。
- 无法写出明确证伪条件。

## 3. 对 v3.3 的评分

| 维度 | 当前评分 | 说明 |
|---|---:|---|
| 诚实度 | 8/10 | 已经承认未验证、删除伪精确 |
| 可持续执行 | 7/10 | lean checklist 可执行，但仍需坚持填写 |
| 早期发现能力 | 4/10 | 过度依赖事件确认 |
| 估值/赔率纪律 | 5/10 | 有意识，但未形成硬字段 |
| 回测证明力 | 3/10 | 样本极少，无法证明 edge |
| 公司 alpha 识别 | 4/10 | 尚未充分剥离主题 beta |
| 防叙事漂移 | 3/10 | 目前缺少 thesis drift 标记 |
| 风险控制 | 6/10 | 相关性意识有，但仓位规则还需组合化 |

总体：v3.3 是一个合格的研究卫生系统，不是合格的高胜率投资模型。

## 4. 下一轮模型优化方向

### 4.1 增加 pre-confirmation watchlist

新增文件建议：

- `pre_confirmation_signal_log_v1.csv`

字段：

- ticker
- theme
- signal_date
- signal_type
- signal_source_quality
- signal_description
- why_it_might_matter
- what_would_confirm
- what_would_kill
- current_market_awareness
- action_allowed

规则：

- pre-confirmation 信号只能允许 `watch` 或极小 tracking position。
- 不能因为 C/D 级信息加仓。
- 只有 A/B 级信息升级后才进入事件账本。

### 4.2 扩展 prospective_event_ledger

当前字段不足。下一版应加入：

- valuation_state
- price_reaction_risk
- theme_basket_return
- alpha_vs_theme
- information_quality
- original_thesis
- thesis_drift_flag
- no_trade_reason

### 4.3 建立 no-trade checklist

新增文件建议：

- `no_trade_checklist_v1.csv`

目标不是找到更多交易，而是减少坏交易。

### 4.4 把“模型有效性”拆成三层

不要再问“模型准不准”这种大问题。拆成：

1. 方向识别是否有效：主题是否跑赢 QQQ/SMH。
2. 公司选择是否有效：个股是否跑赢主题篮子。
3. 执行时点是否有效：事件前后行动是否改善收益/回撤。

只有三层都通过，才是投资模型 edge。

## 5. 现在最应该避免什么

1. 不要因为 v3.3 更干净，就以为它已经有效。
2. 不要继续扩展公司名单来获得“深挖感”。
3. 不要用旧 target price 安慰自己。
4. 不要把主题上涨当成选股正确。
5. 不要把事件后解释当成事件前预测。

## 6. 最终自省

模型真正的问题不是“不够复杂”，而是还没证明自己能在以下三件事上胜出：

- 早于市场发现卡点。
- 区分主题 beta 和公司 alpha。
- 在证据变强但价格过热时克制不买。

v3.3 已经把伪精确降下来了，这是进步。  
下一步必须补“早期信号、估值赔率、主题 beta 剥离、叙事漂移”四件事。

如果这些补不上，它就只能是研究笔记，不是决策模型。
