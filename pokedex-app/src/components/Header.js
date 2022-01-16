import React from "react";
import logo from "../pokedex_logo.png";
function Header() {
  return (
    <>
      <div>
        <h1>Pokedex</h1>
        <img src={logo} width={100}></img>
      </div>
      <h3>A simple pokedex for the Kanto Region's Pokemon</h3>
    </>
  );
}

export default Header;
