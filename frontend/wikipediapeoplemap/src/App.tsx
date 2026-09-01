import './App.css';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import HomePage from './pages/home';

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route index element={<HomePage />}/> 
        <Route path="/Home" element={<HomePage />} />
        {/* <Route path="/Search/:search_query" element={<Search />} /> */}
        
        
        {/* /Profile/"+currentUsername */}

      </Routes>
    </BrowserRouter>
  );
}

export default App;