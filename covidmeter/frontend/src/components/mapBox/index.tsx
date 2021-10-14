import React, { FC, memo } from "react";
import { useState } from "react";
import ReactMapGL from "react-map-gl";
import "mapbox-gl/dist/mapbox-gl.css";

const MAPBOX_TOKEN =
  "pk.eyJ1IjoicmF2ZWVkYWhtZWQiLCJhIjoiY2t1Z2szbW1uMHl1MDJ1cnRpdmRiMDJwcSJ9.1PIuu58R4XAZvsq9lvs5xg";

interface MapProps {
  setCountry: (country: any) => void;
  setChangeCountry: (changeCountry: boolean) => void;
}

const Map: FC<MapProps> = ({ setCountry, setChangeCountry }) => {
  const [viewport, setViewport] = useState({
    width: "100%",
    height: 400,
    latitude: 37.7577,
    longitude: -122.4376,
    zoom: 1,
  });

  return (
    <div style={{ marginRight: 10, marginLeft: 10 }}>
      <ReactMapGL
        {...viewport}
        onClick={(event: any) => {
          event.features.some((feature: any) => {
            if (feature.sourceLayer === "country_label") {
              setCountry({ geoid: feature.properties.code });
              setChangeCountry(false);
              return;
            }
          });
        }}
        mapboxApiAccessToken={MAPBOX_TOKEN}
        onViewportChange={(nextViewport: any) => setViewport(nextViewport)}
      ></ReactMapGL>
    </div>
  );
};

export default memo(Map);
