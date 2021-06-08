import React, {useState} from "react";
import "./styles.scss";
import ChartTypeSelector from '../ChartTypeSelector/ChartTypeSelector';
import TimeScaleGraph from '../TimeScaleGraph/TimeScaleGraph';
import {TokenMetricField, TokenMetricModel} from '../../models/TokenMetricModel/TokenMetricModel';
import {ethTokenMetricsSample, solTokenMetricsSample} from '../../sampleData';

type ContainerProps = {};

const TokenMetricsComparisonChart = (props: ContainerProps) => {
    const [activeTokenMetric, setActiveTokenMetric] = useState<TokenMetricField>('avgTxPrice')
    const ethMetrics = ethTokenMetricsSample.map((metric) => {
        return new TokenMetricModel(metric, 'Etherium')
    })
    const solMetrics = solTokenMetricsSample.map((metric) => {
        return new TokenMetricModel(metric, 'Solana')
    })
    const data = [TokenMetricModel.getAvgTxFeeData(ethMetrics, activeTokenMetric), TokenMetricModel.getAvgTxFeeData(solMetrics, activeTokenMetric)]

    return <>
        <ChartTypeSelector
            onActiveButtonChange={(activeTokenMetric => setActiveTokenMetric(activeTokenMetric))}></ChartTypeSelector>
        <TimeScaleGraph data={data} activeButton={activeTokenMetric}></TimeScaleGraph>
    </>;
};

export default TokenMetricsComparisonChart;
