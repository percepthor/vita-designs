#!/usr/bin/env python3
"""
Setup script for ViTA Design System MCP Server

This script helps configure the MCP server for different platforms.
"""

import json
import os
import platform
import subprocess
import sys
from pathlib import Path


def get_claude_config_path():
    """Get the Claude configuration file path for current platform"""
    system = platform.system()
    
    if system == "Darwin":  # macOS
        return Path.home() / "Library" / "Application Support" / "Claude" / "claude_desktop_config.json"
    elif system == "Windows":
        return Path.home() / "AppData" / "Roaming" / "Claude" / "claude_desktop_config.json"
    elif system == "Linux":
        return Path.home() / ".config" / "Claude" / "claude_desktop_config.json"
    else:
        raise OSError(f"Unsupported operating system: {system}")


def install_dependencies():
    """Install required Python dependencies"""
    print("📦 Installing Python dependencies...")
    
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Dependencies installed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to install dependencies: {e}")
        return False


def setup_claude_config():
    """Setup Claude configuration for MCP server"""
    print("⚙️  Configuring Claude Code...")
    
    # Get paths
    config_path = get_claude_config_path()
    server_path = Path(__file__).parent / "server.py"
    vita_path = Path(__file__).parent.parent
    
    # Create config directory if it doesn't exist
    config_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Load existing config or create new one
    if config_path.exists():
        with open(config_path, 'r') as f:
            config = json.load(f)
    else:
        config = {}
    
    # Add MCP server configuration
    if "mcpServers" not in config:
        config["mcpServers"] = {}
    
    config["mcpServers"]["vita-design-system"] = {
        "command": "python3" if platform.system() != "Windows" else "python",
        "args": [str(server_path.absolute())],
        "cwd": str(vita_path.absolute())
    }
    
    # Save configuration
    with open(config_path, 'w') as f:
        json.dump(config, f, indent=2)
    
    print(f"✅ Configuration saved to: {config_path}")
    print("🔄 Please restart Claude Code to apply changes")
    
    return True


def make_executable():
    """Make server.py executable on Unix systems"""
    if platform.system() != "Windows":
        server_path = Path(__file__).parent / "server.py"
        try:
            os.chmod(server_path, 0o755)
            print("✅ Made server.py executable")
        except OSError as e:
            print(f"⚠️  Could not make server.py executable: {e}")


def verify_setup():
    """Verify the setup is correct"""
    print("🔍 Verifying setup...")
    
    # Check Python version
    if sys.version_info < (3, 8):
        print("❌ Python 3.8 or higher is required")
        return False
    
    print(f"✅ Python {sys.version}")
    
    # Check MCP library
    try:
        import mcp
        print("✅ MCP library installed")
    except ImportError:
        print("❌ MCP library not found")
        return False
    
    # Check ViTA files
    vita_path = Path(__file__).parent.parent
    required_files = ["DESIGN_TOKENS.css", "package.json"]
    
    for file_name in required_files:
        file_path = vita_path / file_name
        if file_path.exists():
            print(f"✅ Found {file_name}")
        else:
            print(f"⚠️  Missing {file_name}")
    
    print("✅ Setup verification completed")
    return True


def main():
    """Main setup function"""
    print("🎨 ViTA Design System MCP Server Setup")
    print("=" * 50)
    
    # Install dependencies
    if not install_dependencies():
        print("❌ Setup failed during dependency installation")
        return 1
    
    # Make executable
    make_executable()
    
    # Setup Claude configuration
    if not setup_claude_config():
        print("❌ Setup failed during Claude configuration")
        return 1
    
    # Verify setup
    if not verify_setup():
        print("⚠️  Setup completed with warnings")
    
    print("\n🎉 Setup completed successfully!")
    print("\nNext steps:")
    print("1. Restart Claude Code")
    print("2. Try: '@vita-design-system Show me available color tokens'")
    print("3. Try: '@vita-design-system Generate a primary button'")
    
    return 0


if __name__ == "__main__":
    sys.exit(main())