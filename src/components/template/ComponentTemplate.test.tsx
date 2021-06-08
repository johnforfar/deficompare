import React from "react";
import { render } from "@testing-library/react";
import ComponentTemplate from './ComponentTemplate';

test("renders without crashing", () => {
  const { baseElement } = render(<ComponentTemplate />);
  expect(baseElement).toBeDefined();
});
