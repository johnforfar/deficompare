import { TemplateModel } from "./TemplateModel";

test("inits without crashing", () => {
  const subject = new TemplateModel();
  expect(subject).toBeDefined();
});
