import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';

import Routes from './routes.jsx';
import { BrowserRouter, Link } from 'react-router-dom';

ReactDOM.render(
    <BrowserRouter>
        <div>
            <ul>
                <li>
                    <Link to="/">Home</Link>
                </li>
                <li>
                    <Link to="/scrapeStatus">Scraping Status</Link>
                </li>
                <li>
                    <Link to="/tacos">Tacos</Link>
                </li>
            </ul>

            <hr />

            <Routes />
        </div>
    </BrowserRouter>
    , document.getElementById('root'));
