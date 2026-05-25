# Realtime Data Pipeline

用途：每分钟抓取公开信息，把事件信号写入 AI 供应链 v3.4 决策系统的数据层。  
说明：只抓公开数据；不能获取未公开订单、内部交期或付费终端数据。

## 运行一次

```bash
python3 realtime_data_pipeline/run_pipeline.py
```

## 每分钟持续运行

```bash
./realtime_data_pipeline/start_minutely.sh
```

停止：

```bash
./realtime_data_pipeline/stop_minutely.sh
```

状态：

```bash
./realtime_data_pipeline/status_minutely.sh
```

## 输出位置

这些输出默认被 `.gitignore` 忽略，避免每分钟污染 Git 历史。

| 文件 | 用途 |
|---|---|
| `data/processed/model_ingest_latest.csv` | 模型每分钟读取的最新事件输入 |
| `data/processed/events_history.csv` | 去重后的事件历史 |
| `data/processed/prices_latest.csv` | 最新可得日线价格 |
| `data/processed/sec_filings_latest.csv` | SEC 最近 filings |
| `reports/realtime_snapshot_latest.md` | 最新实时快照 |
| `data/processed/pipeline.log` | 后台运行日志 |

## 决策规则

- A 级来源里的订单、backlog、guide、margin、cash 信号进入 `event_ledger_review_after_no_trade_check`。
- A/B 级但未完全确认的产品、产能、样品、融资信号进入 `pre_confirmation_signal_log`。
- C/D 级或抓取失败只进入 `research_only`。
- 抓到信号不等于买入；必须先通过 `no_trade_checklist_v1.csv`。

