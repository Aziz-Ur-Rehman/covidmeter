import React, { FC } from "react";
import Router from "./routes.js/routes";
import "mapbox-gl/dist/mapbox-gl.css";

const App: FC = () => {
  return (
    <div className="App">
      <Router />
    </div>
  );
};

export default App;
