#!/bin/bash

# Clipboard MCP Server Setup Script
echo "🖥️  Setting up Clipboard MCP Server..."

# Check if Python is available
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is required but not installed."
    exit 1
fi

# Install xclip if not available (Linux only)
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    if ! command -v xclip &> /dev/null; then
        echo "📋 Installing clipboard support (xclip)..."
        if command -v apt-get &> /dev/null; then
            sudo apt-get update && sudo apt-get install -y xclip
        elif command -v yum &> /dev/null; then
            sudo yum install -y xclip
        elif command -v dnf &> /dev/null; then
            sudo dnf install -y xclip
        elif command -v pacman &> /dev/null; then
            sudo pacman -S xclip
        else
            echo "⚠️  Please install xclip manually for your Linux distribution"
        fi
    fi
fi

# Create virtual environment if it doesn't exist
if [ ! -d ".venv" ]; then
    echo "🐍 Creating Python virtual environment..."
    python3 -m venv .venv
fi

# Activate virtual environment and install dependencies
echo "📦 Installing Python dependencies..."
source .venv/bin/activate
pip install -r requirements.txt

echo "✅ Setup complete!"
echo ""
echo "To start the clipboard server:"
echo "  ./start.sh"
echo ""
echo "MCP Client Configuration:"
echo "Add this to your MCP client config:"
echo '{'
echo '  "mcpServers": {'
echo '    "clipboard": {'
echo '      "type": "sse",'
echo '      "url": "http://localhost:3001/sse"'
echo '    }'
echo '  }'
echo '}'
echo ""
echo "Supported clients: Claude Code, LM Studio, and other MCP-compatible tools"