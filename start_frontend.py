"""Detached launcher for the Vibe-Trading Vite dev frontend only.

Reuses the already-running backend on :8899 (vite.config.ts proxies
/sessions, /runs, /swarm/*, /settings/*, /live, etc. to
http://127.0.0.1:8899, so no backend restart is needed).

Runs `npm run dev` with the system Node on PATH, binding :5899
(per vite.config.ts `port: 5899`).
"""
from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
FRONTEND = HERE / "frontend"

NODE_BIN = r"C:\Program Files\nodejs"
env = os.environ.copy()
env["PATH"] = NODE_BIN + os.pathsep + env.get("PATH", "")

if __name__ == "__main__":
    proc = subprocess.Popen(
        [
            "cmd", "/c",
            "npm", "run", "dev", "--",
            "--host", "127.0.0.1", "--port", "5899",
        ],
        cwd=str(FRONTEND),
        env=env,
    )
    print(f"[frontend] vite PID={proc.pid} on :5899 -> API :8899", flush=True)
    proc.wait()
