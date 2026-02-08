#!/bin/bash
cd /app/auto-mcp-upload/data/5236
rm -rf .venv
exec uv run python -c "import sys; sys.path.insert(0, '.'); from app.main import mcp; mcp.run()"
