import React from "react";
import { act, renderHook } from "@testing-library/react-hooks";
import useNivoTheme from "./useNivoTheme";

describe("useHookTemplate", () => {
  test("calls hook without crashing", () => {
    const { result } = renderHook(() => useNivoTheme());
  });
});
