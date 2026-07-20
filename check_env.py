import importlib.util as u

mods = ["fastapi", "uvicorn", "typer", "rich", "pydantic", "click", "httpx", "sse_starlette"]
for m in mods:
    print(f"{m}: {'OK' if u.find_spec(m) else 'MISSING'}")

import sys
print("python:", sys.executable, sys.version.split()[0])
