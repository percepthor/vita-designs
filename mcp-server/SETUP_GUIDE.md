# ViTA Design System MCP Server - Setup Guide

## 🚀 Quick Setup (Recommended)

### Automatic Setup

Run the automated setup script:

```bash
cd /path/to/vita-design/mcp-server
python3 setup.py
```

This will:
- Install all dependencies
- Configure Claude Code automatically
- Verify the setup
- Provide next steps

### Manual Setup

If the automatic setup doesn't work, follow the manual steps below.

---

## 📋 Platform-Specific Setup

### 🍎 macOS Setup

#### 1. Install Dependencies
```bash
cd /path/to/vita-design/mcp-server
pip3 install -r requirements.txt
```

#### 2. Make Server Executable
```bash
chmod +x server.py
```

#### 3. Configure Claude Code
```bash
# Open configuration file
open ~/Library/Application\ Support/Claude/claude_desktop_config.json
```

Add this configuration (replace `/full/path/to/` with your actual path):
```json
{
  "mcpServers": {
    "vita-design-system": {
      "command": "python3",
      "args": ["/full/path/to/vita-design/mcp-server/server.py"],
      "cwd": "/full/path/to/vita-design"
    }
  }
}
```

#### 4. Restart Claude Code
Close and reopen Claude Code application.

---

### 🐧 Linux Setup

#### 1. Install Dependencies
```bash
cd /path/to/vita-design/mcp-server

# Ubuntu/Debian
sudo apt update
sudo apt install python3 python3-pip
pip3 install -r requirements.txt

# CentOS/RHEL/Fedora
sudo yum install python3 python3-pip  # or dnf
pip3 install -r requirements.txt

# Arch Linux
sudo pacman -S python python-pip
pip install -r requirements.txt
```

#### 2. Make Server Executable
```bash
chmod +x server.py
```

#### 3. Configure Claude Code
```bash
# Create config directory if it doesn't exist
mkdir -p ~/.config/Claude

# Edit configuration file
nano ~/.config/Claude/claude_desktop_config.json
```

Add this configuration:
```json
{
  "mcpServers": {
    "vita-design-system": {
      "command": "python3",
      "args": ["/full/path/to/vita-design/mcp-server/server.py"],
      "cwd": "/full/path/to/vita-design"
    }
  }
}
```

#### 4. Restart Claude Code
```bash
# If installed via snap
snap restart claude-code

# If installed via AppImage
# Just close and reopen the application
```

---

### 🪟 Windows Setup

#### 1. Install Python (if not installed)
- Download Python from [python.org](https://www.python.org/downloads/)
- ✅ Check "Add Python to PATH" during installation
- ✅ Check "Install pip"

#### 2. Install Dependencies
```cmd
# Open Command Prompt or PowerShell
cd C:\path\to\vita-design\mcp-server
pip install -r requirements.txt
```

#### 3. Configure Claude Code
```cmd
# Open configuration file
notepad %APPDATA%\Claude\claude_desktop_config.json
```

Add this configuration (replace `C:\full\path\to\` with your actual path):
```json
{
  "mcpServers": {
    "vita-design-system": {
      "command": "python",
      "args": ["C:\\full\\path\\to\\vita-design\\mcp-server\\server.py"],
      "cwd": "C:\\full\\path\\to\\vita-design"
    }
  }
}
```

#### 4. Restart Claude Code
Close and reopen Claude Code application.

---

## 🔧 Advanced Configuration

### Custom Python Environment

If you're using a virtual environment or specific Python version:

```json
{
  "mcpServers": {
    "vita-design-system": {
      "command": "/path/to/your/python",
      "args": ["/path/to/server.py"],
      "cwd": "/path/to/vita-design",
      "env": {
        "PYTHONPATH": "/path/to/your/venv/lib/python3.x/site-packages"
      }
    }
  }
}
```

### Debug Mode

Enable debug logging:

```json
{
  "mcpServers": {
    "vita-design-system": {
      "command": "python3",
      "args": ["/path/to/server.py", "--debug"],
      "cwd": "/path/to/vita-design"
    }
  }
}
```

### Multiple Environments

Configure different environments:

```json
{
  "mcpServers": {
    "vita-design-dev": {
      "command": "python3",
      "args": ["/path/to/dev/server.py"],
      "cwd": "/path/to/dev/vita-design"
    },
    "vita-design-prod": {
      "command": "python3", 
      "args": ["/path/to/prod/server.py"],
      "cwd": "/path/to/prod/vita-design"
    }
  }
}
```

---

## ✅ Verification Steps

### 1. Test Python Installation
```bash
python3 --version  # Should show Python 3.8+
pip3 --version     # Should show pip version
```

### 2. Test Dependencies
```bash
python3 -c "import mcp; print('MCP library installed')"
```

### 3. Test Server Syntax
```bash
cd /path/to/vita-design/mcp-server
python3 -m py_compile server.py
```

### 4. Test Claude Code Integration
1. Open Claude Code
2. Start a new conversation
3. Type: `@vita-design-system`
4. You should see the server listed in autocomplete

### 5. Test Basic Functionality
Try these commands in Claude Code:
```
@vita-design-system Show me available color tokens
@vita-design-system Generate a primary button with "Click me" text
@vita-design-system What's the value of vita-color-brand-primary?
```

---

## 🐛 Troubleshooting

### Common Issues

#### ❌ "Server not found" error
**Solutions:**
1. Check file paths in configuration are absolute and correct
2. Ensure `server.py` exists and is executable
3. Verify Python is in system PATH
4. Restart Claude Code after configuration changes

#### ❌ "Permission denied" error
**Solutions:**
```bash
# macOS/Linux
chmod +x server.py

# Windows
# Run Command Prompt as Administrator
```

#### ❌ "Module not found" error
**Solutions:**
```bash
pip install -r requirements.txt

# If using virtual environment
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
pip install -r requirements.txt
```

#### ❌ Design tokens not loading
**Solutions:**
1. Verify `DESIGN_TOKENS.css` exists in parent directory
2. Check file permissions: `ls -la ../DESIGN_TOKENS.css`
3. Review server logs in Claude Code

### Debug Commands

```bash
# Check Claude Code logs
# macOS
tail -f ~/Library/Logs/Claude/claude.log

# Windows
type %APPDATA%\Claude\logs\claude.log

# Linux
tail -f ~/.local/share/Claude/logs/claude.log
```

### Server Test Mode

Test the server independently:
```bash
cd /path/to/vita-design/mcp-server
python3 server.py --test
```

---

## 🔄 Updates and Maintenance

### Updating the Server

```bash
cd /path/to/vita-design
git pull origin main
cd mcp-server
pip install -r requirements.txt --upgrade
```

### Backup Configuration

```bash
# macOS
cp ~/Library/Application\ Support/Claude/claude_desktop_config.json ~/claude_backup.json

# Windows
copy %APPDATA%\Claude\claude_desktop_config.json %USERPROFILE%\claude_backup.json

# Linux
cp ~/.config/Claude/claude_desktop_config.json ~/claude_backup.json
```

---

## 📞 Getting Help

### Check These First
1. ✅ Python 3.8+ installed
2. ✅ All dependencies installed (`pip install -r requirements.txt`)
3. ✅ Correct file paths in configuration
4. ✅ Claude Code restarted after configuration
5. ✅ No syntax errors in `server.py`

### Documentation
- **This Guide**: Complete setup instructions
- **README.md**: Usage examples and API reference
- **Claude Code Docs**: https://docs.anthropic.com/claude/docs
- **MCP Specification**: https://modelcontextprotocol.io/

### Support Channels
- Create an issue in the repository
- Check existing issues for similar problems
- Contact the ViTA development team

---

**🎉 Once setup is complete, you can start using the ViTA Design System directly in Claude Code!**