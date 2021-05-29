import {Box, Button, Center, Container, Flex, Heading, Icon, Square, Stack, useColorModeValue} from "@chakra-ui/react";
import {useParams} from "react-router";
import "./styles.scss";
import ComparisonTable from '../../components/ComparisonTable/ComparisonTable';
import React, {useState} from 'react';
import GasFeeChart from '../../components/GasFeeChart/GasFeeChart';
import TimeScaleGraph from '../../components/TimeScaleGraph/TimeScaleGraph';
import ChartTypeSelector from '../../components/ChartTypeSelector/ChartTypeSelector';
import {TokenMetricField} from '../../models/TokenMetricModel/TokenMetricModel';

const Overview = () => {
    const {name} = useParams<{ name: string }>();
    const [activeTokenMetric, setActiveTokenMetric] = useState<TokenMetricField>('avgTxPrice')
    return (

      <Container >
        <Stack
          as={Box}
          textAlign={'center'}
          spacing={{ base: 4, md: 7 }}
          py={{ base: 20, md: 36 }}>
          <Heading
            fontWeight={600}
            fontSize={{ base: '2xl', sm: '4xl', md: '6xl' }}
            lineHeight={'110%'}>
            Defi Compare v2
          </Heading>
          <p color={'gray.500'}>
            Description
          </p>
          <Stack
            direction={'column'}
            spacing={3}
            align={'center'}
            alignSelf={'center'}
            position={'relative'}>
                 <Box>
                     {/*<GasFeeChart></GasFeeChart>*/}
                     <ChartTypeSelector onActiveButtonChange={(activeTokenMetric => setActiveTokenMetric(activeTokenMetric))}></ChartTypeSelector>
                    {/* TODO split time scale into two components with token comparison graph as parent*/}
                    <TimeScaleGraph activeButton={activeTokenMetric}></TimeScaleGraph>
                </Box>
                <Box>
                    {/*TODO*/}
                    <ComparisonTable></ComparisonTable>
                </Box>
          </Stack>
        </Stack>
      </Container>
    );
};


export default Overview;
