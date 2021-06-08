import React from "react";
import { render } from "@testing-library/react";
import TokenMetricsComparisonChart from './TokenMetricsComparisonChart';

test("renders without crashing", () => {
  const { baseElement } = render(<TokenMetricsComparisonChart />);
  expect(baseElement).toBeDefined();
});
