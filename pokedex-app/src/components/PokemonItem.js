import React from "react";
import "./Pokedex.css";

function PokemonItem({
  pokedex_number,
  name,
  japanese_name,
  abilities,
  attack,
  defense,
  sp_attack,
  sp_defense,
  height_m,
  weight_kg,
  speed,
  generation,
  is_legendary,
}) {
  return (
    <>
      <div className="pokemon-item">
        <div>
          <table>
            <tr>
              <th>Description</th>
              <th>Value</th>
            </tr>
            <tr>
              <td>Pokedex Number</td>
              <td>{pokedex_number}</td>
            </tr>
            <tr>
              <td>Name</td>
              <td>{name}</td>
            </tr>
            <tr>
              <td>Japanese Name</td>
              <td>{japanese_name}</td>
            </tr>
            <tr>
              <td>Height</td>
              <td>{height_m} m</td>
            </tr>
            <tr>
              <td>Weight</td>
              <td>{weight_kg} Kg</td>
            </tr>
            <tr>
              <td>Speed</td>
              <td>{speed}</td>
            </tr>
            <tr>
              <td>Abilities</td>
              <td>{abilities}</td>
            </tr>
            <tr>
              <td>Attack</td>
              <td>{attack}</td>
            </tr>
            <tr>
              <td>Defense</td>
              <td>{defense}</td>
            </tr>
            <tr>
              <td>Special Attach</td>
              <td>{sp_attack}</td>
            </tr>
            <tr>
              <td>Special Defense</td>
              <td>{sp_defense}</td>
            </tr>
          </table>
        </div>
      </div>
    </>
  );
}

export default PokemonItem;
