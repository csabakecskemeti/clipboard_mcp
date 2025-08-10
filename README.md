# Clipboard MCP Server

An MCP server that allows LLM models to save relevant output directly to your system clipboard for immediate use.

## Note 
Tested on Linux only 

## What it does

This MCP server provides tools that allow Claude Code (or other MCP-compatible tools) to:
- Save command snippets directly to your clipboard (e.g., `npm install express`)
- Save code snippets ready to paste into your editor
- Save short answers like city names, numbers, or specific values
- Save any text content for immediate use

## Example Usage

When you ask: "How do I install Express.js?"
- Claude gives you a full explanation about Express.js
- **AND** automatically puts `npm install express` on your clipboard ready to paste

When you ask: "What's the capital of Hungary?"
- Claude explains about Budapest being the capital
- **AND** puts just `Budapest` on your clipboard for quick use

## Demo

![Clipboard MCP in Action](clipboard_mcp.gif)

*The clipboard MCP server working with LM Studio - automatically saving useful content to clipboard while providing full responses*

## Quick Start

### Automatic Setup (Recommended)
```bash
./setup.sh
```
This will:
- Install system dependencies (xclip on Linux)
- Create Python virtual environment
- Install all required packages
- Show you the configuration to add to your MCP client

### Manual Setup
1. Install dependencies:
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

2. Install clipboard support (Linux only):
```bash
sudo apt install xclip
```

## Running the Server

### Easy Start
```bash
./start.sh           # Default port 3001
./start.sh 3002      # Custom port 3002
```

### Manual Start
```bash
source .venv/bin/activate
python server.py                # Default port 3001
python server.py --port 3002    # Custom port 3002
python server.py --help         # See all options
```

The server will run on `http://localhost:PORT/sse` and provide clipboard functionality.

## MCP Client Configuration

Add this configuration to your MCP client:

**Claude Code (`~/.claude.json`):**
```json
{
  "mcpServers": {
    "clipboard": {
      "type": "sse",
      "url": "http://localhost:3001/sse"
    }
  }
}
```

**For custom ports**, update the URL accordingly:
```json
{
  "mcpServers": {
    "clipboard": {
      "type": "sse",
      "url": "http://localhost:3002/sse"
    }
  }
}
```

**LM Studio** and other MCP clients use the same configuration format.

The server works with any MCP-compatible client that supports SSE transport.

## Available Tools

### `save_to_clipboard(content: str)`
General-purpose clipboard saving for any text content.

### `save_command_to_clipboard(command: str, description: str = "")`
Specifically for terminal/shell commands with optional description.

### `save_code_to_clipboard(code: str, language: str = "")`
For code snippets with optional language context.

## Testing

Run the server directly to test:
```bash
python server.py
```

The server will start and wait for MCP protocol messages. Use with Claude Code or other MCP clients to test the clipboard functionality.