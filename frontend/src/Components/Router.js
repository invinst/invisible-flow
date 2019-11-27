import React from 'react';

import { BrowserRouter, Route, Switch } from 'react-router-dom';

import App from '../App'
import ScrapeStatus from "./ScrapeStatus";
import FOIA from "./FOIA";
import Header from './Header';

const Router = () => (
        <BrowserRouter>
            <Header/>
            <Switch>
                <Route exact path="/" component={App} />
                <Route path="/scrapeStatus" component={ScrapeStatus} />
                <Route path="/FOIA" component={FOIA} />
            </Switch>
        </BrowserRouter>
    );

export default Router;