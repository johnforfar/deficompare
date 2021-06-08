import React from "react";
import { render } from "@testing-library/react";
import ComparisonTable from './ComparisonTable';

test("renders without crashing", () => {
  const { baseElement } = render(<ComparisonTable />);
  expect(baseElement).toBeDefined();
});
