# AI 供应链决策手册 v0

日期：2026-05-24  
覆盖：HPS-A.TO、ACMR、MXL、AEHR、COHU、KLIC、NEO.TO  
定位：把研究转成仓位、催化剂和止错框架。不是投资建议。

## 0. 当前结论

现在还没到“重仓决策”精度，但已经可以进入 **观察仓/小仓验证** 阶段。原因是产业方向和订单证据已经足够硬，但客户链、收入桥、估值弹性和财务排雷还没完全打穿。

我把七家公司分成三类：

### A. 可以优先进入观察仓/小仓验证

- `HPS-A.TO`：电力变压器/电力质量，backlog 和 data centre activity 最干净。
- `ACMR`：先进封装湿法/电镀/清洗，关键是非中国 advanced packaging 订单是否重复。
- `COHU`：AI processor + GaN power test，估值比 AEHR 温和。

### B. 高弹性但高波动，适合事件仓

- `MXL`：AI optical/copper interconnect 重新定价已经发生，继续看 revenue guide 上修。
- `AEHR`：订单证据非常硬，但估值容错低。

### C. 中期期权，等更明确催化

- `KLIC`：TCB/HBM 转型要看收入和 backlog。
- `NEO.TO`：欧洲永磁和 Magnequench 要看 2026H2 商业项目。

## 1. 仓位原则

在没完成客户链和情景估值前，不做“信仰仓”。只做三层：

| 仓位类型 | 用途 | 触发 |
|---|---|---|
| 观察仓 | 强迫跟踪，避免只看不动 | 方向硬、订单硬，但估值或客户链未打穿 |
| 事件仓 | 押订单/指引/财报催化 | 明确日期或明确数据节点 |
| 确认仓 | 等收入、毛利、backlog 连续验证 | 至少两次财报或客户链交叉确认 |

当前不建议任何单票进入确认仓。

## 2. 单票决策摘要

### HPS-A.TO

**买入前提**：backlog/book-to-bill 继续强，gross margin 维持约 30%，data center/custom mix 没有恶化。  
**加仓条件**：下一季 backlog 继续显著增长，Mexico capacity 顺利 ramp。  
**止错条件**：连续两季 book-to-bill < 1，或毛利跌破 28% 且不是一次性成本。  
**关键风险**：工业股估值已重定价，铜/钢/关税和产能扩张可能压毛利。

### ACMR

**买入前提**：非中国 advanced packaging 订单继续出现，2026 收入指引 $1.08B-$1.175B 兑现。  
**加仓条件**：global OSAT/panel-level packaging repeat orders + gross margin > 45%。  
**止错条件**：增长主要来自中国成熟制程，非中国订单不重复，或应收/库存明显恶化。  
**关键风险**：Entity List、出口限制、中国客户集中和现金流。

### MXL

**买入前提**：2026 optical data center revenue $150M-$170M 指引可信，Keystone/Rushmore/Annapurna 继续有设计赢单。  
**加仓条件**：optical DC revenue 上修到 $200M+，Rushmore/Annapurna 从 sample 进入 production。  
**止错条件**：optical revenue guide 下修，或旧业务拖累整体增长导致估值失去支撑。  
**关键风险**：Q1 后涨幅巨大，预期可能已经提前透支。

### AEHR

**买入前提**：$92M+ bookings 能转 FY2027 revenue，而不是停留在 headline。  
**加仓条件**：FY2027 revenue guide > $150M，且 silicon photonics repeat orders 出现。  
**止错条件**：大订单交付延迟，或客户集中导致收入确认不及预期。  
**关键风险**：TTM P/S 约 66x，估值容错非常低。

### COHU

**买入前提**：FY26 HPC revenue $80M-$100M 兑现，GaN power test 订单多客户化。  
**加仓条件**：HPC revenue outlook 上修，operating margin 转正。  
**止错条件**：AI orders 占比仍小，传统半导体测试周期继续拖累。  
**关键风险**：AI 纯度不够，但这也是它估值没那么贵的原因。

### KLIC

**买入前提**：TCB revenue/backlog 更清楚，Q3/Q4 guide 保持强。  
**加仓条件**：TCB annualized demand 接近 $400M capacity 目标，且 HBM customer repeat。  
**止错条件**：TCB 只是短期热度，老 wirebond 业务拖累整体增长。  
**关键风险**：转型叙事兑现慢。

### NEO.TO

**买入前提**：2026 EBITDA guide $100M-$110M 兑现，Magnequench 持续增长。  
**加仓条件**：欧洲 Permanent Magnet facility 2026H2 商业项目启动，Dy/Tb 分离线稳定。  
**止错条件**：盈利主要来自 hafnium/gallium 价格周期，磁体项目延期。  
**关键风险**：材料周期、债务、流动性和非纯机器人暴露。

## 3. 情景估值方法

现在不做伪精确目标价，只用区间：

- **Bear**：订单不连续/收入不兑现，回到普通工业或设备周期估值。
- **Base**：公司指引兑现，收入和毛利按现有证据增长。
- **Bull**：关键卡点被市场重新定义，倍数扩张 + 收入上修。

详表见：[decision_model_top7_2026-05-24.csv](/Users/yuangzuo/Documents/New%20project/research_ai_supply_chain/decision_model_top7_2026-05-24.csv)

## 4. 现在最重要的下一步

为了把准确度从 35%-45% 提到 60%+，必须做四件事：

1. **客户链交叉验证**：谁供给谁，是否独供，替代品是谁。
2. **收入桥**：订单 -> backlog -> revenue -> gross margin -> EPS。
3. **财务排雷**：应收、库存、现金流、债务、股本稀释。
4. **事件跟踪**：财报日、订单交付、样品验证、量产节点。

## 5. 当前最高优先任务

1. `MXL` 单独收入桥：$150M-$170M optical DC revenue 如何变成 2027 收入和估值。
2. `HPS-A.TO` backlog 深挖：data center/custom mix 到底有多纯。
3. `ACMR` 非中国客户链：global OSAT/panel-level orders 是否可持续。
4. `AEHR` bookings 转 revenue：$92M+ 订单的确认节奏。
5. `COHU` AI/HPC revenue：$80M-$100M FY26 outlook 的质量。

