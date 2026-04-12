import { defineConfig } from 'vite';

export default defineConfig({
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
