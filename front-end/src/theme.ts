import {extendTheme, ThemeConfig} from "@chakra-ui/react"
import type {Styles} from '@chakra-ui/theme-tools';
import {darken, mode, whiten} from "@chakra-ui/theme-tools";
import {Dict} from '@chakra-ui/utils/dist/types/types';

const config: ThemeConfig = {
    initialColorMode: "dark",
    useSystemColorMode: false,
}

const colors = {
    primary: "#845EC2",
    secondary: "#FF6F91",
    highlight: "#00C9A7",
    warning: "#FFC75F",
    danger: "#C34A36",
}

const styles: Styles = {
    global: (props: Dict) => ({
        body: {
            color: mode('gray.800', 'whiteAlpha.900')(props),
            bg: mode('white', 'gray.900')(props)
        }
    })
};

const components = {
    Link: {
        baseStyle: (props: Dict) => ({
            bg: mode(whiten("primary", 20), darken("primary", 20))(props),
            color: props.colorMode === "dark" ? "gray.800" : "white",
        }),
    },
}

const theme = extendTheme({
    config,
    colors,
    components,
    styles
});

export default theme;