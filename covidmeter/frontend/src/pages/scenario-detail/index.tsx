import React, { FC, useEffect, useState } from "react";
import { RootStateOrAny, useDispatch, useSelector } from "react-redux";
import { useHistory, useLocation } from "react-router";
import DeleteIcon from "@mui/icons-material/Delete";
import EditIcon from "@mui/icons-material/Edit";
import { Alert, Divider, Grid, IconButton, Typography } from "@mui/material";
import DeleteScenarioRequest from "../../api/scenarios/deleteScenario";
import updateScenarioRequest from "../../api/scenarios/updateScenario";
import HeaderAppBar from "../../components/appBar";
import ChartsTab from "../../components/chartsTab";
import DeleteModal from "../../components/deleteModel";
import ScenarioFormModal from "../../components/scenarioFormModal";
import { setUserProfileAction } from "../home/slices/profile";
import { fetchScenariosAction } from "../scenarios/slices/scenarios";

const ScenarioDetail: FC = () => {
  const history = useHistory();
  const location: any = useLocation();

  if (!location.state) history.push("/scenarios");

  const scenarioInitialState = {
    name: "",
    scenario_hash: {
      country: [],
      continent: [],
      day: null,
      month: null,
      year: null,
    },
  };

  const user = useSelector((state: RootStateOrAny) => state.profile.user);

  const [scenario, setScenario] = useState<any>(location.state.scenario);
  const [openDeleteModel, setOpenDeleteModel] = useState(false);
  const [editScenario, setEditScenario] = useState<any>(scenarioInitialState);
  const [editScenarioOpen, setEditScenarioOpen] = useState<boolean>(false);
  const [editScenarioMessage, setEditScenarioMessage] = useState<string>("");
  const [message, setMessage] = useState<string>("");

  const dispatch = useDispatch();

  const token = localStorage.getItem("access");

  useEffect(() => {
    if (!token) {
      history.push("/login");
    }
    dispatch(setUserProfileAction());
    // eslint-disable-next-line
  }, []);

  useEffect(() => {
    if (scenario.name) {
      setEditScenario((prev: any) => ({
        name: scenario.name,
        scenario_hash: {
          ...prev.scenario_hash,
          ...scenario.scenario_hash.params,
        },
      }));
    }
  }, [scenario]);

  const handleEditScenarioNameChange = (event: any) => {
    setEditScenario((prev: any) => ({
      ...prev,
      name: event.target.value,
    }));
  };

  const handleEditScenarioParamsChange = (event: any) => {
    setEditScenario((prev: any) => ({
      ...prev,
      scenario_hash: {
        ...prev.scenario_hash,
        [event.target.name]: event.target.value,
      },
    }));
  };

  const handleEditClose = () => {
    setEditScenarioOpen(false);
  };

  const handleEditSubmit = () => {
    setMessage("");
    setEditScenarioMessage("");
    updateScenarioRequest(scenario.id, editScenario, token)
      .then((response) => {
        dispatch(fetchScenariosAction(token));
        setScenario(response);
        setEditScenarioOpen(false);
        setMessage("Scenario updated successfully!");
      })
      .catch((err) => {
        setEditScenarioMessage("Something went wrong!");
      });
  };

  const handleDeleteClose = () => {
    setOpenDeleteModel(false);
  };

  const handleDelete = () => {
    setOpenDeleteModel(false);
    DeleteScenarioRequest(scenario.id, token)
      .then((response) => {
        history.push("/scenarios");
      })
      .catch((err) => {});
  };

  return (
    <div>
      <HeaderAppBar user={user} />
      <DeleteModal
        open={openDeleteModel}
        handleClose={handleDeleteClose}
        handleDelete={handleDelete}
      />
      <ScenarioFormModal
        open={editScenarioOpen}
        scenario={editScenario}
        message={editScenarioMessage}
        helpText="Update"
        handleNewScenarioNameChange={handleEditScenarioNameChange}
        handleNewScenarioParamsChange={handleEditScenarioParamsChange}
        handleClose={handleEditClose}
        handleSubmit={handleEditSubmit}
      />
      <div style={{ textAlign: "center" }}>
        {message ? (
          <Alert
            sx={{ width: "300px", margin: "auto" }}
            variant="outlined"
            severity="info"
          >
            {message}
          </Alert>
        ) : (
          ""
        )}
      </div>
      <Grid container spacing={2} sx={{ padding: 5 }}>
        <Grid item xs={12} sx={{ textAlign: "center" }}>
          <Typography component="h6" variant="h6">
            <i>{scenario.name}</i>
          </Typography>
        </Grid>
        <Grid item xs={12} sx={{ textAlign: "center" }}>
          <IconButton
            onClick={() => {
              setEditScenarioOpen(true);
            }}
            aria-label="Edit"
          >
            <EditIcon />
          </IconButton>
          <IconButton
            onClick={() => {
              setOpenDeleteModel(true);
            }}
            aria-label="delete"
          >
            <DeleteIcon />
          </IconButton>
        </Grid>
        <Grid item xs={12}>
          <Divider />
          <Divider />
        </Grid>
        <Grid item xs={12} md={6}>
          <Typography component="h6" variant="h6">
            Created on: <i>{scenario.created_on}</i>
          </Typography>
        </Grid>
        <Grid item xs={12} md={6}>
          <Typography component="h6" variant="h6">
            Modified on: <i>{scenario.modified_on}</i>
          </Typography>
        </Grid>
        <Grid item xs={12}>
          <Divider />
          <Divider />
        </Grid>
        <Grid item xs={4}>
          <Typography component="h6" variant="h6">
            Day:{" "}
            <i>
              {scenario.scenario_hash.params.day
                ? scenario.scenario_hash.params.day
                : "X"}
            </i>
          </Typography>
        </Grid>
        <Grid item xs={4}>
          <Typography component="h6" variant="h6">
            Month:{" "}
            <i>
              {scenario.scenario_hash.params.month
                ? scenario.scenario_hash.params.month
                : "X"}
            </i>
          </Typography>
        </Grid>
        <Grid item xs={4}>
          <Typography component="h6" variant="h6">
            Year:{" "}
            <i>
              {scenario.scenario_hash.params.year
                ? scenario.scenario_hash.params.year
                : "X"}
            </i>
          </Typography>
        </Grid>
        <Grid item xs={12} md={6}>
          <Typography component="h6" variant="h6">
            Continents:{" "}
            <i>{scenario.scenario_hash.params.continent.join(", ")}</i>
          </Typography>
        </Grid>
        <Grid item xs={12} md={6}>
          <Typography component="h6" variant="h6">
            Countries: <i>{scenario.scenario_hash.params.country.join(", ")}</i>
          </Typography>
        </Grid>
        <Grid item xs={12}>
          <Divider />
          <Divider />
          <Divider />
          <Divider />
          <Divider />
          <Divider />
        </Grid>
        {scenario.scenario_hash.result.world ? (
          <Grid item xs={12}>
            <ChartsTab data={scenario.scenario_hash.result.world} />
          </Grid>
        ) : (
          ""
        )}
        {scenario.scenario_hash.result.continent.length ? (
          <Grid item xs={12} md={6}>
            <Typography
              sx={{ textAlign: "center" }}
              component="h4"
              variant="h4"
            >
              Continents Stats
            </Typography>
            {scenario.scenario_hash.result.continent.map(
              (continent_data: any) => (
                <ChartsTab data={continent_data} />
              )
            )}
          </Grid>
        ) : (
          ""
        )}
        {scenario.scenario_hash.result.country.length ? (
          <Grid item xs={12} md={6}>
            {" "}
            <Typography
              sx={{ textAlign: "center" }}
              component="h4"
              variant="h4"
            >
              Countries Stats
            </Typography>
            {scenario.scenario_hash.result.country.map((country_data: any) => (
              <ChartsTab data={country_data} />
            ))}
          </Grid>
        ) : (
          ""
        )}
      </Grid>
    </div>
  );
};

export default ScenarioDetail;
