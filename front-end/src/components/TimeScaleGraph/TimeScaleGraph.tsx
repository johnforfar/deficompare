import React, {Component, useEffect, useState} from "react";
import "./styles.scss";
import {Line} from '@nivo/line'
import useNivoTheme from '../../hooks/useNivoTheme/useNivoTheme';
import {TokenMetricModel} from '../../models/TokenMetricModel/TokenMetricModel';
import {ethTokenMetricsSample} from '../../sampleData';
import moment from 'moment';
import range from 'lodash/range'
import last from 'lodash/last'

import { timeFormat } from 'd3-time-format'
import * as time from 'd3-time'

type ContainerProps = {};

const getRequiredDateFormat = (timeStamp: string, format = "MM-DD-YYYY") => {
    return moment(timeStamp).format(format);
};

// const TimeScaleGraph = (props: ContainerProps) => {
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

class TimeScaleGraph extends Component {
    private formatTime: (date: Date) => string;
    private timer: NodeJS.Timeout;
    constructor(props:any) {
        super(props)

        const date = new Date()
        date.setMinutes(0)
        date.setSeconds(0)
        date.setMilliseconds(0)

        this.state = {
            dataA: range(100).map(i => ({
                x: time.timeMinute.offset(date, i * 30),
                y: 10 + Math.round(Math.random() * 20),
            })),
            dataB: range(100).map(i => ({
                x: time.timeMinute.offset(date, i * 30),
                y: 30 + Math.round(Math.random() * 20),
            })),
            dataC: range(100).map(i => ({
                x: time.timeMinute.offset(date, i * 30),
                y: 60 + Math.round(Math.random() * 20),
            })),
        }
        this.timer = setInterval(this.next, 100)

        this.formatTime = timeFormat('%Y %b %d')
    }

    componentDidMount() {
    }

    componentWillUnmount() {
        clearInterval(this.timer)
    }

    next = () => {
        // @ts-ignore
        const dataA = this.state.dataA.slice(1)
        dataA.push({
        // @ts-ignore
            x: time.timeMinute.offset(last(dataA).x, 30),
            y: 10 + Math.round(Math.random() * 20),
        })
        // @ts-ignore
        const dataB = this.state.dataB.slice(1)
        dataB.push({
        // @ts-ignore
            x: time.timeMinute.offset(last(dataB).x, 30),
            y: 30 + Math.round(Math.random() * 20),
        })
        // @ts-ignore
        const dataC = this.state.dataC.slice(1)
        dataC.push({
        // @ts-ignore
            x: time.timeMinute.offset(last(dataC).x, 30),
            y: 60 + Math.round(Math.random() * 20),
        })

        this.setState({ dataA, dataB, dataC })
    }

    render() {
        // @ts-ignore
        const { dataA, dataB, dataC } = this.state

        //
        return (
            <Line
                {...commonProperties}
                margin={{ top: 30, right: 50, bottom: 60, left: 50 }}
                data={[
                    { id: 'A', data: dataA },
                    { id: 'B', data: dataB },
                    { id: 'C', data: dataC },
                ]}
                xScale={{ type: 'time', format: 'native' }}
                yScale={{ type: 'linear', max: 100 }}
                axisTop={{
                    format: '%H:%M',
                    tickValues: 'every 4 hours',
                }}
                axisBottom={{
                    format: '%H:%M',
                    tickValues: 'every 4 hours',
                    //@ts-ignore
                    legend: `${this.formatTime(dataA[0].x)} ——— ${this.formatTime(last(dataA).x)}`,
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
                    axis: { ticks: { text: { fontSize: 14 } } },
                    grid: { line: { stroke: '#ddd', strokeDasharray: '1 2' } },
                }}
            />
        )
    }
}



export default TimeScaleGraph;
