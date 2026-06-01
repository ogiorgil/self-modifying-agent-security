import sys
from pathlib import Path


# Make project root (py-graph-algorithms/) importable for flat-module layout.
PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

