import logo from './logo.svg';
import './App.css';
import { BrowserRouter, Route, Switch } from 'react-router-dom';
import CustomerItinerary from './models/CustomItinerary';
import Home from './models/Home';

function App() {
  return (
    <BrowserRouter>
      <Route path='/'>
        <Home></Home>
      </Route>
      <Route path='/itinerary'>
        <CustomerItinerary></CustomerItinerary>
      </Route>
    </BrowserRouter>
  );
}

export default App;
