// @ts-check
import { defineConfig } from 'astro/config';
import tailwindcss from "@tailwindcss/vite";
import preact from "@astrojs/preact";
import sitemap from "@astrojs/sitemap";
import icon from "astro-icon";

// https://astro.build/config
export default defineConfig({
  // The full URL of your GitHub Pages site
  site: "https://ram-devopss.github.io/React_Portfolio", 

  // Base path for GitHub Pages (repository name)
  base: "/React_Portfolio/",

  integrations: [
    preact(),
    icon(),
    sitemap({
      filter: (page) =>
        !page.includes("/blog/tags") &&
        !page.includes("/blog/techs"),
    }),
  ],

  vite: {
    plugins: [tailwindcss()],
  },

  markdown: {
    shikiConfig: {
      theme: "github-dark",
    },
  },

  // Optional: generate relative paths for all assets (safer for GitHub Pages)
  build: {
    site: "https://ram-devopss.github.io/React_Portfolio",
    assets: "assets",
  },
});
