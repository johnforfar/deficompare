import {Box, Button, Center, Container, Flex, Heading, Icon, Square, Stack, useColorModeValue} from "@chakra-ui/react";
import {useParams} from "react-router";
import "./styles.scss";
import ComparisonTable from '../../components/ComparisonTable/ComparisonTable';
import React from 'react';
import GasFeeChart from '../../components/GasFeeChart/GasFeeChart';
import TimeScaleGraph from '../../components/TimeScaleGraph/TimeScaleGraph';

const Overview = () => {
    const {name} = useParams<{ name: string }>();

    return (

      <Container maxW={'3xl'}>
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
                    <TimeScaleGraph></TimeScaleGraph>
                </Box>
                <Box >
                    {/*TODO*/}
                    {/*<ComparisonTable></ComparisonTable>*/}
                </Box>
          </Stack>
        </Stack>
      </Container>
    );
};


export default Overview;
