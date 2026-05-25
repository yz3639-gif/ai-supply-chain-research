#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PID_FILE="$ROOT_DIR/realtime_data_pipeline/data/processed/pipeline.pid"
LOG_FILE="$ROOT_DIR/realtime_data_pipeline/data/processed/pipeline.log"

mkdir -p "$(dirname "$PID_FILE")"

if [[ -f "$PID_FILE" ]]; then
  OLD_PID="$(cat "$PID_FILE")"
  if [[ -n "$OLD_PID" ]] && kill -0 "$OLD_PID" 2>/dev/null; then
    echo "Pipeline already running with PID $OLD_PID"
    exit 0
  fi
fi

nohup python3 "$ROOT_DIR/realtime_data_pipeline/run_pipeline.py" --loop-seconds 60 >>"$LOG_FILE" 2>&1 &
PID="$!"
echo "$PID" >"$PID_FILE"
echo "Started realtime pipeline with PID $PID"
echo "Log: $LOG_FILE"

