import './App.css';
import { lazy } from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import SiteLayout from './components/site_layout';
import { Analytics } from '@vercel/analytics/react';

// Chaque page est téléchargée seulement quand on y va (la carte et les graphiques sont lourds)
const WorldMap = lazy(() => import('./pages/worldmap'));
const HomePage = lazy(() => import('./pages/home'));
const Statistics = lazy(() => import("./pages/statistics"));
const QjisMap = lazy(() => import('./pages/qjis_map'));
const About = lazy(() => import('./pages/about'));
const OtherStatistics = lazy(() => import('./pages/other_statistics'));

function App() {
  return (
    <BrowserRouter>
      <Routes>
        {/* Toutes les pages partagent l'en-tête et la navigation */}
        <Route element={<SiteLayout />}>
          <Route index element={<HomePage />}/>
          <Route path="/WorldMap" element={<WorldMap />} />
          <Route path="/Home" element={<HomePage />} />
          <Route path="/Statistics" element={<Statistics />} />
          <Route path="/Qjis" element={<QjisMap />} />
          <Route path="/About" element={<About />} />
          <Route path="/OtherStatistics" element={<OtherStatistics />} />
          <Route path="*" element={<HomePage/>}/>
        </Route>


        {/* <Route path="/Search/:search_query" element={<Search />} /> */}


        {/* /Profile/"+currentUsername */}

      </Routes>
      <Analytics />
    </BrowserRouter>
  );
}

export default App;

