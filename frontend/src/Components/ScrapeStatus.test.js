import React from 'react';
import ReactDOM from 'react-dom';
import ScrapeStatus from './ScrapeStatus';

it('renders without crashing', () => {
  const div = document.createElement('div');
  ReactDOM.render(<ScrapeStatus />, div);
  ReactDOM.unmountComponentAtNode(div);
});
