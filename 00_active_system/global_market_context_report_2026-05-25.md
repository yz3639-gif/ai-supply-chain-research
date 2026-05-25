# 全球市场上下文报告

日期：2026-05-25  
数据抓取时间：约 2026-05-25 05:30 UTC  
用途：把非美市场、FX、商品、加密和期货纳入 AI 供应链 v3.4 决策系统。  
说明：这是研究框架，不是个人投资建议。

## 1. 核心结论

今天美国 Memorial Day 休市，因此其他市场的价值是给明天美股恢复交易前提供外部温度计，而不是直接触发交易。

最强信号：

1. 日本半导体设备和测试链出现强烈新鲜确认。
2. 日本光纤/线缆链出现更强的新鲜确认。
3. 台湾 AI 硬件链明显走强，尤其是 Lite-On。
4. 韩国和欧洲目前是上一交易日数据，不作为今天新鲜确认。
5. 宏观风险温度偏中性：Nasdaq 100 futures 近似持平，BTC 小涨，黄金微涨，WTI 对前收持平但日内从开盘走高。

模型含义：  
这强化了 `AP_HBM_test`、`semi_equipment`、`advanced_packaging`、`optical_cable`、`power_optical_components` 这几条外部确认线，但不改变 v3.4 的交易纪律。若美股明天相关股票大幅高开，仍要先触发 `no_trade_checklist_v1.csv` 的估值/追高检查。

## 2. 主题聚合

| 主题组 | 新鲜度 | 平均前收涨跌 | 平均相对开盘 | 解读 |
|---|---:|---:|---:|---|
| Japan_optical_cable | 2/2 | +9.10% | +2.18% | 强外部确认 |
| Japan_semi_equipment | 3/3 | +7.71% | +4.49% | 强外部确认 |
| Taiwan_AI_hardware | 2/2 | +5.95% | +4.21% | 强外部确认 |
| Japan_semi_test | 1/1 | +4.32% | +2.79% | 强外部确认 |
| Taiwan_AI_server | 2/2 | +2.59% | +0.25% | 正向确认，但强度低于设备/线缆 |
| Taiwan_ASIC | 1/1 | +0.10% | -2.39% | 混合，不确认追高 |
| Macro_risk | 3/3 | +0.29% | -0.06% | 中性 |
| Macro_fx | 2/2 | +0.06% | +0.15% | 中性 |
| Macro_cost | 1/1 | 0.00% | +2.90% | 能源成本需观察 |
| Korea_memory_HBM | 0/2 | -1.14% | -1.28% | 非今日信号 |
| Korea_HBM_equipment | 0/1 | -3.61% | -1.84% | 非今日信号 |
| Europe_semi_equipment | 0/1 | +4.74% | +2.47% | 上一交易日正向，非今日信号 |
| Europe_power_semis | 0/2 | +6.57% | +3.31% | 上一交易日正向，非今日信号 |
| Europe_AP_equipment | 0/1 | +1.18% | -0.51% | 上一交易日混合 |

## 3. 关键个股/资产

| 名称 | 市场 | 日期 | 价格 | 较前收 | 相对开盘 | 新鲜度 |
|---|---|---:|---:|---:|---:|---|
| Fujikura | Japan | 2026-05-25 | 5550.0 | +14.43% | +3.54% | fresh |
| Lasertec | Japan | 2026-05-25 | 42720.0 | +12.04% | +6.01% | fresh |
| Lite-On | Taiwan | 2026-05-25 | 227.5 | +9.90% | +7.31% | fresh |
| Disco | Japan | 2026-05-25 | 69830.0 | +6.03% | +3.85% | fresh |
| Tokyo Electron | Japan | 2026-05-25 | 52360.0 | +5.08% | +3.62% | fresh |
| Advantest | Japan | 2026-05-25 | 28005.0 | +4.32% | +2.79% | fresh |
| Sumitomo Electric | Japan | 2026-05-25 | 12265.0 | +3.76% | +0.82% | fresh |
| Taiwan Weighted | Taiwan | 2026-05-25 | 43630.91 | +3.22% | +2.26% | fresh |
| Wistron | Taiwan | 2026-05-25 | 149.0 | +3.11% | +0.34% | fresh |
| Nikkei 225 | Japan | 2026-05-25 | 65324.67 | +3.13% | +2.62% | fresh |
| Quanta | Taiwan | 2026-05-25 | 322.5 | +2.06% | +0.16% | fresh |
| TSMC | Taiwan | 2026-05-25 | 2300.0 | +2.00% | +1.10% | fresh |
| BTC-USD | Crypto | 2026-05-25 | 77295.90 | +0.81% | +0.42% | fresh |
| Nasdaq 100 Futures | US futures | 2026-05-25 | 29558.75 | 0.00% | -0.40% | fresh |

## 4. 对 AI 供应链模型的影响

### 4.1 外部确认提高的方向

`Japan_semi_equipment` 和 `Japan_semi_test` 强，说明市场继续愿意给先进制程、测试、先进封装链条更高权重。  
映射到美股/研究名单：`FORM`、`ONTO`、`CAMT`、`COHU`、`VECO` 的主题背景改善，但仍需公司级事件确认。

`Japan_optical_cable` 强，尤其 Fujikura 大涨，说明光通信链条中“线缆/连接/材料”继续被重估。  
映射到美股/研究名单：`SMTC`、`MTSI`、`MXL`、`VECO`、`POET` 的主题背景改善，但不能替代订单、guide 和 margin 证据。

`Taiwan_AI_hardware` 强，尤其 Lite-On，说明电源/光电/组件层开始更活跃。  
映射到美股/研究名单：`POWL`、`MOD`、`PPSI` 的外部需求背景改善，但电力/散热仍要看 backlog、交付和 FCF。

### 4.2 不能使用的“假确认”

韩国 HBM 链和欧洲半导体设备链今天没有 fresh signal。  
虽然欧洲上一交易日 ASML、Infineon、STM 偏强，但因为日期是 2026-05-22，不应该把它写成 2026-05-25 的新确认。

### 4.3 风险纪律

如果明天美股相关股票因为亚洲信号而高开，模型不应自动追。  
需要先检查：

- 是否高于 EMA20/50/200 太多。
- 是否接近或突破 BOLL 上轨。
- 是否已有 A/B 级公司事件确认。
- 是否触发 `NT01 valuation/price extension`。
- 同一风险簇是否超过组合上限。

## 5. 数据入口

机器可读数据：

- `realtime_data_pipeline/data/processed/global_market_context_latest.csv`
- `realtime_data_pipeline/data/processed/global_market_theme_summary_latest.csv`
- `realtime_data_pipeline/reports/realtime_snapshot_latest.md`

数据源：

- Yahoo Finance chart API, 5 日/日线数据。
- 本地 pipeline 抓取时间约 2026-05-25 05:30 UTC。

