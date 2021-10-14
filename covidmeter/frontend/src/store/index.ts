import { configureStore } from "@reduxjs/toolkit";
import { continentGraphDataSlice } from "../pages/home/slices/continent-graph-data";
import { continentsDataSlice } from "../pages/home/slices/continents-data";
import { countriesDataSlice } from "../pages/home/slices/countries-data";
import { countryGraphDataSlice } from "../pages/home/slices/country-graph-data";
import { userProfileSlice } from "../pages/home/slices/profile";
import { worldGraphDataSlice } from "../pages/home/slices/world-graph-data";
import { scenarioSlice } from "../pages/scenarios/slices/scenarios";

export default configureStore({
  reducer: {
    profile: userProfileSlice.reducer,
    worldGraphData: worldGraphDataSlice.reducer,
    countryGraphData: countryGraphDataSlice.reducer,
    continentGraphData: continentGraphDataSlice.reducer,
    scenarios: scenarioSlice.reducer,
    continentsData: continentsDataSlice.reducer,
    countriesData: countriesDataSlice.reducer,
  },
});
