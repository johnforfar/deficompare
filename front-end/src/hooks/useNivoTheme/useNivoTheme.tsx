import React from "react";
import {CompleteTheme, Theme} from '@nivo/core'
import {useColorMode} from '@chakra-ui/react';

type HookProps = {
    overrides?: CustomNivoTheme
    darkOnlyOverrides?: CustomNivoTheme
    lightOnlyOverrides?: CustomNivoTheme
};

export interface CustomNivoTheme extends Theme {
    //Work around to ensure tooltip attribute will always be there
    tooltip: {
        container: Partial<React.CSSProperties>
        basic: Partial<React.CSSProperties>
        chip: Partial<React.CSSProperties>
        table: Partial<React.CSSProperties>
        tableCell: Partial<React.CSSProperties>
        tableCellValue: Partial<React.CSSProperties>
    }
}

const useNivoTheme = (props?: HookProps) => {
    const {colorMode} = useColorMode()
    let theme: CustomNivoTheme = {
        background: "#000000",
        textColor: "#ffffff",
        fontSize: 14,
        tooltip: {
            container: {},
            basic: {},
            chip: {},
            table: {},
            tableCell: {},
            tableCellValue: {}
        },
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
        theme.background = 'black';
        theme.textColor = 'white';
        theme.tooltip.container.background = 'black'
        theme.tooltip.container.textEmphasisColor = 'white'

        if (props && props.darkOnlyOverrides) {
            //Merge the two themes
            theme = {
                ...theme,
                ...props.overrides
            }
        }
    } else if (colorMode === 'light') {
        theme.background = 'white'
        theme.textColor = 'black'

        theme.tooltip.container.background = 'white'
        theme.tooltip.container.textEmphasisColor = 'black'
        if (props && props.lightOnlyOverrides) {
            //Merge the two themes
            theme = {
                ...theme,
                ...props.lightOnlyOverrides
            }
        }
    }


    if (props && props.overrides) {
        //Merge the two themes
        theme = {
            ...theme,
            ...props.overrides
        }
    }
    return {theme};

};

export default useNivoTheme;
