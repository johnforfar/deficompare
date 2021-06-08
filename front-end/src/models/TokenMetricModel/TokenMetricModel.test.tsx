import {TokenMetricModel} from "./TokenMetricModel";
import {TokenMetricDB} from '../../sampleData';

test("inits without crashing", () => {
    const modelData: TokenMetricDB = {
        id: 1,
        datetime: new Date().toDateString(),
        current_coin_price: 10,
        avg_gas_price: 12,
        avg_tx_time: 15,
        avg_tx_price: 3,
        last_block_time: 23
    }
    const subject = new TokenMetricModel(modelData, 'test token');
    expect(subject).toBeDefined();
});
