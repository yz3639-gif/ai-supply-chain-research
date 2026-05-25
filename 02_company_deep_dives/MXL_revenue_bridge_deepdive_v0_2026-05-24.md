# MXL Revenue Bridge Deep Dive v0

日期：2026-05-24  
目的：判断 `MXL` 是否还能作为 AI 互连轮动票，而不是已经完全透支。

## 1. 结论

`MXL` 不是“还没被发现”的票。它已经被市场重新定价。现在只有一个核心问题：

**2026 optical data center revenue 能不能从 $150M-$170M 继续上修到 $200M+，并且 Rushmore 1.6T / Annapurna 224G 在 2027 进入量产。**

如果答案是能，`MXL` 仍有 bull case；如果只是兑现当前 $150M-$170M 指引，当前估值已经不便宜。

## 2. 官方证据

MaxLinear Q1 2026：

- Q1 revenue $137.2M，同比 +43%。
- Infrastructure business 同比 +136%，成为最大终端市场。
- Q2 2026 revenue guide $160M-$170M。
- 管理层称 Q1 是 optical data center connectivity 多年增长阶段的开始，且 Q2 会有 step-function increase。
- 来源：[MXL Q1 2026](https://investors.maxlinear.com/press-releases/detail/607/maxlinear-inc-announces-first-quarter-2026-financial)

10-Q 里公司披露 Q1 revenue 来自包括 high-speed optical interconnect solutions sold into optical modules for data-center, metro and long-haul networks。10-Q 还提到 operating cash flow 受 wafer prepayment 影响，该预付款用于支持某些 data center products 的 rising demand。来源：[MXL Q1 2026 10-Q](https://investors.maxlinear.com/all-sec-filings/content/0001288469-26-000029/mxl-20260331.htm)

产品线：

- Keystone：400G/800G DSP。
- Rushmore：1.6T PAM4 DSP。
- Annapurna：224G scale-up retimer，最高 1.6Tbps electrical connectivity，支持 ESUN、UALink、Ultra Ethernet 等 emerging scale-up protocols。
- Washington：200G TIA。
- 来源：[Annapurna](https://www.maxlinear.com/news/press-releases/2026/maxlinear-unveils-annapurna-224g-scale-up-retimer-to-extend-copper-connectivity-in-ai-data-centers)

## 3. 收入桥

| 项目 | Bear | Base | Bull |
|---|---:|---:|---:|
| 2026 company revenue | $550M | $700M | $925M |
| Optical data center revenue | <$150M | $150M-$170M | $200M+ |
| Keystone 800G | ramp but limited | meaningful ramp | multiple hyperscaler/platform ramps |
| Rushmore 1.6T | sampling only | late 2026 production bridge | 2027 volume ramp visibility |
| Annapurna 224G | engagement only | design wins | production sockets in scale-up fabrics |
| Valuation multiple | 6x sales | 11.5x sales | 15x sales |
| Implied market cap | $3.3B | $8.05B | $13.875B |
| vs current market cap | -63% | -9% | +56% |

## 4. 关键判断

Base case 不够。当前市值已经把 optical data center ramp 计入一部分。`MXL` 的仓位逻辑必须建立在两个触发之一：

1. 2026 optical data center revenue 从 $150M-$170M 上修到 $200M+。
2. Rushmore / Annapurna 从 sampling 和 engagement 进入明确 production socket。

## 5. 财务排雷

Q1 working capital 初看没有 AR 雷：

- Q1 accounts receivable / quarterly revenue = 0.30x。
- DSO 约 26.8 天。

但库存和 wafer prepayment 要盯：

- Inventory / quarterly COGS = 1.47x。
- DIO 约 132.5 天。
- 10-Q 说明 operating cash flow 受 wafer prepayment 影响，用于 data center product demand。

解释：这可以是 ramp 前备货的正信号，也可以变成需求不及预期时的库存风险。下一季要看 Q2 revenue 是否真正跳升。

## 6. 客户链风险

公开语言仍是 multiple hyperscale customers / Tier-1 OEM / customer engagement，没有点名客户。替代者包括 Broadcom、Marvell、Credo、Semtech、MACOM 和客户自研。

这意味着 `MXL` 不能按独供估值，只能按“设计赢单扩大概率”估值。

## 7. 仓位规则

**观察仓/事件仓可以**：如果回撤但 Q2/Q3 guidance 不坏。  
**加仓条件**：optical DC revenue guide 上修，或 Rushmore/Annapurna 量产客户明确。  
**止错条件**：optical revenue 不达 $150M，或旧业务拖累整体收入，或库存继续升但 revenue 没跟。

