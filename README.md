# Zimbabwe Running Show

A Pelican-powered blog for the Zimbabwe running community, using the Evently Bootstrap template.

## About

This website serves as a central hub for runners in Zimbabwe, featuring:
- News and updates about running events
- Training tips and resources
- Community stories and features
- Event announcements

## Setup

### Prerequisites
- Python 3.12+
- pip

### Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Build the site:
```bash
pelican content -s pelicanconf.py
```

Or use the Makefile:
```bash
make html
```

3. Preview the site locally:
```bash
pelican --listen
```

The site will be available at http://localhost:8000

## Deployment

This site is configured for deployment on Netlify:

- Build command: `make publish`
- Publish directory: `output`
- Python version: 3.12

### Blog Subdomain

The site is configured to be deployed as a blog subdomain. See `netlify.toml` for configuration details.

## Content Management

### Adding Blog Posts

Create a new Markdown file in the `content/` directory:

```markdown
Title: Your Post Title
Date: YYYY-MM-DD HH:MM
Category: News|Events|Training
Tags: tag1, tag2, tag3
Slug: your-post-slug
Author: Author Name

Your content here...
```

### Adding Pages

Create a new Markdown file in the `content/pages/` directory with similar front matter.

## Theme

The site uses a custom Pelican theme based on the Evently Bootstrap template. The theme files are located in `themes/evently/`.

## License

- Evently Template: [BootstrapMade](https://bootstrapmade.com/license/)
- Content: Zimbabwe Running Show
