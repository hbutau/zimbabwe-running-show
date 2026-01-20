# Content Management Guide

## Adding New Blog Posts

1. Create a new markdown file in the `content/` directory
2. Add the required metadata at the top of the file:

```markdown
Title: Your Article Title
Date: YYYY-MM-DD HH:MM
Category: News|Events|Training
Tags: tag1, tag2, tag3
Slug: your-article-slug
Author: Author Name

Your article content here...
```

3. Write your content using Markdown syntax
4. Build the site to see your changes:
   ```bash
   pelican content -s pelicanconf.py
   ```

## Adding New Static Pages

1. Create a new markdown file in the `content/pages/` directory
2. Add the required metadata:

```markdown
Title: Page Title
Date: YYYY-MM-DD
Slug: page-slug

Your page content here...
```

3. Build the site to generate the page

## Markdown Syntax Guide

### Headings
```markdown
# H1
## H2
### H3
```

### Lists
```markdown
- Item 1
- Item 2
- Item 3

1. First item
2. Second item
3. Third item
```

### Links
```markdown
[Link text](https://example.com)
```

### Images
```markdown
![Alt text](path/to/image.jpg)
```

Place images in `content/images/` directory and reference them as:
```markdown
![Alt text]({static}/images/image.jpg)
```

### Emphasis
```markdown
*italic* or _italic_
**bold** or __bold__
***bold and italic***
```

## Building and Previewing

### Development Build
```bash
pelican content -s pelicanconf.py
```

### Preview Locally
```bash
pelican --listen
# Visit http://localhost:8000
```

### Production Build
```bash
make publish
```

## Tips

- Use descriptive slugs for SEO
- Always add relevant tags to articles
- Choose appropriate categories (News, Events, Training)
- Add dates in YYYY-MM-DD format
- Keep article titles concise and descriptive
