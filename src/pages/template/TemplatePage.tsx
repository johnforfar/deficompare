import {Box, Center, Flex, Square} from "@chakra-ui/react";
import { useParams } from "react-router";
import "./styles.scss";

const TemplatePage = () => {
  const { name } = useParams<{ name: string }>();

  return (
 <Flex color="white">
  <Box flex="1" bg="tomato">
    <Center>Content here</Center>
  </Box>
</Flex>
  );
};

export default TemplatePage;
