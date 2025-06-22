# Mira Presentation

This is a Reveal.js presentation for Mira, built using Markdown and HTML.

## Setup

The presentation uses CDN-hosted Reveal.js, so you only need to serve these files using a web server.

You can use any simple HTTP server, for example with Python:

```bash
# If you have Python 3
python3 -m http.server

# If you have Python 2
python -m SimpleHTTPServer
```

Then open `http://localhost:8000` in your browser.

## Structure

- `index.html` - The main presentation container
- `slides.md` - The presentation content in Markdown format
- `assets/` - Directory for images and other media files

## Visual Showcase

![Mira Background](assets/mira-bg.png)
![Dashboard Interface](assets/dashboard.png)
![Runthrough Demo](assets/runthrough-interface-.gif)

### Profile Analysis Examples
| Professional Analysis | Vulnerability Assessment |
|-----------------------|--------------------------|
| ![Alex Professional](assets/Alex-pro.png) | ![Alex Vulnerability](assets/Alex-vulnerability.png) |
| ![Diana Professional](assets/Diana-pro.png) | ![Diana Vulnerability](assets/Diana-vulnerability.png) |
| ![Kam Professional](assets/Kam-pro.png) | ![Kam Vulnerability](assets/Kam-vulnerability.png) |

## Notes

- Slides are separated by three newlines (`\n\n\n`)
- Vertical slides are separated by two newlines (`\n\n`)
- Speaker notes start with `Note:` on a new line 