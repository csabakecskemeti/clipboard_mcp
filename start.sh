#!/bin/bash

# Default port
PORT=${1:-3001}

echo "🚀 Starting Clipboard MCP Server on port $PORT..."
source .venv/bin/activate
python server.py --port $PORT