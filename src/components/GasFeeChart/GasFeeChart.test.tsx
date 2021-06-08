import React from "react";
import { render } from "@testing-library/react";
import GasFeeChart from './GasFeeChart';

test("renders without crashing", () => {
  const { baseElement } = render(<GasFeeChart />);
  expect(baseElement).toBeDefined();
});
