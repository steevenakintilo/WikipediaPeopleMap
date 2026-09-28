import './App.css';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import WorldMap from './pages/worldmap';
import HomePage from './pages/home';
import Statistics from "./pages/statistics";
import QjisMap from './pages/qjis_map';
import About from './pages/about';
import OtherStatistics from './pages/other_statistics'

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route index element={<HomePage />}/> 
        <Route path="/WorldMap" element={<WorldMap />} />
        <Route path="/Home" element={<HomePage />} />
        <Route path="/Statistics" element={<Statistics />} />
        <Route path="/Qjis" element={<QjisMap />} />
        <Route path="/About" element={<About />} />
        <Route path="/OtherStatistics" element={<OtherStatistics />} />
         
                
        {/* <Route path="/Search/:search_query" element={<Search />} /> */}
        
        
        {/* /Profile/"+currentUsername */}

      </Routes>
    </BrowserRouter>
  );
}

export default App;

