## 📁 Project Structure

```bash
└── 📁NeonMint
    └── 📁public
        ├── android-chrome-192x192.png
        ├── android-chrome-512x512.png
        ├── apple-touch-icon.png
        ├── favicon-16x16.png
        ├── favicon-32x32.png
        ├── favicon.ico
        └── 📁images
            ├── 📁posts    # Post images
            └── 📁projects # Project images
        └── site.webmanifest # PWA configuration file
    └── 📁src
        ├── 📁components  # Reusable UI components
        │   ├── 📁blog    # Blog components
        │   ├── 📁layout  # Layout components
        │   ├── 📁portfolio # Portfolio components
        │   └── 📁ui      # UI components
        ├── 📁icons       # Icons (.svg)
        ├── 📁layouts     # Site layouts
        │   ├── Layout.astro           # Main application layout
        │   ├── MarkdownAbout.astro    # About-me page layout
        │   ├── MarkdownPostLayout.astro # Posts page layout
        │   └── ProjectLayout.astro    # Projects page layout
        ├── 📁pages       # Site pages
        │   ├── about-me.md            # About-me page
        │   ├── 📁blog   # All posts page
        │   │   ├── index.astro        # Blog home page
        │   │   ├── 📁posts            # Blog posts
        ├── │   ├── └── index.astro     # All posts page
        │   │   ├── 📁tags             # Blog tags
        │   │   └── 📁techs            # Blog technologies
        │   ├── index.astro            # Home page
        │   ├── 📁portfolio
        │   │   └── 📁projects         # Portfolio projects
        │   ├── robots.txt.ts          # robots.txt configuration
        │   └── rss.xml.js             # RSS configuration
        ├── 📁scripts
        │   └── menu.js                # Menu script
        ├── 📁styles
        │   └── global.css             # Global styles
        └── 📁utils
            └── languages.ts           # Technology tools configuration
    ├── .gitignore
    ├── astro.config.mjs
    ├── package-lock.json
    ├── package.json
    ├── README.md
    └── tsconfig.json
```
### 🎨 Styling

- Use TailwindCSS classes for styling
- Add custom styles in `src/styles/global.css`

### 🧩 Components

- Create reusable components in `src/components`
- Import icons using `astro-icon`

## 🚀 Deployment

The site is configured for deployment on Vercel, but can be deployed to any static hosting service.
\

This project is licensed under the MIT License - see the LICENSE file for details.

# Trigger deploy
