import React from 'react';
import { unmountComponentAtNode } from 'react-dom';
import { fireEvent, render, waitForDomChange } from '@testing-library/react';
import StartScrapeButton from './StartScrapeButton';

const mockPush = jest.fn();

jest.mock('react-router-dom', () => ({
  useHistory: () => ({
    push: mockPush
  })
}));

const mockRequest = {
  open: jest.fn(),
  send: jest.fn(),
  status: 200
};

window.XMLHttpRequest = jest.fn(() => mockRequest);

let container = null;

beforeEach(() => {
  container = document.createElement('div');
  document.body.appendChild(container);
});

afterEach(() => {
  unmountComponentAtNode(container);
  container.remove();
  container = null;
});

it('renders without crashing', () => {
  render(<StartScrapeButton toggleLoading={jest.fn()} />, container);
});

describe('When StartScrapeButton is clicked', () => {
  it('redirects to scrape status page and sends HTTP request to backend', async () => {
    const { getByText } = render(<StartScrapeButton toggleLoading={jest.fn()} />, container);

    fireEvent.click(getByText('Initiate scrape'));

	waitForDomChange(container).then(() => {
		expect(mockRequest.send).toHaveBeenCalled();
	    expect(mockPush).toBeCalledWith('/scrapeStatus');
    });
  });
});
