# John Bacus Portfolio Website

A modern, responsive portfolio website showcasing the work of John Bacus - designer, builder, and maker of things.

## Overview

This portfolio website was rebuilt from the original Adobe Portfolio site to provide a cleaner, more maintainable, and faster alternative. The site features a modern design with responsive layouts, smooth navigation, and optimized performance.

## Features

- **Responsive Design**: Works seamlessly on desktop, tablet, and mobile devices
- **Modern UI**: Clean, minimalist design with smooth transitions and animations
- **Fast Loading**: Optimized CSS and minimal dependencies for quick page loads
- **Accessible**: Semantic HTML and ARIA labels for better accessibility
- **SEO Optimized**: Proper meta tags and structured content for search engines

## Structure

```
portfolio-site/
├── index.html              # Homepage with portfolio grid
├── about.html              # About/profile page
├── assets/
│   ├── css/
│   │   └── style.css       # Main stylesheet
│   ├── js/
│   │   └── main.js         # JavaScript for navigation and interactions
│   └── images/             # Project images and screenshots
└── projects/               # Individual project pages
    ├── datastructure.html
    ├── skpr.html
    ├── expansive-help-tip.html
    ├── design-foundations.html
    └── ... (other projects)
```

## Portfolio Categories

The portfolio is organized into the following categories:

- **Software Design**: SketchUp Client, SketchUp for Web, LayOut, 3D Warehouse, Trimble Connect
- **Interaction Design**: Expansive Help, Touch Modeling UX Design
- **Product Design**: SKPR (hexapod robot), Pochade Box
- **Furniture Design**: Datastructure
- **Writing**: Deep Design in the age of Generative AI

## Technologies Used

- **HTML5**: Semantic markup for better structure and accessibility
- **CSS3**: Modern CSS with variables, flexbox, and grid layouts
- **JavaScript (Vanilla)**: No frameworks required - lightweight and fast
- **Responsive Design**: Mobile-first approach with media queries

## Local Development

To run this site locally:

1. Clone the repository
2. Navigate to the `portfolio-site` directory
3. Open `index.html` in your web browser

Or use a local server:

```bash
# Using Python 3
python -m http.server 8000

# Using Node.js (http-server)
npx http-server -p 8000
```

Then open `http://localhost:8000` in your browser.

## Deployment

This is a static website that can be deployed to any static hosting service:

- **GitHub Pages**: Push to a `gh-pages` branch
- **Netlify**: Connect your repository and deploy
- **Vercel**: Import your repository and deploy
- **Amazon S3**: Upload files to an S3 bucket configured for static hosting

## Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)
- Mobile browsers (iOS Safari, Chrome Mobile)

## Content Source

Content was extracted from the original portfolio at bacus.org and reorganized for better maintainability and performance.

## License

Copyright © 2024 John Bacus. All rights reserved.

## Contact

- LinkedIn: [jbacus](https://www.linkedin.com/in/jbacus/)
- Medium: [@jbacus](https://medium.com/@jbacus)
- Email: john@bacus.org
