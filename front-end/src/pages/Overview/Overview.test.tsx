import React from "react";
import { MemoryRouter, Redirect, Route, Router } from "react-router-dom";
import { render } from "@testing-library/react";
import Overview from "./Overview";

test("renders without crashing", () => {
  const { baseElement } = render(
    <MemoryRouter initialEntries={["/test"]}>
      <Overview />
    </MemoryRouter>
  );
  expect(baseElement).toBeDefined();
});
