# AI 供应链实时信息报告

日期：2026-05-25  
性质：实时信息层，不替代 v3.4 决策系统。  
说明：这是研究框架，不是个人投资建议。

## 0. 信息状态

2026-05-25 是美国 Memorial Day，NYSE/Nasdaq 休市；本报告里的股价只能视为最新可得交易日快照，不是盘中实时成交。

使用方式：

1. 先看“实时事实是否改变 thesis”。
2. 再看“估值和拥挤度是否允许交易”。
3. 最后才决定是否进入 `prospective_event_ledger_v2.csv`。

## 1. 最新可得行情快照

| Ticker | 最新可得价 | 市值 | 当前状态 |
|---|---:|---:|---|
| SMTC | $156.78 | $13.75B | 5/26 AH 财报前，高预期，高波动 |
| MOD | $260.52 | $13.76B | 5/26 AH 出 Q4，5/27 call，高预期 |
| POWL | $279.22 | $10.21B | 订单强，但估值已反映大量乐观 |
| FORM | $128.99 | $10.24B | HBM/probe 兑现度提高，但估值紧 |
| VECO | $59.55 | $3.60B | InP 激光设备订单强验证 |
| POET | $14.59 | $0.89B | 商业验证增强，但仍是里程碑期权 |
| AXTI | $140.83 | $7.51B | InP 需求被市场剧烈重估，执行前必须二次确认报价 |
| PPSI | $5.21 | $57.8M | 小订单验证，现金和规模仍约束 |

注：行情数据来自最新可得市场快照；由于今日美股休市，执行前必须用券商端重新确认价格、成交量和盘前盘后流动性。

## 2. 实时事实更新

### 2.1 光通信主线：仍在升温，但个股分化更大

SMTC 是 5/26 的核心事件。Semtech 在 FY2026 Q4 给出的 Q1 FY2027 outlook 是：net sales $283M +/- $5M，adjusted gross margin 52.8% +/- 50bps，adjusted EPS $0.45 +/- $0.03。公司计划在 2026-05-26 收盘后发布 Q1 FY2027 结果。

判断：

- 财报前不追，因为股价和预期已经很高。
- 财报后重点看 Signal Integrity、800G/1.6T/3.2T、guide、margin 和 FCF。
- 不能只因为股价涨就证明模型有效；必须拆出 optical theme beta 和 SMTC company alpha。

### 2.2 POET：从“纯样品期权”升级为“有订单/资金验证的里程碑期权”

POET Q1 2026 披露 Lumilens 对 EOI-based optical engines 的初始 purchase order 为 $50M，同时公司宣布与 Lumilens、Lessengers、LITEON 等生态伙伴推进 AI optical roadmap。随后 POET 宣布完成 US$400M 融资，并称将把 wafer production 和 optical engine assembly 产能扩大约 10 倍，以支持 2027 年更高量制造。

判断：

- 这不是普通 PR，信息质量从 B/C 提升到 A/B。
- 但仍不能做 DCF，因为关键仍是样品、qualification、production ramp、重复订单和真实毛利。
- 模型处理：进入 `pre_confirmation_signal_log_v1.csv` 的高级观察位；只有出现生产交付、客户复购或收入确认，才升级为事件账本核心。
- 风险：融资摊薄、warrant overhang、2027 才放量、客户资格认证失败。

### 2.3 VECO/AXTI：InP 激光链条成为更明确的上游卡点

VECO 宣布获得 $250M+ InP laser manufacturing equipment orders，交付从 2026 年开始并在 2027 年显著加速；订单涉及 800G/1.6T hyperscale data-center optical transceiver 相关制造。AXTI Q1 2026 披露 revenue $26.9M，GAAP gross margin 29.6%，并明确把 InP substrates 与 AI-focused data-center high-speed optical transmission 连接起来，同时提到 $632.5M capital raise 支持 Tongmei InP capacity expansion。

判断：

- 这加强“光通信卡点向 InP 激光/材料/设备上游迁移”的判断。
- VECO 比 POET 更接近可建模，因为订单和交付节奏更清楚。
- AXTI 是更高 beta 的材料端票，股价已经被剧烈重估，不能用旧价格思维处理。
- 模型处理：VECO 可进入事件账本候选；AXTI 保持高波动 watch，等待报价/成交量/融资和 Tongmei 进展二次确认。

### 2.4 电力/散热：POWL 和 MOD 继续验证，但不等于可以追

POWL Q2 FY2026 披露 revenue $297M、gross profit margin 29.6%、new orders $490M、backlog $1.8B，并在季度后获得超过 $400M 的 mega data-center order。MOD Q3 FY2026 披露 data-center sales +78% YoY，并把未来两年 data-center sales growth outlook 提到 50%-70%；但 MOD Q4/FY2026 结果要等 2026-05-26 收盘后发布，5/27 开 call。

判断：

- 电力/散热 backlog 拉长这个方向仍强。
- POWL 事实强，但股价和估值也已经强，核心风险从“有没有需求”转成“订单能否按毛利和现金流兑现”。
- MOD 要等 5/26 Q4/FY2026，尤其看 data-center segment、新产线成本、FCF 和 FY2027 outlook。
- 模型处理：不做财报前追价；财报后用 v3.4 的 no-trade checklist 和 theme alpha 拆解。

### 2.5 AP/HBM：FORM 明显兑现，但估值赔率要单独看

FORM Q1 2026 披露 revenue $226.1M，同比 +32.0%，创纪录；公司称 DRAM revenue 创纪录并由 HBM applications 需求增加驱动，non-GAAP gross margin 49.0%，FCF $30.7M，Q2 outlook revenue $240M +/- $5M，non-GAAP gross margin 49.5% +/- 1.5%。

判断：

- HBM/probe 不是纯想象，FORM 已经有财务兑现。
- 但 FORM 当前不是“冷门未发现票”，更像高质量高预期票。
- 模型处理：从 early signal 升级到 AP/HBM active watch；是否买取决于回撤、估值和与 ONTO/CAMT 的相关性。

### 2.6 PPSI：有真实订单，但仍是微型公司执行风险

PPSI Q1 2026 披露 PRYMUS 获得 $6M order，delivery expected in 2026H2；backlog $13.9M，cash $13.6M，revenue $4.3M，gross margin 13.6%，仍有 operating loss。

判断：

- PRYMUS 不是完全空故事，已有订单。
- 但规模太小，现金、内控、交付、毛利和客户复购都未证明。
- 模型处理：仍是 cold option，不应因为 AI power narrative 重仓。

## 3. 当前决策结论

| 主题 | 实时方向 | 交易态度 |
|---|---|---|
| 光通信主链 | 强 | 不追高；等 SMTC 财报确认和同赛道 alpha |
| InP/激光上游 | 明显增强 | VECO 优先于更高噪音材料票；AXTI 需确认报价和风险 |
| 电力/散热 | 强 | POWL/MOD 事实强，但估值和财报事件风险高 |
| AP/HBM test | 已兑现 | FORM 可升到 active watch，但不能当冷门低估票 |
| 冷门期权 | 分化 | POET 升级，PPSI 仍小仓观察 |

## 4. 即时行动规则

1. SMTC/MOD 财报前：不加仓，只记录预期。
2. SMTC/MOD 财报后：先判断 beat/raise/thesis evidence/margin/FCF，再判断价格。
3. POET：把 thesis 从“样品验证”更新为“订单+融资+产能扩张验证”，但仍要求 late-2026 samples、2027 production ramp、revenue recognition。
4. VECO：作为 InP 激光设备链条的优先验证对象，等待订单转收入和 margin/FCF。
5. AXTI：短期不按旧估值框架处理，先确认最新报价、换手和 Tongmei/出口/中国集中风险。
6. PPSI：只跟踪订单转收入、backlog 增长、cash runway 和内控修复。

## 5. 主要来源

- NYSE holiday calendar: https://www.nyse.com/markets/hours-calendars
- Nasdaq holiday calendar: https://www.nasdaq.com/holiday-trading-hours
- Semtech FY2026 Q4 results and Q1 FY2027 outlook: https://investors.semtech.com/news/semtech-announces-fourth-quarter-and-fiscal-year-2026-results/21cc5cf3-f51f-4f27-88d7-4023516e7840
- Semtech Q1 FY2027 conference call notice: https://www.semtech.com/company/press/semtech-announces-first-quarter-of-fiscal-year-2027-conference-call
- Modine Q4 FY2026 call notice: https://investors.modine.com/news/news-details/2026/Modine-to-Host-Fourth-Quarter-Fiscal-2026-Earnings-Conference-Call-on-May-27-2026/default.aspx
- Modine Q3 FY2026 results: https://investors.modine.com/news/news-details/2026/Modine-Reports-Third-Quarter-Fiscal-2026-Results/default.aspx
- Powell Q2 FY2026 results: https://powellindustriesinc.gcs-web.com/news-releases/news-release-details/powell-industries-announces-second-quarter-fiscal-2026-results
- POET Q1 2026 results: https://www.poet-technologies.com/news/poet-technologies-reports-first-quarter-2026-financial-results
- POET US$400M investment closing: https://www.poet-technologies.com/news/poet-technologies-announces-closing-of-us400-million-investment
- POET/Lumilens partnership: https://www.poet-technologies.com/news/poet-technologies-and-lumilens-advance-wafer-level-photonic-integration-for-next-generation-ai-optical-networks
- VECO $250M+ InP equipment orders: https://ir.veeco.com/news-and-events/news-details/2026/Veeco-Announces-250-Million-in-Equipment-Orders-for-Manufacturing-Indium-Phosphide-Lasers/default.aspx
- AXTI Q1 2026 results: https://www.sec.gov/Archives/edgar/data/1051627/000143774926014204/ex_906119.htm
- FORM Q1 2026 results: https://investors.formfactor.com/news-releases/news-release-details/formfactor-inc-reports-2026-first-quarter-results/
- FORM Altius HBM product page: https://www.formfactor.com/product/probe-cards/foundry-logic/altius/
- PPSI Q1 2026 results: https://www.pioneerpowersolutions.com/286-pioneer-power-announces-financial-results-for-first-quarter-2026-and-business-updates/
