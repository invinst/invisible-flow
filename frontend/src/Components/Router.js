import React from 'react';

import { BrowserRouter, Route, Switch } from 'react-router-dom';

import App from '../App'
import ScrapeStatus from "./ScrapeStatus";

const Router = () => (
        <BrowserRouter>
            <Switch>
                <Route exact path="/" component={App} />
                <Route path="/scrapeStatus" component={ScrapeStatus} />
            </Switch>
        </BrowserRouter>
    );

export default Router;