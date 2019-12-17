import React from 'react';
import ReactDOM from 'react-dom';
import { render, fireEvent } from "@testing-library/react";
import StartScrapeButton from './StartScrapeButton';

it("renders without crashing", () => {
  const div = document.createElement("div");
  ReactDOM.render(<StartScrapeButton />, div);
  ReactDOM.unmountComponentAtNode(div);
});

describe("When StartScrapeButton is clicked", () => {
    it("redirects to scrape status page", () => {
    const windowLocationMock = window.location.assign = jest.fn();
    const { getByTestId } = render(<StartScrapeButton/>);
    fireEvent.click(getByTestId("startScrape"));
    expect(windowLocationMock).toBeCalledWith("/scrapeStatus");
  });
});