# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is the **ViTA Design System** - a comprehensive design system built on Material Design 3 principles for modern web and mobile applications. It provides design tokens, components, and guidelines for the ViTA Flutter mobile application and web interfaces.

## Development Commands

### Local Development
```bash
# Start local development server (serves index.html)
npm start
# or
npm run serve

# Open interactive UI Kit documentation
npm run demo
```

### Dependencies
- **Node.js**: >= 14.0.0 required
- **Python 3**: Required for the built-in HTTP server
- No build process or package dependencies - this is a pure CSS design system

## Architecture & File Structure

### Core Files
- **`DESIGN_TOKENS.css`** - Complete CSS design token system with light/dark themes
- **`index.html`** - Interactive UI Kit demonstrating all components
- **`FIGMA_DESIGN_TOKENS.json`** - Design tokens in Figma-compatible format
- **`README.md`** - Complete documentation and usage guide
- **`GETTING_STARTED.md`** - Quick start guide for developers

### Design System Structure
This is a **pure CSS design system** using CSS custom properties (variables). No preprocessing, build tools, or frameworks required.

**Key Design Principles:**
- Material Design 3 foundation
- Light/dark theme support via `data-theme` attribute
- Responsive design with mobile-first approach
- WCAG 2.1 AA accessibility compliance
- CSS custom properties for all design tokens

### Theme Implementation
- **Light theme**: Default (`:root` variables)
- **Dark theme**: Activated via `[data-theme="dark"]` attribute on `<html>`
- **System preference**: Auto-detection available via CSS media queries

### Component Categories
- Typography (Poppins for display, Heebo for body)
- Color system (brand, surface, semantic, functional)
- Spacing (4px base grid: 4px, 8px, 12px, 16px, 24px, 32px)
- Components (buttons, inputs, badges, cards, progress, grid)

## Usage Notes

### Theme Switching
Use JavaScript to toggle themes:
```javascript
document.documentElement.setAttribute('data-theme', 'dark'); // or 'light'
```

### Required External Dependencies
```html
<!-- Google Fonts -->
<link href="https://fonts.googleapis.com/css2?family=Heebo:wght@400;500;600;700&family=Poppins:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">

<!-- Material Icons (optional) -->
<link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
```

### CSS Class Naming Convention
- Prefix: `vita-` for all design system classes
- Categories: `vita-button`, `vita-text-*`, `vita-container`, `vita-card`, etc.
- Variants: `vita-button-primary`, `vita-text-headline-large`, etc.

## Development Workflow

1. **Design Changes**: Modify `DESIGN_TOKENS.css` design tokens
2. **Component Updates**: Update styles in `DESIGN_TOKENS.css` and test in `index.html`
3. **Documentation**: Update `README.md` and/or `GETTING_STARTED.md`
4. **Testing**: Test in both light and dark themes, verify responsive behavior
5. **Figma Sync**: Update `FIGMA_DESIGN_TOKENS.json` if design tokens change

## Integration Notes

- **Web Projects**: Import `DESIGN_TOKENS.css` and use CSS classes
- **Flutter Projects**: Reference design tokens for consistency
- **Figma**: Import `FIGMA_DESIGN_TOKENS.json` using design token plugins
- **Frameworks**: Compatible with React, Vue, Angular, or vanilla HTML/CSS

## Quality Standards

- All color combinations must meet WCAG 2.1 AA contrast ratios
- Components must work in both light and dark themes
- Responsive behavior required for all components
- Test with screen readers and keyboard navigation
- Follow Material Design 3 guidelines