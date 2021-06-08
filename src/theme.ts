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
    Container: {
        baseStyle: (props: Dict) => ({
            bg: mode('white', 'black')(props),
        }),
    },
    Button: {
        variants: {
            outline: (props: Dict) => ({
                border: "2px solid",
                borderColor: "primary",
                color: props.colorMode === 'dark' ? "white" : 'primary',
                _hover: {
                    bg: 'primary',
                    color: 'white'
                }
            }),
            solid: (props: Dict) => ({
                bg: "primary",
                color: 'white',
                _hover: {
                    bg: 'primary',
                    color: 'white'
                }
            })
        }
    },
}

const theme = extendTheme({
    config,
    colors,
    components,
    styles
});

export default theme;