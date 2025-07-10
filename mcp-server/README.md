# ViTA Design System MCP Server

## 🎯 Overview

The **ViTA Design System MCP Server** provides seamless access to the ViTA Design System through the Model Context Protocol (MCP). This allows Claude Code and other AI assistants to instantly access design tokens, generate components, and create layouts using the ViTA design system.

### What is MCP?

**Model Context Protocol (MCP)** is like a "USB-C for AI" - it provides a standardized way for AI models to connect to external data sources and tools. Instead of manually reading files and explaining your design system every time, Claude can automatically access all your design tokens, components, and guidelines.

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Claude Code (desktop app)
- ViTA Design System files

### Installation

1. **Clone or download this repository:**
```bash
cd /path/to/vita-design/mcp-server
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

3. **Make the server executable:**
```bash
chmod +x server.py
```

### Configuration

#### macOS/Linux Setup

1. **Edit Claude Code settings:**
```bash
# Open settings file
code ~/Library/Application\ Support/Claude/claude_desktop_config.json
```

2. **Add MCP server configuration:**
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

#### Windows Setup

1. **Open Claude Code settings:**
```cmd
notepad %APPDATA%\Claude\claude_desktop_config.json
```

2. **Add MCP server configuration:**
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

3. **Restart Claude Code**

## 🎨 Usage Examples

Once configured, you can interact with the ViTA Design System directly through Claude:

### Basic Commands

```
@vita-design-system Create a primary button with "Get Started" text
@vita-design-system Show me all available color tokens
@vita-design-system Generate a dashboard layout with cards and buttons
@vita-design-system What's the value of the primary brand color?
@vita-design-system Create a form with validation styles
@vita-design-system Validate this HTML code against ViTA standards
```

### Advanced Examples

```
Create a landing page layout using ViTA design system with:
- Hero section with primary and secondary buttons
- Three feature cards in a grid
- Dark theme support
- Mobile responsive design

Generate a user profile page with:
- Profile card with avatar placeholder
- Editable form fields
- Settings section with toggles
- Light theme

Validate this code and ensure it follows ViTA accessibility guidelines:
[paste your HTML/CSS code]
```

## 📋 Available Resources

The MCP server exposes the following resources that Claude can access:

### Design Tokens
- `vita://tokens/colors` - Complete color system (brand, surface, semantic)
- `vita://tokens/typography` - Font families, sizes, weights, line heights
- `vita://tokens/spacing` - 4px-based spacing system

### Components
- `vita://components/buttons` - Button variants and states
- `vita://components/inputs` - Form input styles and validation
- `vita://components/cards` - Card layouts and containers

### Themes
- `vita://themes/light` - Light theme configuration
- `vita://themes/dark` - Dark theme configuration

### Guidelines
- `vita://guidelines/accessibility` - WCAG 2.1 AA compliance guidelines

### Examples
- `vita://examples/layouts` - Pre-built layout templates

## 🔧 Available Tools

### `generate_component`
Generates HTML/CSS code for ViTA components.

**Parameters:**
- `component_type`: "button", "input", "card", "badge", "layout"
- `variant`: Component variant (e.g., "primary", "secondary")
- `theme`: "light", "dark", or "auto"
- `content`: Text content for the component
- `attributes`: Additional HTML attributes

**Example:**
```json
{
  "component_type": "button",
  "variant": "primary", 
  "content": "Get Started",
  "theme": "dark",
  "attributes": {"onclick": "handleClick()"}
}
```

### `create_layout`
Creates complete page layouts using ViTA design system.

**Parameters:**
- `layout_type`: "dashboard", "form", "landing", "profile", "settings"
- `components`: List of components to include
- `theme`: Theme preference
- `responsive`: Enable responsive design (default: true)

### `validate_design`
Validates HTML/CSS code against ViTA design standards.

**Parameters:**
- `code`: HTML/CSS code to validate
- `check_accessibility`: Include accessibility validation (default: true)

### `get_token_value`
Retrieves the current value of a specific design token.

**Parameters:**
- `token_name`: Name of the design token
- `theme`: "light" or "dark" (default: "light")

## 🔍 How It Works

### Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Claude Code   │◄──►│   MCP Server    │◄──►│ ViTA Files      │
│                 │    │                 │    │                 │
│ - Chat Interface│    │ - Parse CSS     │    │ - DESIGN_TOKENS │
│ - Tool Calls    │    │ - Generate Code │    │ - Figma JSON    │
│ - Resource Refs │    │ - Validate      │    │ - Components    │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

### Data Flow

1. **Initialization**: Server loads and parses ViTA design system files
2. **Resource Access**: Claude requests design tokens via `vita://` URIs
3. **Tool Execution**: Claude calls tools to generate components or layouts
4. **Response**: Server returns structured data or generated HTML/CSS

### Token Parsing

The server automatically parses your `DESIGN_TOKENS.css` file and extracts:
- CSS custom properties (`--vita-*`)
- Component class definitions
- Theme configurations
- Color values and descriptions

## 🛠️ Development

### File Structure

```
mcp-server/
├── server.py              # Main MCP server implementation
├── requirements.txt       # Python dependencies
├── README.md              # This documentation
├── setup.py               # Installation script
└── tests/
    ├── test_server.py     # Server tests
    └── test_tokens.py     # Token parsing tests
```

### Testing

```bash
# Install development dependencies
pip install pytest pytest-asyncio

# Run tests
python -m pytest tests/

# Test server directly
python server.py
```

### Debugging

1. **Enable debug logging:**
```python
logging.basicConfig(level=logging.DEBUG)
```

2. **Check Claude Code logs:**
   - macOS: `~/Library/Logs/Claude/`
   - Windows: `%APPDATA%\Claude\logs\`
   - Linux: `~/.local/share/Claude/logs/`

3. **Test MCP connection:**
```bash
# Run server in test mode
python server.py --test
```

## ⚠️ Troubleshooting

### Common Issues

#### "Server not found" error
- ✅ Check file paths in `claude_desktop_config.json`
- ✅ Ensure `server.py` is executable
- ✅ Verify Python is in PATH
- ✅ Restart Claude Code after configuration changes

#### "Permission denied" error
```bash
chmod +x server.py
```

#### "Module not found" error
```bash
pip install -r requirements.txt
```

#### Design tokens not loading
- ✅ Verify `DESIGN_TOKENS.css` exists in parent directory
- ✅ Check file permissions
- ✅ Review server logs for parsing errors

### Debug Commands

```bash
# Test Python installation
python3 --version

# Test MCP library
python3 -c "import mcp; print('MCP library installed')"

# Check file permissions
ls -la server.py

# Test server syntax
python3 -m py_compile server.py
```

## 🚀 Advanced Configuration

### Custom Token Mapping

You can extend the server to parse additional token formats:

```python
# In server.py, modify _parse_css_tokens method
def _parse_custom_tokens(self, content: str):
    # Add custom parsing logic
    pass
```

### Performance Optimization

For large design systems, enable caching:

```json
{
  "mcpServers": {
    "vita-design-system": {
      "command": "python3",
      "args": ["/path/to/server.py", "--cache"],
      "cwd": "/path/to/vita-design"
    }
  }
}
```

### Integration with CI/CD

Auto-update design tokens when your repository changes:

```bash
# Add to your GitHub Actions workflow
- name: Update MCP Server
  run: |
    cd mcp-server
    python update_tokens.py
```

## 📚 Examples Repository

Check out our examples repository for complete implementations:

- **E-commerce Dashboard**: Full dashboard with ViTA components
- **Authentication Forms**: Login/signup flows with validation
- **Landing Pages**: Marketing pages with responsive design
- **Admin Panels**: Complex layouts with data tables and charts

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Add tests for new functionality
4. Submit a pull request

## 📄 License

This MCP server is part of the ViTA Design System project by Percepthor. For licensing information, please contact the development team.

---

## 📞 Support

- **Documentation**: Check this README and inline code comments
- **Issues**: Create an issue in the repository
- **Claude Code Help**: Visit [Claude Code documentation](https://docs.anthropic.com/claude/docs)
- **MCP Protocol**: See [MCP specification](https://modelcontextprotocol.io/)

---

**Built with ❤️ by the ViTA Design Team**