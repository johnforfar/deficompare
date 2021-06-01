import {extendTheme, ThemeConfig} from "@chakra-ui/react"
import type {Styles} from '@chakra-ui/theme-tools';
import {darken, mode, whiten} from "@chakra-ui/theme-tools";
import {Dict} from '@chakra-ui/utils/dist/types/types';

const config: ThemeConfig = {
    initialColorMode: "dark",
    useSystemColorMode: false,
}

const colors = {
    primary: "#832BCC",
    secondary: "#66C7F4",
    highlight: "#00C9A7",
    warning: "#FFC75F",
    danger: "#C34A36",
}

const styles: Styles = {
    global: (props: Dict) => ({
        body: {
            bg: mode('white', 'black')(props),
            // color: mode('white', 'black')(props),
        }
    })
};

const components = {
    Link: {
        baseStyle: (props: Dict) => ({
            bg: mode(whiten("primary", 20), darken("primary", 20))(props),
            // color: mode('white', 'white')(props),
        }),
    },
    Container: {
        baseStyle: (props: Dict) => ({
            bg: mode('white', 'black')(props),
            // color: mode('white', 'black')(props),
        }),
    },
    Button: {
        baseStyle: (props: Dict) => ({
            bg: mode(whiten("primary", 20), darken("primary", 20))(props),
            // color: mode('white', 'black')(props),
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