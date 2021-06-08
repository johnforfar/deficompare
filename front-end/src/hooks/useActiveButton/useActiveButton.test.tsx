import React from "react";
import { act, renderHook } from "@testing-library/react-hooks";
import useActiveButton from "./useActiveButton";

describe("useHookTemplate", () => {
  test("calls hook without crashing", () => {
    const { result } = renderHook(() => useActiveButton({currentButton: 'test'}));
    //    act(() => {
    //   result.current.incrementStroke();
    // });
  });
});
