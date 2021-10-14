import React, { FC, memo, useState } from "react";
import { useDispatch } from "react-redux";
import { useHistory } from "react-router";
import AddIcon from "@mui/icons-material/Add";
import DeleteIcon from "@mui/icons-material/Delete";
import RemoveRedEyeIcon from "@mui/icons-material/RemoveRedEye";
import { Alert } from "@mui/material";
import Button from "@mui/material/Button";
import { createTheme, Theme } from "@mui/material/styles";
import { makeStyles } from "@mui/styles";
import {
  DataGridPro,
  GridActionsCellItem,
  GridColumns,
  GridToolbarContainer,
  useGridApiRef,
} from "@mui/x-data-grid-pro";
import addScenarioRequest from "../../api/scenarios/addScenario";
import DeleteScenarioRequest from "../../api/scenarios/deleteScenario";
import { fetchScenariosAction } from "../../pages/scenarios/slices/scenarios";
import DeleteModal from "../deleteModel";
import ScenarioFormModal from "../scenarioFormModal";

const defaultTheme = createTheme();

const useStyles = makeStyles(
  (theme: Theme) => ({
    actions: {
      color: theme.palette.text.secondary,
    },
    textPrimary: {
      color: theme.palette.text.primary,
    },
  }),
  { defaultTheme }
);

interface ScenarioTableProps {
  data: any;
}

const ScenariosTable: FC<ScenarioTableProps> = ({ data }) => {
  const classes = useStyles();
  const apiRef = useGridApiRef();
  const history = useHistory();
  const dispatch = useDispatch();

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

  const [openDeleteModel, setOpenDeleteModel] = useState<boolean>(false);
  const [addScenarioOpen, setAddScenarioOpen] = useState<boolean>(false);
  const [newScenario, setNewScenario] = useState(scenarioInitialState);
  const [deleteScenarioId, setDeleteScenarioId] = useState<number>(-1);
  const [addScenarioMessage, setAddScenarioMessage] = useState<string>("");
  const [message, setMessage] = useState<string>("");

  const token = localStorage.getItem("access");

  const handleNewScenarioNameChange = (event: any) => {
    setNewScenario((prev) => ({
      ...prev,
      name: event.target.value,
    }));
  };

  const handleNewScenarioParamsChange = (event: any) => {
    setNewScenario((prev) => ({
      ...prev,
      scenario_hash: {
        ...prev.scenario_hash,
        [event.target.name]: event.target.value,
      },
    }));
  };

  const handleAddClose = () => {
    setAddScenarioOpen(false);
  };

  const handleAddSubmit = () => {
    setMessage("");
    setAddScenarioMessage("");
    addScenarioRequest(newScenario, token)
      .then((response) => {
        dispatch(fetchScenariosAction(token));
        setNewScenario(scenarioInitialState);
        setAddScenarioOpen(false);
        setMessage("Scenario added successfully!");
      })
      .catch((err) => {
        setAddScenarioMessage("Something went wrong!");
      });
  };

  const handleDeleteClose = () => {
    setOpenDeleteModel(false);
    setDeleteScenarioId(-1);
  };

  const handleDelete = () => {
    setOpenDeleteModel(false);
    if (deleteScenarioId === -1) return;
    DeleteScenarioRequest(deleteScenarioId, token)
      .then((response) => {
        setMessage("Scenario Deleted Successfully!");
      })
      .catch((err) => {
        setMessage("Something went wrong!");
      });
    dispatch(fetchScenariosAction(token));
    setDeleteScenarioId(-1);
  };

  const columns: GridColumns = [
    { field: "name", headerName: "Name", width: 180 },
    {
      field: "country",
      headerName: "Countries",
      type: "any",
      width: 300,
    },
    {
      field: "continent",
      headerName: "Continents",
      type: "any",
      width: 300,
    },
    {
      field: "day",
      headerName: "Day",
      type: "date",
      width: 130,
    },
    {
      field: "month",
      headerName: "Month",
      type: "date",
      width: 130,
    },
    {
      field: "year",
      headerName: "year",
      type: "date",
      width: 130,
    },
    {
      field: "created_on",
      headerName: "Date Created",
      type: "date",
      width: 300,
    },
    {
      field: "actions",
      headerName: "Actions",
      type: "actions",
      width: 100,
      cellClassName: classes.actions,
      getActions: (params: any) => [
        <GridActionsCellItem
          icon={<RemoveRedEyeIcon />}
          label="View"
          onClick={(event: any) => {
            history.push({
              pathname: "/scenario-detail",
              state: { scenario: params.row },
            });
          }}
        />,
        <GridActionsCellItem
          icon={<DeleteIcon />}
          label="Delete"
          onClick={() => {
            setMessage("");
            setDeleteScenarioId(params.id);
            setOpenDeleteModel(true);
          }}
        />,
      ],
    },
  ];

  return (
    <div
      style={{ height: "90vh", width: "100%", marginLeft: 5, marginRight: 5 }}
    >
      <DeleteModal
        open={openDeleteModel}
        handleClose={handleDeleteClose}
        handleDelete={handleDelete}
      />
      <ScenarioFormModal
        open={addScenarioOpen}
        scenario={newScenario}
        message={addScenarioMessage}
        helpText="Add"
        handleNewScenarioNameChange={handleNewScenarioNameChange}
        handleNewScenarioParamsChange={handleNewScenarioParamsChange}
        handleClose={handleAddClose}
        handleSubmit={handleAddSubmit}
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
      <GridToolbarContainer>
        <Button
          color="primary"
          startIcon={<AddIcon />}
          onClick={() => {
            setMessage("");
            setAddScenarioOpen(true);
          }}
        >
          Add Scenario
        </Button>
      </GridToolbarContainer>
      <DataGridPro
        rows={data.map((data_row: any) => ({
          ...data_row,
          continent: data_row.scenario_hash.params.continent.join(", "),
          country: data_row.scenario_hash.params.country.join(", "),
          day: data_row.scenario_hash.params.day,
          month: data_row.scenario_hash.params.month,
          year: data_row.scenario_hash.params.year,
        }))}
        columns={columns}
        componentsProps={{
          toolbar: { apiRef },
        }}
      />
    </div>
  );
};

export default memo(ScenariosTable);
