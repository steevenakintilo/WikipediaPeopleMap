import Home from "./home.tsx"

// Accueil en anglais (/en) : mêmes contenus, mais helmet et langue forcés en anglais pour le référencement
const HomeEnglish = () => <Home route_language="en" />

export default HomeEnglish
