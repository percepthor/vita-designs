# Getting Started with ViTA Design System

## 🚀 Quick Setup (5 minutes)

### Step 1: Download Required Files
Ensure you have these files in your project:
- `DESIGN_TOKENS.css` - The complete design system
- `index.html` - Interactive documentation and examples

### Step 2: Basic HTML Setup
```html
<!DOCTYPE html>
<html lang="en" data-theme="light">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My ViTA App</title>
    
    <!-- ViTA Design System -->
    <link rel="stylesheet" href="./DESIGN_TOKENS.css">
    
    <!-- Required Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Heebo:wght@400;500;600;700&family=Poppins:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
    
    <!-- Material Icons (Optional) -->
    <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
</head>
<body>
    <!-- Your content here -->
</body>
</html>
```

### Step 3: Your First Component
```html
<div class="vita-card">
    <h2 class="vita-text-headline-small">Welcome to ViTA</h2>
    <p class="vita-text-body-medium">This card uses the ViTA design system!</p>
    <button class="vita-button vita-button-primary">Get Started</button>
</div>
```

## 🎨 Essential CSS Classes

### Layout
```html
<!-- Containers -->
<div class="vita-container">Main container</div>
<div class="vita-container-content">Content area</div>

<!-- Grid System -->
<div class="grid grid-2">
    <div>Column 1</div>
    <div>Column 2</div>
</div>
```

### Typography
```html
<!-- Headings -->
<h1 class="vita-text-display-large">Hero Title</h1>
<h2 class="vita-text-headline-large">Section Title</h2>
<h3 class="vita-text-headline-small">Card Title</h3>

<!-- Body Text -->
<p class="vita-text-body-large">Main content text</p>
<p class="vita-text-body-medium">Secondary text</p>
<span class="vita-text-label-medium">Label text</span>
```

### Components
```html
<!-- Buttons -->
<button class="vita-button vita-button-primary">Primary Action</button>
<button class="vita-button vita-button-secondary">Secondary Action</button>

<!-- Form Elements -->
<div class="demo-input-group">
    <label class="vita-input-label">Email Address</label>
    <input type="email" class="vita-input" placeholder="Enter your email">
</div>

<!-- Status Badges -->
<span class="vita-status-badge vita-status-badge-success">Active</span>
<span class="vita-status-badge vita-status-badge-warning">Pending</span>
```

## 🌙 Theme Implementation

### Method 1: JavaScript Toggle
```html
<button onclick="toggleTheme()">
    <span id="theme-icon">dark_mode</span>
    <span id="theme-text">Dark Mode</span>
</button>

<script>
function toggleTheme() {
    const html = document.documentElement;
    const themeIcon = document.getElementById('theme-icon');
    const themeText = document.getElementById('theme-text');
    
    if (html.getAttribute('data-theme') === 'dark') {
        html.setAttribute('data-theme', 'light');
        themeIcon.textContent = 'light_mode';
        themeText.textContent = 'Light Mode';
    } else {
        html.setAttribute('data-theme', 'dark');
        themeIcon.textContent = 'dark_mode';
        themeText.textContent = 'Dark Mode';
    }
}

// Auto-detect system preference
document.addEventListener('DOMContentLoaded', function() {
    if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
        document.documentElement.setAttribute('data-theme', 'dark');
    } else {
        document.documentElement.setAttribute('data-theme', 'light');
    }
});
</script>
```

### Method 2: CSS Media Query Only
```css
/* Automatically follows system preference */
@media (prefers-color-scheme: dark) {
    :root {
        /* Dark theme variables are automatically applied */
    }
}
```

## 📱 Responsive Design

### Mobile-First Approach
```css
/* Mobile styles (default) */
.my-component {
    padding: var(--vita-spacing-4);
    font-size: var(--vita-font-size-base);
}

/* Tablet and up */
@media (min-width: 768px) {
    .my-component {
        padding: var(--vita-spacing-6);
        font-size: var(--vita-font-size-lg);
    }
}

/* Desktop and up */
@media (min-width: 1024px) {
    .my-component {
        padding: var(--vita-spacing-8);
    }
}
```

### Grid Responsiveness
```html
<!-- Automatically stacks on mobile -->
<div class="grid grid-3">
    <div>Item 1</div>
    <div>Item 2</div>
    <div>Item 3</div>
</div>
```

## 🎯 Common Patterns

### Card with Actions
```html
<div class="vita-card">
    <h3 class="vita-text-headline-small">Task Title</h3>
    <p class="vita-text-body-medium">Task description goes here...</p>
    <div style="display: flex; gap: var(--vita-spacing-2); margin-top: var(--vita-spacing-4);">
        <button class="vita-button vita-button-primary">Complete</button>
        <button class="vita-button vita-button-edit">Edit</button>
    </div>
</div>
```

### Form with Validation
```html
<form>
    <div class="demo-input-group">
        <label class="vita-input-label">Required Field *</label>
        <input type="text" class="vita-input" required>
    </div>
    
    <div class="demo-input-group">
        <label class="vita-input-label">Email</label>
        <input type="email" class="vita-input error" value="invalid-email">
        <span class="vita-text-body-small" style="color: var(--vita-color-semantic-error);">
            Please enter a valid email address
        </span>
    </div>
    
    <button type="submit" class="vita-button vita-button-primary">Submit</button>
</form>
```

### Status Dashboard
```html
<div class="grid grid-4">
    <div class="vita-card" style="text-align: center;">
        <h4 class="vita-text-headline-small">Active Tasks</h4>
        <div class="vita-text-display-small" style="color: var(--vita-color-semantic-success);">24</div>
        <span class="vita-status-badge vita-status-badge-success">Running</span>
    </div>
    
    <div class="vita-card" style="text-align: center;">
        <h4 class="vita-text-headline-small">Pending</h4>
        <div class="vita-text-display-small" style="color: var(--vita-color-semantic-warning);">8</div>
        <span class="vita-status-badge vita-status-badge-warning">Review</span>
    </div>
    
    <div class="vita-card" style="text-align: center;">
        <h4 class="vita-text-headline-small">Completed</h4>
        <div class="vita-text-display-small" style="color: var(--vita-color-brand-primary);">156</div>
        <span class="vita-status-badge vita-status-badge-success">Done</span>
    </div>
    
    <div class="vita-card" style="text-align: center;">
        <h4 class="vita-text-headline-small">Errors</h4>
        <div class="vita-text-display-small" style="color: var(--vita-color-semantic-error);">2</div>
        <span class="vita-status-badge vita-status-badge-error">Attention</span>
    </div>
</div>
```

## 🛠️ Customization

### Custom Component Example
```css
.my-custom-card {
    background-color: var(--vita-color-surface-container);
    border-radius: var(--vita-border-radius-lg);
    padding: var(--vita-spacing-6);
    box-shadow: var(--vita-shadow-md);
    border-left: 4px solid var(--vita-color-brand-primary);
    transition: transform 0.2s ease;
}

.my-custom-card:hover {
    transform: translateY(-2px);
    box-shadow: var(--vita-shadow-lg);
}

.my-custom-card h3 {
    color: var(--vita-color-brand-primary);
    margin-bottom: var(--vita-spacing-3);
}
```

### Brand Color Override
```css
:root {
    --vita-color-brand-primary: #your-brand-color;
    --vita-color-brand-secondary: #your-secondary-color;
}

/* Dark theme override */
[data-theme="dark"] {
    --vita-color-brand-primary: #your-dark-theme-primary;
}
```

## 🔍 Debugging Tips

### Check Current Theme
```javascript
console.log('Current theme:', document.documentElement.getAttribute('data-theme'));
```

### Inspect Design Tokens
```javascript
// Get computed value of a design token
const primaryColor = getComputedStyle(document.documentElement)
    .getPropertyValue('--vita-color-brand-primary');
console.log('Primary color:', primaryColor);
```

### CSS Custom Property Support
```javascript
// Check if browser supports CSS custom properties
if (window.CSS && CSS.supports('color', 'var(--fake-var)')) {
    console.log('CSS custom properties supported');
} else {
    console.log('CSS custom properties not supported');
}
```

## ⚠️ Common Issues

### Fonts Not Loading
- Ensure Google Fonts links are in `<head>`
- Check network requests in DevTools
- Verify font-display property for fallbacks

### Theme Not Switching
- Check `data-theme` attribute on `<html>` element
- Verify CSS custom properties are properly defined
- Ensure no conflicting CSS overrides

### Responsive Issues
- Use browser DevTools to test different screen sizes
- Check that grid classes are properly applied
- Verify viewport meta tag is present

### Accessibility Issues
- Test with screen readers
- Check color contrast ratios
- Ensure proper heading hierarchy
- Test keyboard navigation

## 📞 Support

If you encounter issues:
1. Check the interactive documentation in `index.html`
2. Review this getting started guide
3. Inspect CSS custom properties in DevTools
4. Contact the ViTA development team

## ✅ Checklist for New Projects

- [ ] Include `DESIGN_TOKENS.css`
- [ ] Add required Google Fonts
- [ ] Set up theme switching (optional)
- [ ] Test in light and dark modes
- [ ] Verify responsive behavior
- [ ] Test accessibility features
- [ ] Optimize for production

Happy building with ViTA Design System! 🎉