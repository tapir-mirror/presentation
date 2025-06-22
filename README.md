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

### Profile Analysis Examples (Static Images)
| Professional Analysis | Vulnerability Assessment |
|-----------------------|--------------------------|
| ![Alex Professional](assets/Alex-pro.png) | ![Alex Vulnerability](assets/Alex-vulnerability.png) |
| ![Diana Professional](assets/Diana-pro.png) | ![Diana Vulnerability](assets/Diana-vulnerability.png) |
| ![Kam Professional](assets/Kam-pro.png) | ![Kam Vulnerability](assets/Kam-vulnerability.png) |

### Profile Analysis Demos (Animated GIFs)

#### Kam's Analysis
| Professional Analysis | Vulnerability Assessment |
|-----------------------|--------------------------|
| ![Kam Professional GIF](assets/kalp.gif) | ![Kam Vulnerability GIF](assets/kalv.gif) |

#### Alex's Analysis  
| Professional Analysis | Vulnerability Assessment |
|-----------------------|--------------------------|
| ![Alex Professional GIF](assets/alexp.gif) | ![Alex Vulnerability GIF](assets/alexv.gif) |

#### Diana's Analysis
| Professional Analysis | Vulnerability Assessment |
|-----------------------|--------------------------|
| ![Diana Professional GIF](assets/dianap.gif) | ![Diana Vulnerability GIF](assets/dianav.gif) |


## Mirastral

![Profile Generation](assets/profile_gen.png)
![MiraStral Demo](assets/mirastral.gif)