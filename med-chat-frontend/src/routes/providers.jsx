import React, {useState, useEffect} from "react";
import { Form } from "react-router-dom";

let base_url = "http://localhost:5000/";

export default function Providers() {
  const [providers, setProviders] = useState([]);
  useEffect(() => {
    fetch(base_url + "providers")
    .then((response) => response.json())
    .then((actualData) => {
      setProviders(actualData);
    })
    .catch((err) => {
      setMonuments(null);
      console.error(err.message)
    })
}, []);



  return (
    <div id="providers">
        <h1>Providers</h1>
          {
                providers && providers.map((provider, key) => {
                    return(
                      <div>
                        <h2>{provider.name}</h2>
                        <p>{provider.specialty}</p>
                        <p>{provider.phone}</p>
                        <p>{provider.email}</p>
                      </div>
                    )
                })
            }
    </div>
  );
}