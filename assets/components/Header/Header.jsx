import React from "react";
import { NavLink } from "react-router-dom";
import { Container, Button } from "@mui/material";

import "./Header.css";

const Header = () => {
    return (
        <header>
            <Container>
                <nav>
                    <div>
                        {/* <NavLink to="browse">Browse</NavLink>
                        <NavLink to="create">Create</NavLink> */}
                        <Button component={NavLink} to="browse">Browse</Button>
                        <Button component={NavLink} to="create">Create</Button>
                    </div>
                </nav>
            </Container>
        </header>
    )
};

export default Header;