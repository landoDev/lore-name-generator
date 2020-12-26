import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';

import { ChakraProvider } from "@chakra-ui/react";
// Chakra provides the below function which allows a deep merge of custom themes with Chakra's default.
import { extendTheme } from "@chakra-ui/react";
import { colors, fonts } from "./customThemes";

const theme = extendTheme({colors, fonts})


ReactDOM.render(
  <React.StrictMode>
    <ChakraProvider
    // custom themes can be uncommented when ready
    // theme={theme}
    >
      <App />
    </ChakraProvider>
  </React.StrictMode>,
  document.getElementById('root')
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
