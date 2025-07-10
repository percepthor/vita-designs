#!/usr/bin/env python3
"""
ViTA Design System MCP Server

This server provides access to the ViTA Design System tokens, components,
and tools through the Model Context Protocol (MCP).

Author: ViTA Design Team
License: Private - Percepthor Organization
"""

import asyncio
import json
import logging
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional, Sequence

import mcp.server.stdio
import mcp.types as types
from mcp.server import NotificationOptions, Server
from mcp.server.models import InitializationOptions

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("vita-design-mcp")

class ViTADesignSystemMCP:
    """Main MCP server class for ViTA Design System"""
    
    def __init__(self):
        self.server = Server("vita-design-system")
        self.design_data = {}
        self.base_path = Path(__file__).parent.parent
        
        # Setup handlers
        self._setup_handlers()
        
    def _setup_handlers(self):
        """Setup MCP server handlers"""
        
        @self.server.list_resources()
        async def handle_list_resources() -> list[types.Resource]:
            """List all available design system resources"""
            return [
                types.Resource(
                    uri="vita://tokens/colors",
                    name="Color Tokens",
                    description="Complete color system including brand, surface, semantic, and functional colors",
                    mimeType="application/json",
                ),
                types.Resource(
                    uri="vita://tokens/typography",
                    name="Typography Tokens", 
                    description="Font families, sizes, weights, and text styles",
                    mimeType="application/json",
                ),
                types.Resource(
                    uri="vita://tokens/spacing",
                    name="Spacing System",
                    description="4px-based spacing tokens for consistent layouts",
                    mimeType="application/json",
                ),
                types.Resource(
                    uri="vita://components/buttons",
                    name="Button Components",
                    description="Button variants, states, and usage guidelines",
                    mimeType="application/json",
                ),
                types.Resource(
                    uri="vita://components/inputs",
                    name="Input Components", 
                    description="Form input styles and validation states",
                    mimeType="application/json",
                ),
                types.Resource(
                    uri="vita://components/cards",
                    name="Card Components",
                    description="Card layouts and container styles",
                    mimeType="application/json",
                ),
                types.Resource(
                    uri="vita://themes/light",
                    name="Light Theme",
                    description="Light theme configuration and tokens",
                    mimeType="application/json",
                ),
                types.Resource(
                    uri="vita://themes/dark", 
                    name="Dark Theme",
                    description="Dark theme configuration and tokens",
                    mimeType="application/json",
                ),
                types.Resource(
                    uri="vita://guidelines/accessibility",
                    name="Accessibility Guidelines",
                    description="WCAG 2.1 AA compliance guidelines and best practices",
                    mimeType="application/json",
                ),
                types.Resource(
                    uri="vita://examples/layouts",
                    name="Layout Examples",
                    description="Pre-built layout templates and patterns",
                    mimeType="application/json",
                ),
            ]

        @self.server.read_resource()
        async def handle_read_resource(uri: types.AnyUrl) -> str:
            """Read a specific design system resource"""
            
            # Load design data if not already loaded
            await self._load_design_data()
            
            uri_str = str(uri)
            
            if uri_str == "vita://tokens/colors":
                return json.dumps(self.design_data.get("colors", {}), indent=2)
            elif uri_str == "vita://tokens/typography":
                return json.dumps(self.design_data.get("typography", {}), indent=2)
            elif uri_str == "vita://tokens/spacing":
                return json.dumps(self.design_data.get("spacing", {}), indent=2)
            elif uri_str == "vita://components/buttons":
                return json.dumps(self.design_data.get("components", {}).get("buttons", {}), indent=2)
            elif uri_str == "vita://components/inputs":
                return json.dumps(self.design_data.get("components", {}).get("inputs", {}), indent=2)
            elif uri_str == "vita://components/cards":
                return json.dumps(self.design_data.get("components", {}).get("cards", {}), indent=2)
            elif uri_str == "vita://themes/light":
                return json.dumps(self.design_data.get("themes", {}).get("light", {}), indent=2)
            elif uri_str == "vita://themes/dark":
                return json.dumps(self.design_data.get("themes", {}).get("dark", {}), indent=2)
            elif uri_str == "vita://guidelines/accessibility":
                return json.dumps(self.design_data.get("guidelines", {}).get("accessibility", {}), indent=2)
            elif uri_str == "vita://examples/layouts":
                return json.dumps(self.design_data.get("examples", {}).get("layouts", {}), indent=2)
            else:
                raise ValueError(f"Unknown resource URI: {uri}")

        @self.server.list_tools()
        async def handle_list_tools() -> list[types.Tool]:
            """List all available design system tools"""
            return [
                types.Tool(
                    name="generate_component",
                    description="Generate HTML/CSS code for ViTA design system components",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "component_type": {
                                "type": "string",
                                "enum": ["button", "input", "card", "badge", "layout"],
                                "description": "Type of component to generate"
                            },
                            "variant": {
                                "type": "string", 
                                "description": "Component variant (e.g., 'primary', 'secondary', 'error')"
                            },
                            "theme": {
                                "type": "string",
                                "enum": ["light", "dark", "auto"],
                                "default": "auto",
                                "description": "Theme to apply"
                            },
                            "content": {
                                "type": "string",
                                "description": "Content/text for the component"
                            },
                            "attributes": {
                                "type": "object",
                                "description": "Additional HTML attributes"
                            }
                        },
                        "required": ["component_type"]
                    },
                ),
                types.Tool(
                    name="create_layout",
                    description="Create complete page layouts using ViTA design system",
                    inputSchema={
                        "type": "object", 
                        "properties": {
                            "layout_type": {
                                "type": "string",
                                "enum": ["dashboard", "form", "landing", "profile", "settings"],
                                "description": "Type of layout to create"
                            },
                            "components": {
                                "type": "array",
                                "items": {"type": "string"},
                                "description": "List of components to include"
                            },
                            "theme": {
                                "type": "string", 
                                "enum": ["light", "dark", "auto"],
                                "default": "auto"
                            },
                            "responsive": {
                                "type": "boolean",
                                "default": True,
                                "description": "Include responsive design"
                            }
                        },
                        "required": ["layout_type"]
                    },
                ),
                types.Tool(
                    name="validate_design",
                    description="Validate that provided CSS/HTML uses correct ViTA design tokens",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "code": {
                                "type": "string",
                                "description": "HTML/CSS code to validate"
                            },
                            "check_accessibility": {
                                "type": "boolean", 
                                "default": True,
                                "description": "Include accessibility validation"
                            }
                        },
                        "required": ["code"]
                    },
                ),
                types.Tool(
                    name="get_token_value",
                    description="Get the current value of a specific design token",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "token_name": {
                                "type": "string",
                                "description": "Name of the design token (e.g., 'vita-color-brand-primary')"
                            },
                            "theme": {
                                "type": "string",
                                "enum": ["light", "dark"],
                                "default": "light"
                            }
                        },
                        "required": ["token_name"]
                    },
                ),
            ]

        @self.server.call_tool()
        async def handle_call_tool(
            name: str, arguments: dict[str, Any] | None
        ) -> list[types.TextContent]:
            """Handle tool calls"""
            
            if not arguments:
                arguments = {}
                
            await self._load_design_data()
            
            if name == "generate_component":
                return await self._generate_component(arguments)
            elif name == "create_layout":
                return await self._create_layout(arguments)
            elif name == "validate_design":
                return await self._validate_design(arguments)
            elif name == "get_token_value":
                return await self._get_token_value(arguments)
            else:
                raise ValueError(f"Unknown tool: {name}")

    async def _load_design_data(self):
        """Load design system data from files"""
        if self.design_data:
            return  # Already loaded
            
        try:
            # Parse CSS tokens
            css_file = self.base_path / "DESIGN_TOKENS.css"
            if css_file.exists():
                self.design_data = await self._parse_css_tokens(css_file)
            
            # Load Figma tokens if available
            figma_file = self.base_path / "FIGMA_DESIGN_TOKENS.json"
            if figma_file.exists():
                with open(figma_file, 'r') as f:
                    figma_data = json.load(f)
                    self._merge_figma_data(figma_data)
                    
            logger.info("Design system data loaded successfully")
            
        except Exception as e:
            logger.error(f"Error loading design data: {e}")
            self.design_data = self._get_fallback_data()

    async def _parse_css_tokens(self, css_file: Path) -> Dict[str, Any]:
        """Parse CSS custom properties into structured data"""
        tokens = {
            "colors": {},
            "typography": {},
            "spacing": {},
            "components": {"buttons": {}, "inputs": {}, "cards": {}},
            "themes": {"light": {}, "dark": {}},
            "guidelines": {"accessibility": {}},
            "examples": {"layouts": {}}
        }
        
        try:
            with open(css_file, 'r') as f:
                content = f.read()
                
            # Extract CSS custom properties
            import re
            
            # Find all CSS custom properties
            property_pattern = r'--vita-([^:]+):\s*([^;]+);'
            matches = re.findall(property_pattern, content)
            
            for prop_name, value in matches:
                value = value.strip()
                
                # Categorize tokens
                if prop_name.startswith('color-'):
                    category = prop_name.replace('color-', '').replace('-', '_')
                    tokens["colors"][f"vita_color_{category}"] = {
                        "value": value,
                        "css_var": f"--vita-color-{prop_name.replace('color-', '')}",
                        "description": f"ViTA color token for {category.replace('_', ' ')}"
                    }
                elif prop_name.startswith('font-'):
                    category = prop_name.replace('font-', '').replace('-', '_')
                    tokens["typography"][f"vita_font_{category}"] = {
                        "value": value,
                        "css_var": f"--vita-font-{prop_name.replace('font-', '')}",
                        "description": f"ViTA typography token for {category.replace('_', ' ')}"
                    }
                elif prop_name.startswith('spacing-'):
                    category = prop_name.replace('spacing-', '').replace('-', '_')
                    tokens["spacing"][f"vita_spacing_{category}"] = {
                        "value": value,
                        "css_var": f"--vita-spacing-{prop_name.replace('spacing-', '')}",
                        "description": f"ViTA spacing token {category}"
                    }
                    
            # Add component definitions
            tokens["components"]["buttons"] = {
                "primary": {
                    "class": "vita-button vita-button-primary",
                    "description": "Primary action button",
                    "usage": "Main CTAs, form submissions"
                },
                "secondary": {
                    "class": "vita-button vita-button-secondary", 
                    "description": "Secondary action button",
                    "usage": "Secondary actions, cancel buttons"
                },
                "edit": {
                    "class": "vita-button vita-button-edit",
                    "description": "Edit action button",
                    "usage": "Edit operations, modify content"
                },
                "delete": {
                    "class": "vita-button vita-button-delete",
                    "description": "Delete action button", 
                    "usage": "Destructive actions, remove content"
                }
            }
            
            tokens["components"]["inputs"] = {
                "default": {
                    "class": "vita-input",
                    "description": "Standard text input",
                    "states": ["default", "focus", "error", "disabled"]
                },
                "label": {
                    "class": "vita-input-label",
                    "description": "Input label styling"
                }
            }
            
            tokens["components"]["cards"] = {
                "default": {
                    "class": "vita-card",
                    "description": "Standard content card",
                    "usage": "Content containers, information display"
                }
            }
            
            # Theme configurations
            tokens["themes"]["light"] = {
                "data_attribute": "data-theme=\"light\"",
                "description": "Light theme configuration",
                "primary_surface": "var(--vita-color-surface-background)",
                "primary_text": "var(--vita-color-text-on-surface)"
            }
            
            tokens["themes"]["dark"] = {
                "data_attribute": "data-theme=\"dark\"", 
                "description": "Dark theme configuration",
                "primary_surface": "var(--vita-color-surface-background)", 
                "primary_text": "var(--vita-color-text-on-surface)"
            }
            
            # Accessibility guidelines
            tokens["guidelines"]["accessibility"] = {
                "contrast_ratios": {
                    "normal_text": "4.5:1 minimum (WCAG AA)",
                    "large_text": "3:1 minimum (WCAG AA)"
                },
                "focus_indicators": {
                    "outline": "2px solid var(--vita-color-brand-primary)",
                    "offset": "2px"
                },
                "semantic_markup": [
                    "Use proper heading hierarchy (h1-h6)",
                    "Include ARIA labels where appropriate", 
                    "Use semantic HTML elements"
                ]
            }
            
            # Layout examples
            tokens["examples"]["layouts"] = {
                "dashboard": {
                    "description": "Analytics dashboard layout",
                    "components": ["navigation", "cards", "charts", "tables"]
                },
                "form": {
                    "description": "Form layout with validation",
                    "components": ["inputs", "labels", "buttons", "validation"]
                },
                "landing": {
                    "description": "Landing page layout", 
                    "components": ["hero", "features", "cta", "footer"]
                }
            }
            
        except Exception as e:
            logger.error(f"Error parsing CSS tokens: {e}")
            
        return tokens

    def _merge_figma_data(self, figma_data: Dict[str, Any]):
        """Merge Figma design tokens with parsed CSS data"""
        try:
            if "tokens" in figma_data and "color" in figma_data["tokens"]:
                # Add Figma color information
                figma_colors = figma_data["tokens"]["color"]
                for category, colors in figma_colors.items():
                    for color_name, color_data in colors.items():
                        if isinstance(color_data, dict):
                            for theme, theme_data in color_data.items():
                                if isinstance(theme_data, dict) and "value" in theme_data:
                                    token_key = f"vita_color_{category}_{color_name}_{theme}"
                                    if token_key not in self.design_data["colors"]:
                                        self.design_data["colors"][token_key] = {
                                            "value": theme_data["value"],
                                            "figma_path": f"color.{category}.{color_name}.{theme}",
                                            "description": theme_data.get("description", "")
                                        }
        except Exception as e:
            logger.error(f"Error merging Figma data: {e}")

    def _get_fallback_data(self) -> Dict[str, Any]:
        """Provide fallback data if files can't be loaded"""
        return {
            "colors": {
                "vita_color_brand_primary": {
                    "value": "#003965",
                    "css_var": "--vita-color-brand-primary",
                    "description": "Primary brand color"
                }
            },
            "typography": {},
            "spacing": {},
            "components": {"buttons": {}, "inputs": {}, "cards": {}},
            "themes": {"light": {}, "dark": {}},
            "guidelines": {"accessibility": {}},
            "examples": {"layouts": {}}
        }

    async def _generate_component(self, args: Dict[str, Any]) -> list[types.TextContent]:
        """Generate component HTML/CSS code"""
        component_type = args.get("component_type")
        variant = args.get("variant", "default")
        theme = args.get("theme", "auto")
        content = args.get("content", "")
        attributes = args.get("attributes", {})
        
        # Generate HTML based on component type
        if component_type == "button":
            html = self._generate_button_html(variant, content, attributes, theme)
        elif component_type == "input":
            html = self._generate_input_html(variant, content, attributes, theme)
        elif component_type == "card":
            html = self._generate_card_html(variant, content, attributes, theme)
        elif component_type == "badge":
            html = self._generate_badge_html(variant, content, attributes, theme)
        elif component_type == "layout":
            html = self._generate_layout_html(variant, content, attributes, theme)
        else:
            return [types.TextContent(
                type="text",
                text=f"Error: Unknown component type '{component_type}'"
            )]
            
        return [types.TextContent(
            type="text", 
            text=f"Generated {component_type} component:\n\n```html\n{html}\n```"
        )]

    def _generate_button_html(self, variant: str, content: str, attributes: Dict, theme: str) -> str:
        """Generate button HTML"""
        content = content or "Button"
        class_name = f"vita-button vita-button-{variant}" if variant != "default" else "vita-button"
        
        attrs_str = " ".join([f'{k}="{v}"' for k, v in attributes.items()])
        theme_attr = f' data-theme="{theme}"' if theme != "auto" else ""
        
        return f'<button class="{class_name}"{theme_attr} {attrs_str}>{content}</button>'

    def _generate_input_html(self, variant: str, content: str, attributes: Dict, theme: str) -> str:
        """Generate input HTML"""
        label_text = content or "Label"
        placeholder = attributes.get("placeholder", "Enter value")
        input_type = attributes.get("type", "text")
        
        theme_attr = f' data-theme="{theme}"' if theme != "auto" else ""
        error_class = " error" if variant == "error" else ""
        
        return f'''<div class="demo-input-group"{theme_attr}>
    <label class="vita-input-label">{label_text}</label>
    <input type="{input_type}" class="vita-input{error_class}" placeholder="{placeholder}">
</div>'''

    def _generate_card_html(self, variant: str, content: str, attributes: Dict, theme: str) -> str:
        """Generate card HTML"""
        title = attributes.get("title", "Card Title")
        content = content or "Card content goes here..."
        
        theme_attr = f' data-theme="{theme}"' if theme != "auto" else ""
        
        return f'''<div class="vita-card"{theme_attr}>
    <h3 class="vita-text-headline-small">{title}</h3>
    <p class="vita-text-body-medium">{content}</p>
</div>'''

    def _generate_badge_html(self, variant: str, content: str, attributes: Dict, theme: str) -> str:
        """Generate badge HTML"""
        content = content or "Badge"
        class_name = f"vita-status-badge vita-status-badge-{variant}" if variant != "default" else "vita-status-badge"
        
        theme_attr = f' data-theme="{theme}"' if theme != "auto" else ""
        
        return f'<span class="{class_name}"{theme_attr}>{content}</span>'

    def _generate_layout_html(self, variant: str, content: str, attributes: Dict, theme: str) -> str:
        """Generate layout HTML"""
        columns = attributes.get("columns", 2)
        theme_attr = f' data-theme="{theme}"' if theme != "auto" else ""
        
        return f'''<div class="vita-container"{theme_attr}>
    <div class="grid grid-{columns}">
        <div class="vita-card">
            <h3>Section 1</h3>
            <p>Content here...</p>
        </div>
        <div class="vita-card">
            <h3>Section 2</h3>
            <p>Content here...</p>
        </div>
    </div>
</div>'''

    async def _create_layout(self, args: Dict[str, Any]) -> list[types.TextContent]:
        """Create complete page layout"""
        layout_type = args.get("layout_type")
        components = args.get("components", [])
        theme = args.get("theme", "auto")
        responsive = args.get("responsive", True)
        
        # Generate complete HTML page
        html = self._generate_complete_layout(layout_type, components, theme, responsive)
        
        return [types.TextContent(
            type="text",
            text=f"Generated {layout_type} layout:\n\n```html\n{html}\n```"
        )]

    def _generate_complete_layout(self, layout_type: str, components: List[str], theme: str, responsive: bool) -> str:
        """Generate complete HTML layout"""
        theme_attr = f'data-theme="{theme}"' if theme != "auto" else 'data-theme="light"'
        
        head_section = '''<!DOCTYPE html>
<html lang="en" ''' + theme_attr + '''>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ViTA Design System - ''' + layout_type.title() + '''</title>
    <link rel="stylesheet" href="./DESIGN_TOKENS.css">
    <link href="https://fonts.googleapis.com/css2?family=Heebo:wght@400;500;600;700&family=Poppins:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
    <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
</head>
<body>'''

        if layout_type == "dashboard":
            body_content = self._generate_dashboard_layout(components)
        elif layout_type == "form":
            body_content = self._generate_form_layout(components)
        elif layout_type == "landing":
            body_content = self._generate_landing_layout(components)
        elif layout_type == "profile":
            body_content = self._generate_profile_layout(components)
        elif layout_type == "settings":
            body_content = self._generate_settings_layout(components)
        else:
            body_content = '<div class="vita-container"><h1>Unknown layout type</h1></div>'

        footer_section = '''</body>
</html>'''

        return head_section + '\n' + body_content + '\n' + footer_section

    def _generate_dashboard_layout(self, components: List[str]) -> str:
        """Generate dashboard layout"""
        return '''    <div class="vita-container">
        <header class="vita-card" style="margin-bottom: var(--vita-spacing-6);">
            <h1 class="vita-text-display-medium">Dashboard</h1>
            <p class="vita-text-body-large">Welcome to your ViTA dashboard</p>
        </header>
        
        <div class="grid grid-4">
            <div class="vita-card" style="text-align: center;">
                <h3 class="vita-text-headline-small">Active</h3>
                <div class="vita-text-display-small" style="color: var(--vita-color-semantic-success);">24</div>
                <span class="vita-status-badge vita-status-badge-success">Running</span>
            </div>
            <div class="vita-card" style="text-align: center;">
                <h3 class="vita-text-headline-small">Pending</h3>
                <div class="vita-text-display-small" style="color: var(--vita-color-semantic-warning);">8</div>
                <span class="vita-status-badge vita-status-badge-warning">Review</span>
            </div>
            <div class="vita-card" style="text-align: center;">
                <h3 class="vita-text-headline-small">Completed</h3>
                <div class="vita-text-display-small" style="color: var(--vita-color-brand-primary);">156</div>
                <span class="vita-status-badge vita-status-badge-success">Done</span>
            </div>
            <div class="vita-card" style="text-align: center;">
                <h3 class="vita-text-headline-small">Errors</h3>
                <div class="vita-text-display-small" style="color: var(--vita-color-semantic-error);">2</div>
                <span class="vita-status-badge vita-status-badge-error">Attention</span>
            </div>
        </div>
    </div>'''

    def _generate_form_layout(self, components: List[str]) -> str:
        """Generate form layout"""
        return '''    <div class="vita-container-content">
        <div class="vita-card" style="max-width: 500px; margin: 0 auto;">
            <h2 class="vita-text-headline-large">Contact Form</h2>
            <form style="margin-top: var(--vita-spacing-6);">
                <div class="demo-input-group">
                    <label class="vita-input-label">Full Name *</label>
                    <input type="text" class="vita-input" placeholder="Enter your full name" required>
                </div>
                
                <div class="demo-input-group">
                    <label class="vita-input-label">Email Address *</label>
                    <input type="email" class="vita-input" placeholder="Enter your email" required>
                </div>
                
                <div class="demo-input-group">
                    <label class="vita-input-label">Message</label>
                    <textarea class="vita-input" rows="4" placeholder="Enter your message"></textarea>
                </div>
                
                <div style="display: flex; gap: var(--vita-spacing-3); margin-top: var(--vita-spacing-6);">
                    <button type="submit" class="vita-button vita-button-primary">Send Message</button>
                    <button type="reset" class="vita-button vita-button-secondary">Clear</button>
                </div>
            </form>
        </div>
    </div>'''

    def _generate_landing_layout(self, components: List[str]) -> str:
        """Generate landing page layout"""
        return '''    <div class="vita-container">
        <header style="text-align: center; padding: var(--vita-spacing-8) 0;">
            <h1 class="vita-text-display-large">Welcome to ViTA</h1>
            <p class="vita-text-headline-medium" style="margin-top: var(--vita-spacing-4);">
                Powerful design system for modern applications
            </p>
            <div style="margin-top: var(--vita-spacing-6);">
                <button class="vita-button vita-button-primary vita-button-action">Get Started</button>
                <button class="vita-button vita-button-secondary vita-button-action" style="margin-left: var(--vita-spacing-3);">Learn More</button>
            </div>
        </header>
        
        <div class="grid grid-3" style="margin-top: var(--vita-spacing-8);">
            <div class="vita-card" style="text-align: center;">
                <h3 class="vita-text-headline-small">Fast Development</h3>
                <p class="vita-text-body-medium">Build interfaces quickly with pre-designed components</p>
            </div>
            <div class="vita-card" style="text-align: center;">
                <h3 class="vita-text-headline-small">Consistent Design</h3>
                <p class="vita-text-body-medium">Maintain visual consistency across all your applications</p>
            </div>
            <div class="vita-card" style="text-align: center;">
                <h3 class="vita-text-headline-small">Accessible</h3>
                <p class="vita-text-body-medium">WCAG 2.1 AA compliant components out of the box</p>
            </div>
        </div>
    </div>'''

    def _generate_profile_layout(self, components: List[str]) -> str:
        """Generate profile layout"""
        return '''    <div class="vita-container">
        <div class="grid grid-3">
            <div class="vita-card">
                <div style="text-align: center;">
                    <div style="width: 80px; height: 80px; background: var(--vita-color-brand-primary); border-radius: 50%; margin: 0 auto var(--vita-spacing-4);"></div>
                    <h3 class="vita-text-headline-small">John Doe</h3>
                    <p class="vita-text-body-medium">Senior Developer</p>
                    <button class="vita-button vita-button-edit" style="margin-top: var(--vita-spacing-4);">Edit Profile</button>
                </div>
            </div>
            
            <div style="grid-column: span 2;">
                <div class="vita-card">
                    <h3 class="vita-text-headline-small">Profile Information</h3>
                    <div style="margin-top: var(--vita-spacing-4);">
                        <div class="demo-input-group">
                            <label class="vita-input-label">Email</label>
                            <input type="email" class="vita-input" value="john.doe@example.com">
                        </div>
                        <div class="demo-input-group">
                            <label class="vita-input-label">Phone</label>
                            <input type="tel" class="vita-input" value="+1 (555) 123-4567">
                        </div>
                        <div class="demo-input-group">
                            <label class="vita-input-label">Bio</label>
                            <textarea class="vita-input" rows="3">Passionate developer with 5+ years of experience...</textarea>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>'''

    def _generate_settings_layout(self, components: List[str]) -> str:
        """Generate settings layout"""
        return '''    <div class="vita-container">
        <h1 class="vita-text-display-medium">Settings</h1>
        
        <div style="margin-top: var(--vita-spacing-6);">
            <div class="vita-card">
                <h3 class="vita-text-headline-small">Appearance</h3>
                <div style="margin-top: var(--vita-spacing-4);">
                    <div class="demo-input-group">
                        <label class="vita-input-label">Theme</label>
                        <select class="vita-input">
                            <option>Light</option>
                            <option>Dark</option>
                            <option>Auto</option>
                        </select>
                    </div>
                    <div style="display: flex; align-items: center; margin-top: var(--vita-spacing-3);">
                        <input type="checkbox" id="animations" style="margin-right: var(--vita-spacing-2);">
                        <label for="animations" class="vita-text-body-medium">Enable animations</label>
                    </div>
                </div>
            </div>
            
            <div class="vita-card" style="margin-top: var(--vita-spacing-4);">
                <h3 class="vita-text-headline-small">Notifications</h3>
                <div style="margin-top: var(--vita-spacing-4);">
                    <div style="display: flex; align-items: center; margin-bottom: var(--vita-spacing-3);">
                        <input type="checkbox" id="email-notif" checked style="margin-right: var(--vita-spacing-2);">
                        <label for="email-notif" class="vita-text-body-medium">Email notifications</label>
                    </div>
                    <div style="display: flex; align-items: center; margin-bottom: var(--vita-spacing-3);">
                        <input type="checkbox" id="push-notif" style="margin-right: var(--vita-spacing-2);">
                        <label for="push-notif" class="vita-text-body-medium">Push notifications</label>
                    </div>
                </div>
            </div>
            
            <div style="margin-top: var(--vita-spacing-6);">
                <button class="vita-button vita-button-primary">Save Changes</button>
                <button class="vita-button vita-button-secondary" style="margin-left: var(--vita-spacing-3);">Cancel</button>
            </div>
        </div>
    </div>'''

    async def _validate_design(self, args: Dict[str, Any]) -> list[types.TextContent]:
        """Validate design against ViTA standards"""
        code = args.get("code", "")
        check_accessibility = args.get("check_accessibility", True)
        
        validation_results = []
        
        # Check for ViTA classes
        import re
        vita_classes = re.findall(r'vita-[\w-]+', code)
        if not vita_classes:
            validation_results.append("❌ No ViTA design system classes found")
        else:
            validation_results.append(f"✅ Found {len(vita_classes)} ViTA classes: {', '.join(set(vita_classes))}")
        
        # Check for proper theme setup
        if 'data-theme=' in code:
            validation_results.append("✅ Theme attribute found")
        else:
            validation_results.append("⚠️ No theme attribute found (recommended: data-theme='light' or 'dark')")
        
        # Check for accessibility if requested
        if check_accessibility:
            if 'alt=' in code and 'img' in code:
                validation_results.append("✅ Alt text found for images")
            if 'aria-' in code:
                validation_results.append("✅ ARIA attributes found")
            if '<label' in code and 'for=' in code:
                validation_results.append("✅ Proper form labels found")
        
        # Check for design token usage
        token_pattern = r'var\(--vita-[\w-]+\)'
        tokens_used = re.findall(token_pattern, code)
        if tokens_used:
            validation_results.append(f"✅ Using {len(tokens_used)} design tokens: {', '.join(set(tokens_used))}")
        else:
            validation_results.append("⚠️ No design tokens (CSS custom properties) found")
        
        result_text = "Design Validation Results:\n\n" + "\n".join(validation_results)
        
        return [types.TextContent(type="text", text=result_text)]

    async def _get_token_value(self, args: Dict[str, Any]) -> list[types.TextContent]:
        """Get the value of a design token"""
        token_name = args.get("token_name", "")
        theme = args.get("theme", "light")
        
        # Look for token in our data
        for category in self.design_data.values():
            if isinstance(category, dict):
                for token_key, token_data in category.items():
                    if isinstance(token_data, dict) and token_data.get("css_var") == f"--{token_name}":
                        return [types.TextContent(
                            type="text",
                            text=f"Token: {token_name}\nValue: {token_data.get('value', 'Not found')}\nDescription: {token_data.get('description', 'No description')}"
                        )]
        
        return [types.TextContent(
            type="text",
            text=f"Token '{token_name}' not found in ViTA design system"
        )]

    async def run(self):
        """Run the MCP server"""
        async with mcp.server.stdio.stdio_server() as (read_stream, write_stream):
            await self.server.run(
                read_stream,
                write_stream,
                InitializationOptions(
                    server_name="vita-design-system",
                    server_version="1.0.0",
                    capabilities=self.server.get_capabilities(
                        notification_options=NotificationOptions(),
                        experimental_capabilities={},
                    ),
                ),
            )

async def main():
    """Main entry point"""
    try:
        server = ViTADesignSystemMCP()
        await server.run()
    except KeyboardInterrupt:
        logger.info("Server stopped by user")
    except Exception as e:
        logger.error(f"Server error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    asyncio.run(main())