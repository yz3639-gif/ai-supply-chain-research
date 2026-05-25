from __future__ import annotations

import matplotlib
import numpy
import pandas


def main() -> None:
    print("analysis env OK")
    print(f"numpy {numpy.__version__}")
    print(f"pandas {pandas.__version__}")
    print(f"matplotlib {matplotlib.__version__}")


if __name__ == "__main__":
    main()
