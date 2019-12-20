import React from 'react';
import ReactDOM from 'react-dom';
import { render } from "@testing-library/react";
import App from './App';

jest.mock('react-router-dom', () => ({
  useHistory: () => ({
    push: jest.fn()
  })
}));

it('renders without crashing', () => {
  const div = document.createElement('div');
  ReactDOM.render(<App />, div);
  ReactDOM.unmountComponentAtNode(div);
});


describe("App goes to status", function () {
  it('App should have scrape button', function () {
    const { getByTestId } = render(<App />);
    const e = getByTestId("startScrape");
    expect(e.tagName).toBe("BUTTON");
  });
});