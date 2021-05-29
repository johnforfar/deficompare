import { ExchangeMetricModel } from "./ExchangeMetricModel";

test("inits without crashing", () => {
  const subject = new ExchangeMetricModel();
  expect(subject).toBeDefined();
});
