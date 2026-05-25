#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PID_FILE="$ROOT_DIR/realtime_data_pipeline/data/processed/pipeline.pid"
LOG_FILE="$ROOT_DIR/realtime_data_pipeline/data/processed/pipeline.log"
LATEST_REPORT="$ROOT_DIR/realtime_data_pipeline/reports/realtime_snapshot_latest.md"

if [[ -f "$PID_FILE" ]]; then
  PID="$(cat "$PID_FILE")"
  if [[ -n "$PID" ]] && kill -0 "$PID" 2>/dev/null; then
    echo "running PID=$PID"
  else
    echo "stale PID=$PID"
  fi
else
  echo "not running"
fi

[[ -f "$LATEST_REPORT" ]] && echo "latest_report=$LATEST_REPORT"
[[ -f "$LOG_FILE" ]] && tail -n 8 "$LOG_FILE"

