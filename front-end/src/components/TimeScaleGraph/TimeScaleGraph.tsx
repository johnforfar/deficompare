import React, {Component, useEffect, useState} from "react";
import "./styles.scss";
import {Line} from '@nivo/line'
import useNivoTheme from '../../hooks/useNivoTheme/useNivoTheme';
import {TokenMetricModel} from '../../models/TokenMetricModel/TokenMetricModel';
import {ethTokenMetricsSample} from '../../sampleData';
import moment from 'moment';
import range from 'lodash/range'
import last from 'lodash/last'

import {timeFormat} from 'd3-time-format'
import * as time from 'd3-time'

type ContainerProps = {};

const getRequiredDateFormat = (timeStamp: string, format = "MM-DD-YYYY") => {
    return moment(timeStamp).format(format);
};

const commonProperties = {
    width: 900,
    height: 400,
    margin: {top: 20, right: 20, bottom: 60, left: 80},
    animate: true,
    enableSlices: 'x',
}
//     const {theme} = useNivoTheme()
//     const ethMetricModel = new TokenMetricModel(ethTokenMetricsSample, 'eth')
//     // const data = [ethMetricModel.getGasFeeData()]

const TimeScaleGraph = (props: ContainerProps) => {
    const date = new Date()
    date.setMinutes(0)
    date.setSeconds(0)
    date.setMilliseconds(0)
    const [dataA, setDataA] = useState(range(100).map(i => ({
        x: time.timeMinute.offset(date, i * 30),
        y: 10 + Math.round(Math.random() * 20),
    })))

    const formatTime = timeFormat('%Y %b %d')

    return (
        <Line
            {...commonProperties}
            margin={{top: 30, right: 50, bottom: 60, left: 50}}
            data={[
                {id: 'A', data: dataA},
            ]}
            xScale={{type: 'time', format: 'native'}}
            yScale={{type: 'linear', max: 100}}
            axisTop={{
                format: '%H:%M',
                tickValues: 'every 4 hours',
            }}
            axisBottom={{
                format: '%H:%M',
                tickValues: 'every 4 hours',
                //@ts-ignore
                legend: `${formatTime(dataA[0].x)} ——— ${formatTime(last(dataA).x)}`,
                legendPosition: 'middle',
                legendOffset: 46,
            }}
            axisRight={{}}
            enablePoints={false}
            enableGridX={true}
            curve="monotoneX"
            animate={false}
            motionStiffness={120}
            motionDamping={50}
            isInteractive={false}
            enableSlices={false}
            useMesh={true}
            theme={{
                axis: {ticks: {text: {fontSize: 14}}},
                grid: {line: {stroke: '#ddd', strokeDasharray: '1 2'}},
            }}
        />
    )
}

export default TimeScaleGraph;
