import React from "react";
import { MemoryRouter, Redirect, Route, Router } from "react-router-dom";
import { render } from "@testing-library/react";
import TemplatePage from "./TemplatePage";

test("renders without crashing", () => {
  const { baseElement } = render(
    <MemoryRouter initialEntries={["/test"]}>
      <TemplatePage />
    </MemoryRouter>
  );
  expect(baseElement).toBeDefined();
});
