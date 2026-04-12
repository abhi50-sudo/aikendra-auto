import { defineConfig } from 'vite';

import { cloudflare } from "@cloudflare/vite-plugin";

export default defineConfig({
  plugins: [cloudflare()],
  // SPA fallback — serve index.html for all routes
  appType: 'spa',
  server: {
    port: 3000,
    open: true,
  },
  build: {
    outDir: 'dist',
  },
});