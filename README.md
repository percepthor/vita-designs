# ViTA Design System

A comprehensive design system built on Material Design 3 principles for modern web and mobile applications.

## 🎨 Overview

The ViTA Design System provides a complete set of design tokens, components, and guidelines to create consistent, accessible, and beautiful user interfaces. Built with Material Design 3 foundations, it includes light and dark theme support, responsive components, and comprehensive documentation.

## 📁 Contents

- **`index.html`** - Interactive UI Kit demonstrating all components and design tokens
- **`DESIGN_TOKENS.css`** - Complete CSS design tokens with light/dark theme support
- **`FIGMA_DESIGN_TOKENS.json`** - Figma-compatible design tokens for design handoff
- **`README.md`** - This documentation

## 🚀 Quick Start

### Web Implementation

1. **Include the CSS file** in your HTML:
```html
<link rel="stylesheet" href="./DESIGN_TOKENS.css">
<link href="https://fonts.googleapis.com/css2?family=Heebo:wght@400;500;600;700&family=Poppins:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
```

2. **Apply theme support** to your HTML:
```html
<html data-theme="light">  <!-- or data-theme="dark" -->
```

3. **Use design tokens** in your CSS:
```css
.my-component {
  background-color: var(--vita-color-surface-container);
  color: var(--vita-color-text-on-surface);
  padding: var(--vita-spacing-4);
  border-radius: var(--vita-border-radius-md);
}
```

### Figma Implementation

Import `FIGMA_DESIGN_TOKENS.json` into your Figma project using design token plugins like:
- Figma Tokens
- Style Dictionary
- Design Tokens

## 🎨 Design Principles

### Material Design 3 Foundation
- **Dynamic Color**: Adaptive color system that works with user preferences
- **Typography Scale**: Systematic text styles based on Poppins and Heebo fonts
- **Motion**: Purposeful animations with consistent timing
- **Accessibility**: WCAG 2.1 AA compliance built-in

### Brand Identity
- **Primary Color**: Deep blue (#003965) representing trust and reliability
- **Typography**: Poppins for headings, Heebo for body text
- **Spacing**: 4px base grid for consistent rhythm
- **Accessibility**: High contrast ratios and semantic markup

## 🌈 Color System

### Brand Colors
```css
--vita-color-brand-primary: #003965;        /* Primary brand color */
--vita-color-brand-secondary: #33445a;      /* Secondary brand color */
--vita-color-brand-tertiary: #50245e;       /* Accent color */
```

### Surface Colors
```css
--vita-color-surface-background: #f9f9fe;   /* Main background */
--vita-color-surface-container: #ededf3;    /* Container backgrounds */
--vita-color-surface-variant: #dee2ed;      /* Alternative surfaces */
```

### Semantic Colors
```css
--vita-color-semantic-error: #8c0009;       /* Error states */
--vita-color-semantic-success: #4caf50;     /* Success states */
--vita-color-semantic-warning: #ff9800;     /* Warning states */
--vita-color-semantic-info: #2196f3;        /* Information states */
```

### Dark Theme
Automatically switches when `data-theme="dark"` is applied:
- Inverted surface hierarchy
- Adjusted contrast ratios
- Maintained brand recognition

## 📝 Typography

### Font Families
- **Display Font**: Poppins (headings, labels, buttons)
- **Body Font**: Heebo (paragraphs, long-form text)

### Text Styles

#### Display Styles
```css
.vita-text-display-large    /* 57px, 900 weight - Hero text */
.vita-text-display-medium   /* 45px, 800 weight - Section headers */
.vita-text-display-small    /* 36px, 700 weight - Page titles */
```

#### Headline Styles
```css
.vita-text-headline-large   /* 32px, 600 weight - Major sections */
.vita-text-headline-medium  /* 28px, 600 weight - Sub-sections */
.vita-text-headline-small   /* 24px, 600 weight - Card titles */
```

#### Body Styles
```css
.vita-text-body-large      /* 16px, 400 weight - Primary content */
.vita-text-body-medium     /* 14px, 400 weight - Secondary content */
.vita-text-body-small      /* 12px, 400 weight - Auxiliary text */
```

#### Label Styles
```css
.vita-text-label-large     /* 14px, 500 weight - Button text */
.vita-text-label-medium    /* 12px, 500 weight - Form labels */
.vita-text-label-small     /* 11px, 500 weight - Small labels */
```

## 📏 Spacing System

Based on a 4px grid for consistent rhythm:

```css
--vita-spacing-1: 4px;    /* Micro spacing */
--vita-spacing-2: 8px;    /* Small spacing */
--vita-spacing-3: 12px;   /* Compact spacing */
--vita-spacing-4: 16px;   /* Standard spacing */
--vita-spacing-6: 24px;   /* Wide spacing */
--vita-spacing-8: 32px;   /* Major sections */
```

## 🔘 Components

### Buttons

#### Types
```html
<button class="vita-button vita-button-primary">Primary</button>
<button class="vita-button vita-button-secondary">Secondary</button>
<button class="vita-button vita-button-edit">Edit Action</button>
<button class="vita-button vita-button-delete">Delete Action</button>
```

#### Modifiers
```html
<button class="vita-button vita-button-primary vita-button-action">Fixed Width</button>
```

### Form Inputs

```html
<div class="demo-input-group">
  <label class="vita-input-label">Input Label</label>
  <input type="text" class="vita-input" placeholder="Enter value">
</div>
```

#### States
- **Default**: Standard input appearance
- **Focus**: Primary color border with increased width
- **Error**: Error color border with `.error` class
- **Disabled**: Reduced opacity with `disabled` attribute

### Status Badges

```html
<span class="vita-status-badge vita-status-badge-success">Success</span>
<span class="vita-status-badge vita-status-badge-error">Error</span>
<span class="vita-status-badge vita-status-badge-warning">Warning</span>
```

### Cards

```html
<div class="vita-card">
  <h3>Card Title</h3>
  <p>Card content goes here...</p>
</div>
```

### Progress Indicators

#### Linear Progress
```html
<div class="vita-progress-linear">
  <div class="vita-progress-fill" style="width: 60%;"></div>
</div>
```

### Layout Utilities

#### Containers
```html
<div class="vita-container">Standard container</div>
<div class="vita-container-content">Content container</div>
<div class="vita-container-responsive">Responsive container</div>
```

#### Grid System
```html
<div class="grid grid-2">  <!-- 2 columns -->
<div class="grid grid-3">  <!-- 3 columns -->
<div class="grid grid-4">  <!-- 4 columns -->
```

## 🌙 Theme Implementation

### JavaScript Theme Toggle
```javascript
function toggleTheme() {
  const html = document.documentElement;
  const currentTheme = html.getAttribute('data-theme');
  
  if (currentTheme === 'dark') {
    html.setAttribute('data-theme', 'light');
  } else {
    html.setAttribute('data-theme', 'dark');
  }
}
```

### Automatic Theme Detection
```javascript
// Auto-detect system preference
if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
  document.documentElement.setAttribute('data-theme', 'dark');
} else {
  document.documentElement.setAttribute('data-theme', 'light');
}
```

## 📱 Responsive Design

### Breakpoints
```css
/* Mobile-first approach */
@media (max-width: 768px) {
  .grid-2, .grid-3, .grid-4 {
    grid-template-columns: 1fr;
  }
}

@media (max-width: 480px) {
  .nav-tabs {
    flex-wrap: wrap;
  }
}
```

### Container Sizes
- **Mobile**: Full width with 16px padding
- **Tablet**: 92% width with auto margins
- **Desktop**: 95% width with max-width 1200px

## ♿ Accessibility

### Color Contrast
- **AA Compliance**: All color combinations meet WCAG 2.1 AA standards
- **Text on Background**: Minimum 4.5:1 contrast ratio
- **Large Text**: Minimum 3:1 contrast ratio

### Focus Management
```css
.vita-button:focus {
  outline: 2px solid var(--vita-color-brand-primary);
  outline-offset: 2px;
}
```

### Semantic Markup
- Proper heading hierarchy (h1-h6)
- ARIA labels where appropriate
- Semantic HTML elements (nav, main, section, article)

### Screen Reader Support
- Descriptive alt text for images
- Proper form labels
- Status announcements for dynamic content

## 🔧 Customization

### Custom Properties
Override design tokens by redefining CSS custom properties:

```css
:root {
  --vita-color-brand-primary: #your-color;
  --vita-spacing-4: 20px;
  --vita-border-radius-md: 8px;
}
```

### Component Variations
Create component variations using existing tokens:

```css
.my-custom-button {
  background-color: var(--vita-color-semantic-info);
  color: white;
  padding: var(--vita-spacing-3) var(--vita-spacing-6);
  border-radius: var(--vita-border-radius-sm);
  font-family: var(--vita-font-family-display);
}
```

## 📋 Use Cases

### ViTA Application Examples
- **Field Data Collection**: Photo capture, GPS tracking, sensor data
- **Process Management**: Workflow automation, quality checkpoints
- **AI Analysis**: ML-powered detection, confidence scoring

### Universal Applications
- **Enterprise Resource Planning**: Complex dashboards, data tables
- **Healthcare**: Patient forms, critical alerts, secure input
- **Education**: Student portals, progress tracking, assessments
- **Inventory**: Stock management, barcode scanning, location tags
- **Business Intelligence**: Analytics dashboards, data visualization
- **Customer Support**: Ticket management, chat interfaces, priority handling

## 🛠️ Development Guidelines

### File Organization
```
your-project/
├── assets/
│   ├── css/
│   │   └── vita-design-tokens.css
│   └── fonts/
├── components/
│   ├── buttons/
│   ├── forms/
│   └── cards/
└── pages/
```

### CSS Architecture
1. **Import design tokens first**
2. **Use CSS custom properties for theming**
3. **Follow BEM methodology for custom components**
4. **Maintain cascade order**: tokens → base → components → utilities

### Performance Considerations
- **Font Loading**: Use `font-display: swap` for custom fonts
- **CSS Optimization**: Remove unused tokens in production
- **Theme Switching**: Use CSS custom properties for instant theme changes
- **Bundle Size**: Import only needed components

## 🚀 Advanced Usage

### Build Tools Integration

#### Webpack
```javascript
// webpack.config.js
module.exports = {
  module: {
    rules: [
      {
        test: /\.css$/,
        use: ['style-loader', 'css-loader', 'postcss-loader']
      }
    ]
  }
};
```

#### PostCSS
```javascript
// postcss.config.js
module.exports = {
  plugins: [
    require('autoprefixer'),
    require('cssnano')
  ]
};
```

### Framework Integration

#### React
```jsx
import './vita-design-tokens.css';

function MyComponent() {
  return (
    <div className="vita-card">
      <h3 className="vita-text-headline-small">React Component</h3>
      <p className="vita-text-body-medium">Using ViTA design tokens</p>
    </div>
  );
}
```

#### Vue.js
```vue
<template>
  <div class="vita-card">
    <h3 class="vita-text-headline-small">Vue Component</h3>
    <p class="vita-text-body-medium">Using ViTA design tokens</p>
  </div>
</template>

<style>
@import './vita-design-tokens.css';
</style>
```

## 📚 Resources

### Design Tools
- **Figma**: Import FIGMA_DESIGN_TOKENS.json for design consistency
- **Sketch**: Convert tokens using Style Dictionary
- **Adobe XD**: Use design tokens plugins

### Development Tools
- **VS Code**: CSS custom properties IntelliSense
- **Chrome DevTools**: CSS custom properties debugging
- **Lighthouse**: Accessibility and performance auditing

### Learning Resources
- [Material Design 3 Guidelines](https://m3.material.io/)
- [WCAG 2.1 Accessibility Guidelines](https://www.w3.org/WAI/WCAG21/)
- [CSS Custom Properties MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/Using_CSS_custom_properties)

## 🤝 Contributing

### Design Contributions
1. Follow Material Design 3 principles
2. Maintain accessibility standards
3. Test in both light and dark themes
4. Document new components

### Code Contributions
1. Use existing design tokens
2. Follow CSS naming conventions
3. Include responsive considerations
4. Add accessibility features

## 📄 License

This design system is part of the ViTA project by Percepthor. For licensing information, please contact the development team.

## 🔄 Version History

### v1.0.0
- Initial release with complete design token system
- Light and dark theme support
- Material Design 3 foundation
- Interactive UI Kit
- Comprehensive documentation

---

Built with ❤️ by the ViTA Design Team