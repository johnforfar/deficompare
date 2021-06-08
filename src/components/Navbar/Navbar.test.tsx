import React from "react";
import { render } from "@testing-library/react";
import Navbar from './Navbar';

test("renders without crashing", () => {
  const { baseElement } = render(<Navbar />);
  expect(baseElement).toBeDefined();
});
