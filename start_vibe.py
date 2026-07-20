"""Detached launcher for Vibe-Trading: loads ~/.vibe-trading/.env then
starts the FastAPI backend on :8899 plus the Vite dev server on :5899.

Run with the project venv python. Clears PYTHONPATH so Hermes' own
`cli` package is NOT imported over the project one.
"""
from __future__ import annotations

import os
import sys
from pathlib import Path

# --- isolate from Hermes' own `cli` package ---
os.environ.pop("PYTHONPATH", None)

HERE = Path(__file__).resolve().parent
AGENT_DIR = HERE / "agent"
REPO_ROOT = HERE

# --- load provider env (LLM keys etc.) ---
from dotenv import load_dotenv

env_path = Path.home() / ".vibe-trading" / ".env"
if env_path.exists():
    load_dotenv(env_path)
    print(f"[launcher] loaded env from {env_path}", flush=True)
else:
    print(f"[launcher][warn] no .env at {env_path}", flush=True)

# --- make `cli` importable from the agent package ---
if str(AGENT_DIR) not in sys.path:
    sys.path.insert(0, str(AGENT_DIR))

from cli._legacy import serve_main  # noqa: E402

if __name__ == "__main__":
    # serve_main expects argv WITHOUT the "serve" subcommand itself
    sys.exit(
        serve_main(
            ["--host", "127.0.0.1", "--port", "8899", "--dev"]
        )
    )
