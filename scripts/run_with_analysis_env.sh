#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
DEPS_DIR="$ROOT_DIR/.analysis_deps"
BUNDLED_PYTHON="/Users/yuangzuo/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3"

if [[ -n "${ANALYSIS_PYTHON:-}" ]]; then
  PYTHON_BIN="$ANALYSIS_PYTHON"
elif [[ -x "$BUNDLED_PYTHON" ]]; then
  PYTHON_BIN="$BUNDLED_PYTHON"
else
  PYTHON_BIN="python3"
fi

if [[ ! -d "$DEPS_DIR" ]]; then
  echo "Missing .analysis_deps. Run ./scripts/setup_analysis_env.sh first." >&2
  exit 1
fi

PYTHONPATH="$DEPS_DIR${PYTHONPATH:+:$PYTHONPATH}" "$PYTHON_BIN" "$@"
