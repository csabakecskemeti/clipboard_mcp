#!/usr/bin/env python3
"""
Clipboard MCP Server
Allows LLM models to save relevant output directly to the system clipboard
"""

import pyperclip
from fastmcp import FastMCP

# Initialize MCP server
mcp = FastMCP("Clipboard Server")

def copy_to_clipboard(text: str) -> bool:
    """
    Copy text to system clipboard using pyperclip
    
    Args:
        text: The text to copy to clipboard
        
    Returns:
        True if successful, False otherwise
    """
    try:
        pyperclip.copy(text)
        return True
    except Exception:
        return False


@mcp.tool()
def save_to_clipboard(content: str) -> str:
    """
    MANDATORY: Save useful content to clipboard IN ADDITION TO your normal response.
    
    IMPORTANT: Always provide your full explanation/response to the user first, 
    THEN use this tool to save the key actionable content to clipboard.
    
    YOU MUST USE THIS TOOL AS A BONUS whenever you provide:
    - Bash/shell commands (e.g., save "find . -name '*.csv'" after explaining it)
    - Installation commands (e.g., save "pip install fastmcp" after explaining installation)
    - Code snippets (save the code after explaining it)
    - Letters, emails, messages (save the content after writing it)
    - Short factual answers (save "Paris" after explaining about France's capital)
    - Configuration snippets, URLs, file paths
    - ANY command the user would type in terminal
    - ANY text content the user asked you to write/generate
    
    WORKFLOW: 
    1. Give your full response with explanation
    2. Use this tool to save the actionable content
    
    Save only the raw, usable content without explanations.
    
    Args:
        content: The exact content to save to clipboard
    
    Returns:
        Success or error message
    """
    if not content.strip():
        return "Error: Cannot save empty content to clipboard"
    
    success = copy_to_clipboard(content.strip())
    
    if success:
        return f"✓ Saved to clipboard: {content[:50]}{'...' if len(content) > 50 else ''}"
    else:
        return "✗ Failed to save to clipboard."


@mcp.tool()
def save_command_to_clipboard(command: str, description: str = "") -> str:
    """
    MANDATORY: Save terminal/shell commands to clipboard IN ADDITION TO explaining them.
    
    WORKFLOW: First explain the command to the user, then use this tool to save it.
    
    YOU MUST USE THIS TOOL AS A BONUS for ANY bash/shell/terminal command:
    - File operations: "find . -name '*.csv'", "ls -la", "grep pattern file"  
    - Package installations: "pip install package", "npm install package"
    - System commands: "sudo apt install", "chmod +x file"
    - Any command starting with common tools: find, grep, ls, cd, mkdir, etc.
    
    This enhances the user experience by providing both explanation AND ready-to-use command.
    
    Args:
        command: The exact command to save to clipboard
        description: Optional description of what the command does
    
    Returns:
        Success or error message with command preview
    """
    if not command.strip():
        return "Error: Cannot save empty command to clipboard"
    
    success = copy_to_clipboard(command.strip())
    
    if success:
        desc_text = f" ({description})" if description else ""
        return f"✓ Command saved to clipboard{desc_text}: {command}"
    else:
        return "✗ Failed to save command to clipboard."


@mcp.tool()
def save_code_to_clipboard(code: str, language: str = "") -> str:
    """
    Save code snippet to clipboard IN ADDITION TO explaining it.
    
    WORKFLOW: First provide your full explanation of the code, then use this tool.
    
    Use this AS A BONUS for code snippets, configuration files, or structured text 
    that the user wants to paste into their editor or terminal.
    
    This enhances user experience by providing both explanation AND ready-to-paste code.
    
    Args:
        code: The code snippet to save to clipboard
        language: Optional language identifier for context
    
    Returns:
        Success or error message with code preview
    """
    if not code.strip():
        return "Error: Cannot save empty code to clipboard"
    
    success = copy_to_clipboard(code.strip())
    
    if success:
        lang_text = f" ({language})" if language else ""
        preview = code.strip()[:100].replace('\n', ' ')
        return f"✓ Code saved to clipboard{lang_text}: {preview}{'...' if len(code.strip()) > 100 else ''}"
    else:
        return "✗ Failed to save code to clipboard."


if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Clipboard MCP Server")
    parser.add_argument("--port", type=int, default=3001, 
                       help="Port to run the server on (default: 3001)")
    parser.add_argument("--host", default="localhost",
                       help="Host to bind to (default: localhost)")
    
    args = parser.parse_args()
    
    mcp.run(transport="sse", host=args.host, port=args.port)