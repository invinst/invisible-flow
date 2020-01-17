import React from 'react';
import { BrowserRouter, Route, Switch } from 'react-router-dom';
import MainPage from './MainPage';
import ScrapeStatus from './ScrapeStatus';
import FOIA from './FOIA';
import Header from './Header';
import Footer from './Footer';

const Router = () => (
  <BrowserRouter>
    <Header/>
    <Switch>
      <Route exact path='/' component={MainPage} />
      <Route path='/scrapeStatus' component={ScrapeStatus} />
      <Route path='/FOIA' component={FOIA} />
    </Switch>
    <Footer/>
  </BrowserRouter>
);

export default Router;
