import React from 'react';
import { BrowserRouter as Router, Route, Switch} from 'react-router-dom'

//Nav And Footer
import { Nav } from './Components/Partials/nav'

//Compoment Route's
import { About } from './Components/about';
import {Users} from './Components/users'
import { Principal } from './Components/principal';
import { Products } from './Components/products';
import { Footer } from './Components/Partials/footer';

function App() {
  return (
    <div>
      <Router>
        <Nav />
        <Switch>
          <Route path='/about' component={About} />
          <Route path='/products' component={Products} />
          <Route path='/users' component={Users} />
          <Route path='/' component={Principal} />
        </Switch>
        <Footer />
      </Router>
    </div>
  );
}

export default App;
