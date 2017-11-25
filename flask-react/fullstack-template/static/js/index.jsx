import React from 'react'
import ReactDOM from 'react-dom'

import {
    BrowserRouter as Router,
    Route,
    Link,
    Switch
} from 'react-router-dom'

// Components
import App from './App'
import About from './About'
import NoMatch from './NoMatch'

ReactDOM.render(
    <Router>
        <div>
            <ul>
                <li><Link to="/">Home</Link></li>
                <li><Link to="/about">About</Link></li>
                <li><Link to="/no-match">No Match</Link></li>
            </ul>
            <Switch>
                <Route exact path="/" component={App} />
                <Route path="/about" component={About} />
                <Route component={NoMatch} />
            </Switch>
        </div>    
    </Router>, 
    document.getElementById('content')
)