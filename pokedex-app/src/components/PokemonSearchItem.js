import React, { useState } from "react";
import PokemonItem from "./PokemonItem";

function PokemonSearchItem({ name, prob, img, data }) {
  const [showDetails, setShowDetails] = useState(false);

  return (
    <div className="pokemon-search-item">
      <div>Name: {name} </div>
      <div>Confidence: {Math.round(prob)}% </div>
      <a
        onClick={() => {
          setShowDetails(!showDetails);
        }}
      >
        <img src={`data:image/jpeg;base64,${img}`}></img>
      </a>
      {showDetails ? <PokemonItem {...data}></PokemonItem> : null}
    </div>
  );
}

export default PokemonSearchItem;
