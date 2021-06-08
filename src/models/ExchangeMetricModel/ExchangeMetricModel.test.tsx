import { ExchangeMetricModel } from "./ExchangeMetricModel";
import {ExchangeMetricDB} from '../../sampleData';

test("inits without crashing", () => {
  const modelData:ExchangeMetricDB = {
    id:1,
    datetime: new Date().toDateString(),
    current_token_price: 1,
    total_value_locked: 100,
    min_apy: 10,
    max_apy: 10,
    avg_apy: 20,
    swap_cost: 1,
    staking_cost: 5
  }
  const subject = new ExchangeMetricModel(modelData,'test');
  expect(subject).toBeDefined();
});
