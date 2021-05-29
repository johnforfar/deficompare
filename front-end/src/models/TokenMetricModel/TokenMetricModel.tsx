import {ethTokenMetricsSample, TokenMetricDB} from '../../sampleData';
import {Serie} from '@nivo/line';

export class TokenMetricModel {
    private modelData: TokenMetricDB[];
    private name: string;

    constructor(modelData: TokenMetricDB[], name: string) {
        this.modelData = modelData;
        this.name = name;
    }

    getAvgTxFeeData(): Serie {
        const data = this.modelData.map((metric, index) => {
            const date = new Date(metric.datetime);
            return {
                x: date,
                y: metric.avg_tx_price
            }
        })
        const lineData = {id: this.name, data}
        console.log({lineData})
        return lineData;
    }
}
