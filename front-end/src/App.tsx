import React from 'react';
import './App.scss';
import Navbar from './components/Navbar/Navbar';
// 1. import `ChakraProvider` component
import {ChakraProvider} from "@chakra-ui/react"
import {
    BrowserRouter as Router,
    Switch,
    Route,
    Link
} from "react-router-dom";
import Overview from './pages/Overview/Overview';
import theme from './theme';

function App() {
    return (
        <ChakraProvider theme={theme}>
            <Router>


                <Navbar></Navbar>

                <Switch>
                    {/*<Route path="/about">*/}
                    {/*  <About />*/}
                    {/*</Route>*/}
                    {/*<Route path="/users">*/}
                    {/*  <Users />*/}
                    {/*</Route>*/}
                    <Route path="/">
                        <Overview/>
                    </Route>
                </Switch>
            </Router>
        </ChakraProvider>
    );
}

export default App;
