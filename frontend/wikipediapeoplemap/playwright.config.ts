import { defineConfig, devices } from '@playwright/test'

// Tests UX : parcours utilisateurs, accessibilité, mobile, résilience et performance.
//   npm run test:ux          -> desktop + mobile, backend simulé (rapide, reproductible)
//   npm run test:ux:live     -> desktop contre le vrai backend Django (127.0.0.1:8000)
//   npm run test:ux:report   -> rapport HTML (captures, résultats axe, mesures)
export default defineConfig({
  testDir: './tests/ux',
  timeout: 60_000,
  expect: { timeout: 15_000 },
  fullyParallel: true,
  reporter: [['list'], ['html', { outputFolder: 'tests/ux/report', open: 'never' }]],
  outputDir: 'tests/ux/results',
  use: {
    baseURL: 'http://localhost:5173',
    locale: 'fr-FR',
    // Position fictive (Paris) pour tester « Me géolocaliser »
    geolocation: { latitude: 48.8566, longitude: 2.3522 },
    permissions: ['geolocation'],
    trace: 'retain-on-failure',
    screenshot: 'only-on-failure',
  },
  webServer: {
    command: 'npm run dev',
    url: 'http://localhost:5173',
    reuseExistingServer: true,
    timeout: 120_000,
  },
  projects: [
    { name: 'desktop', use: { ...devices['Desktop Chrome'], viewport: { width: 1440, height: 900 } } },
    { name: 'mobile', use: { ...devices['Pixel 7'] } },
    {
      name: 'live',
      grep: /@live/,
      timeout: 600_000,
      use: { ...devices['Desktop Chrome'], viewport: { width: 1440, height: 900 } },
    },
  ],
})
