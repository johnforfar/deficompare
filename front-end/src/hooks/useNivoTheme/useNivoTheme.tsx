import React from "react";
import {Theme} from '@nivo/core'
import {useColorMode} from '@chakra-ui/react';

type HookProps = {
    overrides?:Theme
};

const useNivoTheme = (props?:HookProps) => {
    const {colorMode} = useColorMode()
    let theme: Theme = {
        background: "#000000",
        textColor: "#ffffff",
        fontSize: 14,
        axis: {
            "domain": {
                "line": {
                    "strokeWidth": 1
                }
            },
            "ticks": {
                "line": {
                    "strokeWidth": 1
                }
            }
        },
        "grid": {
            "line": {
                "strokeWidth": 1
            }
        }
    }
    if (colorMode === 'dark') {
        theme.background = 'black'
        theme.textColor = 'white'
    } else {
        theme.background = 'white'
        theme.textColor = 'black'
    }
    if(props && props.overrides){
        //Merge the two themes
        theme = {
            ...theme,
            ...props.overrides
        }
    }
    return {theme};

};

export default useNivoTheme;
