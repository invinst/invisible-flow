import React from 'react';
import { fireEvent, render } from "@testing-library/react";
import StartScrapeButton from './StartScrapeButton';

const mockXHR = {
  open: jest.fn(),
  send: jest.fn(),
  status: 200
};

const windowLocationMock = window.location.assign = jest.fn();
window.XMLHttpRequest = jest.fn(() => mockXHR);

it("renders without crashing", () => {
  render(<StartScrapeButton />);
});

describe("When StartScrapeButton is clicked", () => {
  it("redirects to scrape status page and sends HTTP request to backend", () => {
    const { getByText } = render(<StartScrapeButton />);

    fireEvent.click(getByText("Initiate COPA Scrape"))

    expect(windowLocationMock).toBeCalledWith("/scrapeStatus");
    expect(mockXHR.send).toHaveBeenCalled();
  });
});