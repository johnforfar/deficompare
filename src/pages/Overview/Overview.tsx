import {Box, Container, Heading, Stack} from "@chakra-ui/react";
import {useParams} from "react-router";
import "./styles.scss";
import ComparisonTable from '../../components/ComparisonTable/ComparisonTable';
import React from 'react';
import TokenMetricsComparisonChart from '../../components/TokenMetricsComparisonChart/TokenMetricsComparisonChart';

const Overview = () => {
    const {name} = useParams<{ name: string }>();
    return (

        <Container>
            <Stack
                as={Box}
                textAlign={'center'}
                spacing={{base: 4, md: 7}}
                py={{base: 20, md: 36}}>
                <Heading
                    fontWeight={600}
                    fontSize={{base: '2xl', sm: '4xl', md: '6xl'}}
                    lineHeight={'110%'}>
                    Defi Compare v2
                </Heading>
                <p color={'gray.500'}>
                    Crypto Compare
                </p>
                <Stack
                    direction={'column'}
                    spacing={3}
                    align={'center'}
                    alignSelf={'center'}
                    position={'relative'}>
                    <Box>
                        <TokenMetricsComparisonChart></TokenMetricsComparisonChart>
                    </Box>
                    <Box>
                        <ComparisonTable></ComparisonTable>
                    </Box>
                </Stack>
            </Stack>
        </Container>
    );
};


export default Overview;
