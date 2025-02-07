# Roo Code Documentation Design System and Styling Conventions

This guide outlines the design system and styling conventions for Roo Code documentation, based on the Just the Docs theme.

## Base Theme Configuration

```yaml
theme: just-the-docs
```

Our documentation uses Just the Docs as the foundation theme, providing consistent navigation and structure.

## Visual Design Elements

### Typography

- **Primary Font**: System fonts for optimal readability
  ```scss
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
  ```
- **Code Font**: Monospace for code blocks and inline code
  ```scss
  font-family: 'Courier New', Courier, monospace;
  ```

### Colors

Define as CSS variables for consistency:
```scss
:root {
  --primary-color: #0f0;         // Primary brand color
  --background-light: #fff;      // Light backgrounds
  --text-primary: #000;          // Primary text
  --text-secondary: #777;        // Secondary text
  --code-background: #000;       // Code block background
  --callout-tip: green;         // Tip callouts
  --callout-note: yellow;       // Note callouts
}
```

### Layout Components

#### Content Cards
```scss
.content-card {
  background: var(--background-light);
  box-shadow: 0 2px 5px rgba(0,0,0,0.1);
  margin-bottom: 2em;
  padding: 1em;
  border-radius: 4px;
}
```

#### Code Blocks
```scss
.code-block {
  font-family: 'Courier New', Courier, monospace;
  background-color: var(--code-background);
  color: var(--primary-color);
  padding: 1em;
  border-radius: 5px;
  margin: 1em 0;
  line-height: 1.1;
}
```

### Callouts

Use callouts for important information:

```yaml
callouts:
  tip:
    title: Tip
    color: var(--callout-tip)
  note:
    title: Note
    color: var(--callout-note)
```

Example usage:
```markdown
{: .tip }
This is a helpful tip for users.

{: .note }
This is an important note about functionality.
```

### Responsive Design

```scss
// Base styles for larger screens
.content {
  max-width: 1200px;
  margin: 0 auto;
}

// Responsive adjustments
@media (max-width: 768px) {
  .content {
    padding: 0 1em;
  }
  
  .code-block {
    padding: 0.5em;
  }
}
```

## Documentation Components

### Navigation

Configure external links in `_config.yml`:
```yaml
nav_external_links:
  - title: "GitHub"
    url: "[REPO_URL]"
  - title: "Support"
    url: "[SUPPORT_URL]"
```

### Page Headers

Standard page header format:
```markdown
---
title: [Page Title]
nav_order: [Number]
description: [Brief description]
---
```

### Content Structure

1. **Main Heading (H1)**
   - One per page
   - Clearly describes the page content

2. **Section Headings (H2)**
   - Major sections of content
   - Keep concise and descriptive

3. **Subsections (H3-H4)**
   - Used for detailed breakdowns
   - Maintain clear hierarchy

### Code Examples

1. **Inline Code**
   - Use single backticks for inline code references
   - Example: `function_name()`

2. **Code Blocks**
   - Use triple backticks with language specification
   ```python
   def example_function():
       return "Hello World"
   ```

### Tables

Use markdown tables for structured data:
```markdown
| Header 1 | Header 2 |
|----------|----------|
| Content  | Content  |
```

## Accessibility Guidelines

- Maintain proper heading hierarchy (H1 > H2 > H3)
- Include alt text for all images
- Use sufficient color contrast
- Provide text alternatives for non-text content

## Best Practices

1. **File Organization**
   - Place documentation in `/docs` directory
   - Use clear, descriptive filenames
   - Maintain consistent directory structure

2. **Image Assets**
   - Store in `/assets` directory
   - Use descriptive filenames
   - Optimize for web use

3. **Markdown Style**
   - Use consistent spacing
   - Include blank lines between sections
   - Follow standard markdown conventions

4. **Version Control**
   - Document significant style changes
   - Maintain changelog
   - Track style guide versions

## Implementation Instructions

1. Copy configuration to `_config.yml`
2. Add custom styles to `_sass/custom/custom.scss`
3. Follow component guidelines for new documentation
4. Use provided templates for consistency

By following these guidelines, we maintain consistent, professional, and accessible documentation across the Roo Code platform.