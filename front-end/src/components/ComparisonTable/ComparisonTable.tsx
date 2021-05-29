import React, {useMemo} from "react";
import "../../themes/ReactTable.scss"
import "./styles.scss";
import {useTable} from 'react-table'
import {ExchangeMetricModel} from '../../models/ExchangeMetricModel/ExchangeMetricModel';
import {srmExchangeMetricsSample, uniExchangeMetricsSample} from '../../sampleData';
import last from "lodash/last";

type ContainerProps = {};

const ComparisonTable = (props: ContainerProps) => {
    const serumMetics = srmExchangeMetricsSample.map((metric) => {
        return new ExchangeMetricModel(metric, 'Serum Exchange')
    })
    const uniswapMetics = uniExchangeMetricsSample.map((metric) => {
        return new ExchangeMetricModel(metric, 'Uniswap Exchange')
    })

    const testingData = ExchangeMetricModel.getLatestExchangeMetric(serumMetics)

    const data = useMemo(
        () => [
            ExchangeMetricModel.getLatestExchangeMetric(serumMetics),
            ExchangeMetricModel.getLatestExchangeMetric(uniswapMetics),
        ],
        []
    )


    const testingColumns = ExchangeMetricModel.getAllTableHeadings()
    console.log({testingData, testingColumns})

    const columns = useMemo(
        () => [
        ...ExchangeMetricModel.getAllTableHeadings(),

        ],
        []
    )

    // @ts-ignore
    const tableInstance = useTable({columns, data})

    const {
        getTableProps,
        getTableBodyProps,
        headerGroups,
        rows,
        prepareRow,
    } = tableInstance

    return (
        // apply the table props
        <table {...getTableProps()} className={'ReactTable'}>
            <thead>
            {// Loop over the header rows
                headerGroups.map(headerGroup => (
                    // Apply the header row props
                    <tr {...headerGroup.getHeaderGroupProps()}>
                        {// Loop over the headers in each row
                            headerGroup.headers.map(column => (
                                // Apply the header cell props
                                <th {...column.getHeaderProps()}>
                                    {// Render the header
                                        column.render('Header')}
                                </th>
                            ))}
                    </tr>
                ))}
            </thead>
            {/* Apply the table body props */}
            <tbody {...getTableBodyProps()}>
            {// Loop over the table rows
                rows.map(row => {
                    // Prepare the row for display
                    prepareRow(row)
                    return (
                        // Apply the row props
                        <tr {...row.getRowProps()}>
                            {// Loop over the rows cells
                                row.cells.map(cell => {
                                    // Apply the cell props
                                    return (
                                        <td {...cell.getCellProps()}>
                                            {// Render the cell contents
                                                cell.render('Cell')}
                                        </td>
                                    )
                                })}
                        </tr>
                    )
                })}
            </tbody>
        </table>

    )

};

export default ComparisonTable;
