import {TokenMetricDB} from '../../sampleData';
import {Serie} from '@nivo/line';

export const AVG_TX_PRICE_FIELD = 'avgTxPrice';
export const COIN_PRICE_FIELD = 'currentCoinPrice';
export const AVG_TX_TIME_FIELD = 'avgTxTime';
export const LAST_BLOCK_TIME_FIELD = 'lastBlockTime';
export const AVG_GAS_PRICE_FIELD = 'avgGasPrice';
export type TokenMetricField =
    typeof AVG_TX_PRICE_FIELD
    | typeof COIN_PRICE_FIELD
    | typeof AVG_TX_TIME_FIELD
    | typeof LAST_BLOCK_TIME_FIELD
    | typeof AVG_GAS_PRICE_FIELD;

export type TokenMetric = {
    id: number;
    name: string;
    datetime: string;
    currentCoinPrice: number;
    avgGasPrice: number;
    avgTxTime: number | null;
    avgTxPrice: number;
    lastBlockTime: number | null;
}

export class TokenMetricModel {
    private modelData: TokenMetricDB;
    private name: string;

    constructor(modelData: TokenMetricDB, name: string) {
        this.modelData = modelData;
        this.name = name;
    }

    toObject(): TokenMetric {
        return {
            id: this.modelData.id,
            name: this.name,
            datetime: this.modelData.datetime,
            currentCoinPrice: this.modelData.current_coin_price,
            avgGasPrice: this.modelData.avg_gas_price,
            avgTxTime: this.modelData.avg_tx_time,
            avgTxPrice: this.modelData.avg_tx_price,
            lastBlockTime: this.modelData.last_block_time,
        }
    }

    static getAvgTxFeeData(tokenMetrics: TokenMetricModel [], tokenType: TokenMetricField): Serie {
        const tokenMetric = tokenMetrics[0]
        const data = tokenMetrics.map((metric, index) => {
            const date = new Date(metric.modelData.datetime);
            return {
                x: date,
                y: metric.toObject()[tokenType]
            }
        })
        const lineData = {id: tokenMetric.name, data}
        console.log({lineData})
        return lineData;
    }
}
