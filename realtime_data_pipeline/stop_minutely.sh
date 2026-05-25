#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PID_FILE="$ROOT_DIR/realtime_data_pipeline/data/processed/pipeline.pid"

if [[ ! -f "$PID_FILE" ]]; then
  echo "No PID file found"
  exit 0
fi

PID="$(cat "$PID_FILE")"
if [[ -n "$PID" ]] && kill -0 "$PID" 2>/dev/null; then
  kill "$PID"
  echo "Stopped realtime pipeline PID $PID"
else
  echo "Pipeline PID $PID is not running"
fi
rm -f "$PID_FILE"

