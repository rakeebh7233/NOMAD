import './App.css';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import { useState } from 'react';
import BeginItinerary from './models/BeginItinerary';
import Home from './models/Home';
import NavBar from './shared/NavBar';
import UserProfile from './models/UserProfile'
import CustomerItinerary from './models/CustomerItinerary';
import Login from './models/Login';

function App() {
  const [isLoginVisible, setIsLoginVisible] = useState(false);

  const handleLoginClick = () => {
    setIsLoginVisible(!isLoginVisible);
  }

  return (
    <div>
      <NavBar handleLoginClick={handleLoginClick} />
      <Login isLoginVisible={isLoginVisible} />

      <Router>
        <Routes>
          <Route path='/' exact element={<Home/>}/>
          <Route path='/beginitinerary' exact element={<BeginItinerary/>}/>
          <Route path='/userprofile' exact element={<UserProfile/>}/>
          <Route path='/itinerary' exact element={<CustomerItinerary/>}/>
        </Routes>
      </Router>

    </div> 
  );
}

export default App;
