import React from "react";
import { act, renderHook } from "@testing-library/react-hooks";
import useHookTemplate from "./useHookTemplate";

describe("useHookTemplate", () => {
  test("calls hook without crashing", () => {
    const { result } = renderHook(() => useHookTemplate());
    //    act(() => {
    //   result.current.incrementStroke();
    // });
  });
});
