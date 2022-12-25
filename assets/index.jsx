import React from "react";
import { BrowserRouter } from "react-router-dom";
import ReactDOM from "react-dom/client";
import App from "./App";

const domContainer = document.getElementById('root');
const root = ReactDOM.createRoot(domContainer);
root.render(
    <BrowserRouter>
        <App />
    </BrowserRouter>
);
