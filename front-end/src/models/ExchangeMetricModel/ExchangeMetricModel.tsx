import {ExchangeMetricDB} from '../../sampleData';

export class ExchangeMetricModel {
    private modelData: ExchangeMetricDB;
    private name: string;

    constructor(modelData: ExchangeMetricDB, name: string) {
        this.modelData = modelData;
        this.name = name;
    }

    static getAllTableHeadings() {
        const headings = [
            {Header: 'Exchange', accessor: 'name'},
            {Header: 'Updated', accessor: 'datetime'},
            {Header: 'Current Token Price', accessor: 'currentTokenPrice'},
            {Header: 'Total Value Locked', accessor: 'totalValueLocked'},
            {Header: 'Min APY', accessor: 'minApy'},
            {Header: 'Avg APY', accessor: 'avgApy'},
            {Header: 'Max APY', accessor: 'maxApy'},
            {Header: 'Swap Cost', accessor: 'swapCost'},
            {Header: 'Staking Cost', accessor: 'stakingCost'},
        ]
        return headings
    }

    toObject() {
        return {
            id: this.modelData.id,
            name: this.name,
            datetime: this.modelData.datetime,
            currentTokenPrice: this.modelData.current_token_price,
            totalValueLocked: this.modelData.total_value_locked,
            minApy: this.modelData.min_apy,
            avgApy: this.modelData.avg_apy,
            maxApy: this.modelData.max_apy,
            swapCost: this.modelData.swap_cost,
            stakingCost: this.modelData.staking_cost,
        }
    }

    static getLatestExchangeMetric(metrics: ExchangeMetricModel []) {
        const metricsSorted = metrics.sort((metric, nextMetric) => {
            if (metric.toObject().datetime > nextMetric.toObject().datetime) {
                return 1
            } else {
                return 0
            }
        })
        if (metricsSorted.length > 0) {
            let latestMetricData = metricsSorted[metricsSorted.length - 1].toObject()
            return latestMetricData;
        }
        return null;
    }
}
