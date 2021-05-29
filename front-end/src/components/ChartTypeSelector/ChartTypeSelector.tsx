import React from "react";
import "./styles.scss";
import {Button, Stack} from '@chakra-ui/react';
import {FaBeer, FaGasPump} from 'react-icons/fa'
import {BiTime, GiPriceTag, GrMoney, MdAvTimer} from 'react-icons/all';
import useActiveButton from '../../hooks/useActiveButton/useActiveButton';
type ContainerProps = {};

export const AVG_TX_PRICE_FIELD = 'avgTxPrice';
export const COIN_PRICE_FIELD = 'coinPrice';
export const AVG_TX_TIME_FIELD = 'avgTxTime';
export const LAST_BLOCK_TIME_FIELD = 'lastBlockTime';
export const AVG_GAS_PRICE_FIELD = 'avgGasPrice';
export type TokenDataField = typeof AVG_TX_PRICE_FIELD | typeof COIN_PRICE_FIELD | typeof AVG_TX_TIME_FIELD | typeof LAST_BLOCK_TIME_FIELD | typeof AVG_GAS_PRICE_FIELD ;

const ChartTypeSelector = (props: ContainerProps) => {
  const {activeButton, handleButtonSelect} = useActiveButton({currentButton:AVG_TX_PRICE_FIELD})
  return <>
  <Stack direction="row" spacing={4}>
    <Button leftIcon={<GiPriceTag />} colorScheme="teal" variant={activeButton===AVG_TX_PRICE_FIELD?"solid":"outline"} onClick={()=>handleButtonSelect(AVG_TX_PRICE_FIELD)}>
    Avg Tx Price
  </Button>
  <Button leftIcon={<GrMoney />} colorScheme="teal" variant={activeButton===COIN_PRICE_FIELD?"solid":"outline"} onClick={()=>handleButtonSelect(COIN_PRICE_FIELD)}>
    Coin Price
  </Button>
    <Button leftIcon={<BiTime />} colorScheme="teal" variant={activeButton===AVG_TX_TIME_FIELD?"solid":"outline"} onClick={()=>handleButtonSelect(AVG_TX_TIME_FIELD)}>
    Avg Tx Time
  </Button>
    <Button leftIcon={<MdAvTimer />} colorScheme="teal" variant={activeButton===LAST_BLOCK_TIME_FIELD?"solid":"outline"} onClick={()=>handleButtonSelect(LAST_BLOCK_TIME_FIELD)}>
    Last Block Time
  </Button>
  <Button leftIcon={<FaGasPump />} colorScheme="teal" variant={activeButton===AVG_GAS_PRICE_FIELD?"solid":"outline"} onClick={()=>handleButtonSelect(AVG_GAS_PRICE_FIELD)}>
    Avg Gas Price
  </Button>
</Stack>
  </>;
};

export default ChartTypeSelector;
