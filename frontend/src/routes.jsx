// routes.jsx
import React from 'react'
import { Route, Switch } from 'react-router-dom'
import App from './App'
import ScrapeStatus from "./Components/ScrapeStatus";


const Routes = () => (
        <Switch>
            <Route exact path="/" component={App} />
            <Route path="/scrapeStatus" component={ScrapeStatus} />
        </Switch>
    );

export default Routes