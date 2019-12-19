import React from 'react';
import { unmountComponentAtNode } from 'react-dom';
import { render, fireEvent } from "@testing-library/react";
import '@testing-library/jest-dom/extend-expect'
import { getNodeText, getAllByText, getByTestId } from '@testing-library/dom';
import FOIAUploadForm from './FOIAUploadForm';


let container = null;

beforeEach(() => {
  container = document.createElement("div");
  document.body.appendChild(container);
});

afterEach(() => {
  unmountComponentAtNode(container);
  container.remove();
  container = null;
});

describe("When FOIAUploadForm is submitted", function () {

    it("handles successful response", async function() {
        global.fetch = jest.fn().mockImplementation(() => {
          var p = new Promise((resolve, reject) => {
            resolve({
              ok: true,
              statusText: ''
            });
          });

          return p;
        });

      const { getAllByText, getByTestId} = render(<FOIAUploadForm/>);
      const button = getAllByText("Upload")[0];
      fireEvent.click(button);
      const banner = await getByTestId("resultsBanner");
      //console.log(getNodeText(banner));
      expect(banner).toHaveTextContent("Your file has been successfully uploaded.");
    });

     it("handles error response", async function() {
        global.fetch = jest.fn().mockImplementation(() => {
          var p = new Promise((resolve, reject) => {
            resolve({
              ok: false,
              statusText: 'UNSUPPORTED MEDIA TYPE'
            });
          });

          return p;
        });

      const { getAllByText, getByTestId} = render(<FOIAUploadForm/>);
      const button = getAllByText("Upload")[0];
      fireEvent.click(button);
      const banner = await getByTestId("resultsBanner");
      //console.log(getNodeText(banner));
      expect(banner).toHaveTextContent("Error: UNSUPPORTED MEDIA TYPE. Please resolve the issue and try again.");
    });

});