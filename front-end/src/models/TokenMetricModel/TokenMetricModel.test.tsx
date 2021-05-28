import { TokenMetricModel } from "./TokenMetricModel";

test("inits without crashing", () => {
  const subject = new TokenMetricModel();
  expect(subject).toBeDefined();
});
