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

cd "$ROOT_DIR"

mkdir -p "$DEPS_DIR"

"$PYTHON_BIN" -m pip install --upgrade --target "$DEPS_DIR" -r "$ROOT_DIR/requirements-analysis.txt"

PYTHONPATH="$DEPS_DIR${PYTHONPATH:+:$PYTHONPATH}" "$PYTHON_BIN" - <<'PY'
import matplotlib
import pandas
import numpy

print("analysis env OK")
print("numpy", numpy.__version__)
print("pandas", pandas.__version__)
print("matplotlib", matplotlib.__version__)
PY
