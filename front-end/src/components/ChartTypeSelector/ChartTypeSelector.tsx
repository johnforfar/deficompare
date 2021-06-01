import React from "react";
import "./styles.scss";
import {Button, Stack} from '@chakra-ui/react';
import {FaBeer, FaGasPump} from 'react-icons/fa'
import {BiTime, GiPriceTag, GrMoney, MdAvTimer} from 'react-icons/all';
import useActiveButton from '../../hooks/useActiveButton/useActiveButton';
import {
    AVG_GAS_PRICE_FIELD,
    AVG_TX_PRICE_FIELD,
    AVG_TX_TIME_FIELD,
    COIN_PRICE_FIELD,
    LAST_BLOCK_TIME_FIELD, TokenMetricField
} from '../../models/TokenMetricModel/TokenMetricModel';

type ContainerProps = {
    onActiveButtonChange: (activeButton: TokenMetricField) => void;
};
const buttons: { type: TokenMetricField, label: string, iconEl: React.ReactElement }[] = [
    {
        type: AVG_TX_PRICE_FIELD,
        label: 'Avg Tx Price',
              iconEl: <GiPriceTag/>
    },
    {
        type: AVG_TX_TIME_FIELD,
        label: 'Avg Tx Time',
              iconEl: <BiTime/>

    },
    {
        type: COIN_PRICE_FIELD,
        label: 'Coin Price',
              iconEl: <GrMoney/>

    },
    {
        type: LAST_BLOCK_TIME_FIELD,
        label: 'Last Block Time',
              iconEl: <MdAvTimer/>

    },
    {
        type: AVG_GAS_PRICE_FIELD,
        label: 'Avg Gas Price',
              iconEl: <FaGasPump/>

    },
]

const ChartTypeSelector = (props: ContainerProps) => {


    const {activeButton, handleButtonSelect} = useActiveButton({currentButton: AVG_TX_PRICE_FIELD})
    return <>
        <Stack direction="row" spacing={6} margin={1}>
            {buttons.map((button,index) => {
                return (<Button key={index} leftIcon={button.iconEl}
                                variant={activeButton === button.type ? "solid" : "outline"}
                                onClick={() => {
                                    handleButtonSelect(button.type)
                                    props.onActiveButtonChange(button.type)
                                }}>    {button.label}
                    </Button>
                );
            })}
        </Stack>
    </>;
};

export default ChartTypeSelector;
