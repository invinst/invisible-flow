import React from 'react';
import { fireEvent, render } from "@testing-library/react";
import StartScrapeButton from './StartScrapeButton';

it("renders without crashing", () => {
  render(<StartScrapeButton />);
});

describe("When StartScrapeButton is clicked", () => {
  it("redirects to scrape status page", () => {
    const windowLocationMock = window.location.assign = jest.fn();
    const { getByText } = render(<StartScrapeButton />);

    fireEvent.click(getByText("Initiate COPA Scrape"))

    expect(windowLocationMock).toBeCalledWith("/scrapeStatus");
  });
});