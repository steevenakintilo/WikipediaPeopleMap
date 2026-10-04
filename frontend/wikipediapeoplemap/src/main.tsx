import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import { QueryClientProvider } from '@tanstack/react-query'
import { ReactQueryDevtools } from '@tanstack/react-query-devtools'
import { polyfillCountryFlagEmojis } from 'country-flag-emoji-polyfill'
import { ThemeProvider, Toaster, TooltipProvider } from '@steevenakintilo/ui'
import { HelmetProvider } from 'react-helmet-async'
import 'leaflet/dist/leaflet.css'
import './index.css'
import App from './App.tsx'
import { query_client } from './api/query_client.ts'

// Affiche les drapeaux emoji sous Windows (police dédiée, voir index.css)
polyfillCountryFlagEmojis()

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <HelmetProvider>
    <ThemeProvider>
      <QueryClientProvider client={query_client}>
        <TooltipProvider>
          <App />
          <Toaster position="bottom-right" />
        </TooltipProvider>
        <ReactQueryDevtools buttonPosition="bottom-right" />
      </QueryClientProvider>
    </ThemeProvider>
    </HelmetProvider>
  </StrictMode>,
)
