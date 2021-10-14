import React, { FC, useEffect, useState } from "react";
import { RootStateOrAny, useDispatch, useSelector } from "react-redux";
import { Grid } from "@mui/material";
import HeaderAppBar from "../../components/appBar";
import ChartsTab from "../../components/chartsTab";
import ProfileCard from "../../components/profileCard";
import { fetchContinentGraphDataAction } from "./slices/continent-graph-data";
import { fetchCountryGraphDataAction } from "./slices/country-graph-data";
import { setUserProfileAction } from "./slices/profile";
import { fetchWorldGraphDataAction } from "./slices/world-graph-data";
import { Button } from "@mui/material";
import Map from "../../components/mapBox";

const Home: FC = () => {
  const user = useSelector((state: RootStateOrAny) => state.profile.user);
  const worldGraphData = useSelector(
    (state: RootStateOrAny) => state.worldGraphData.graphData
  );
  const countryGraphData = useSelector(
    (state: RootStateOrAny) => state.countryGraphData.graphData
  );
  const continentGraphData = useSelector(
    (state: RootStateOrAny) => state.continentGraphData.graphData
  );

  const dispatch = useDispatch();

  const [changeCountry, setChangeCountry] = useState<boolean>(false);
  const [country, setCountry] = useState({ geoid: "pk" });
  const [continent, setContinent] = useState({ name: "asia" });

  useEffect(() => {
    dispatch(setUserProfileAction());
    if (!worldGraphData.data.length) dispatch(fetchWorldGraphDataAction());
    // eslint-disable-next-line
  }, []);

  useEffect(() => {
    if (user && user.country) {
      setCountry(user.country);
      setContinent(user.country.continent);
    }
  }, [user]);

  useEffect(() => {
    dispatch(fetchContinentGraphDataAction(continent.name));
    // eslint-disable-next-line
  }, [continent]);

  useEffect(() => {
    dispatch(fetchCountryGraphDataAction(country.geoid));
    // eslint-disable-next-line
  }, [country]);

  return (
    <div>
      <HeaderAppBar user={user} />
      <Grid container spacing={2}>
        {user && user.email ? (
          <Grid item xs={12} md={4}>
            <ProfileCard user={user} />
          </Grid>
        ) : (
          ""
        )}

        <Grid item xs={12} md={localStorage.getItem("access") ? 8 : 12}>
          <ChartsTab data={worldGraphData} />
        </Grid>
        <Grid sx={{ position: "relative" }} item xs={12} md={6}>
          <ChartsTab data={continentGraphData} />
        </Grid>
        <Grid sx={{ position: "relative" }} item xs={12} md={6}>
          <Button
            variant="contained"
            size="small"
            onClick={() => {
              setChangeCountry(!changeCountry);
            }}
            sx={{ position: "absolute", right: 10, top: 20, zIndex: 100 }}
          >
            {changeCountry ? "Canel Change Country" : "Change Country"}
          </Button>
          {changeCountry ? (
            <div style={{ marginTop: 50 }}>
              <Map
                setCountry={setCountry}
                setChangeCountry={setChangeCountry}
              />
            </div>
          ) : (
            <ChartsTab data={countryGraphData} />
          )}
        </Grid>
      </Grid>
    </div>
  );
};

export default Home;
