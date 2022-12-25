import React from "react";
import { Routes, Route } from "react-router";
import Header from "./components/Header/Header";
import Home from "./components/Home/Home";
import Browse from "./components/Browse/Browse";
import Create from "./components/Create/Create";

const App = () => {
    return (
        <>
            <Header/>
            <Routes>
                <Route
                    path="/"
                    element={<Home/>}
                />
                <Route
                    path="/browse"
                    element={<Browse/>}
                />
                <Route
                    path="/create"
                    element={<Create/>}
                />
            </Routes>
        </>
    );
};

export default App;