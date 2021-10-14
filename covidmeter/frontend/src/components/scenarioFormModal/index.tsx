import React, { FC, useEffect } from "react";
import { RootStateOrAny, useDispatch, useSelector } from "react-redux";
import { Alert } from "@mui/material";
import Button from "@mui/material/Button";
import Chip from "@mui/material/Chip";
import Dialog from "@mui/material/Dialog";
import DialogActions from "@mui/material/DialogActions";
import DialogContent from "@mui/material/DialogContent";
import DialogTitle from "@mui/material/DialogTitle";
import MenuItem from "@mui/material/MenuItem";
import OutlinedInput from "@mui/material/OutlinedInput";
import Select from "@mui/material/Select";
import TextField from "@mui/material/TextField";
import { Box } from "@mui/system";

import { fetchContinentsDataAction } from "../../pages/home/slices/continents-data";
import { fetchCountriesDataAction } from "../../pages/home/slices/countries-data";

interface ScenarioFormModalProps {
  open: boolean;
  scenario: any;
  message: string;
  helpText: string;
  handleNewScenarioNameChange: (event: any) => void;
  handleNewScenarioParamsChange: (event: any) => void;
  handleClose: () => void;
  handleSubmit: () => void;
}

const ScenarioFormModal: FC<ScenarioFormModalProps> = ({
  open,
  scenario,
  message,
  helpText,
  handleNewScenarioNameChange,
  handleNewScenarioParamsChange,
  handleClose,
  handleSubmit,
}) => {
  const countries = useSelector(
    (state: RootStateOrAny) => state.countriesData.countries
  );
  const continents = useSelector(
    (state: RootStateOrAny) => state.continentsData.continents
  );
  const monthNames = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
  ];

  const dispatch = useDispatch();

  useEffect(() => {
    dispatch(fetchCountriesDataAction());
    dispatch(fetchContinentsDataAction());
    // eslint-disable-next-line
  }, []);

  return (
    <Dialog open={open} onClose={handleClose}>
      <DialogTitle>{helpText} Scenario</DialogTitle>
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
      <DialogContent>
        <TextField
          autoFocus
          margin="dense"
          id="name"
          name="name"
          label="Scenario Name"
          fullWidth
          variant="standard"
          required
          value={scenario.name}
          onChange={handleNewScenarioNameChange}
        />
        <Select
          name="day"
          margin="dense"
          sx={{ width: "33%" }}
          value={scenario.scenario_hash.day}
          label="Day"
          input={<OutlinedInput label="Day" />}
          onChange={handleNewScenarioParamsChange}
        >
          {Array.from(Array(30).keys()).map((day) => (
            <MenuItem key={day + 1} value={day + 1}>
              {day + 1}
            </MenuItem>
          ))}
        </Select>

        <Select
          name="month"
          margin="dense"
          sx={{ width: "33%" }}
          value={scenario.scenario_hash.month}
          label="Month"
          input={<OutlinedInput label="Month" />}
          onChange={handleNewScenarioParamsChange}
        >
          {monthNames.map((month, index) => (
            <MenuItem key={index + 1} value={index + 1}>
              {month}
            </MenuItem>
          ))}
        </Select>
        <Select
          name="year"
          margin="dense"
          sx={{ width: "33%" }}
          value={scenario.scenario_hash.year}
          label="Year"
          input={<OutlinedInput label="Year" />}
          onChange={handleNewScenarioParamsChange}
        >
          <MenuItem key={2019} value={2019}>
            {2019}
          </MenuItem>
          <MenuItem key={2020} value={2020}>
            {2020}
          </MenuItem>
        </Select>
        <Select
          multiple
          fullWidth
          name="continent"
          margin="dense"
          value={scenario.scenario_hash.continent}
          label="Continents"
          input={<OutlinedInput label="Continents" />}
          onChange={handleNewScenarioParamsChange}
          renderValue={(selected) => (
            <Box sx={{ display: "flex", flexWrap: "wrap", gap: 0.5 }}>
              {selected.map((value: string) => (
                <Chip key={value.toUpperCase()} label={value} />
              ))}
            </Box>
          )}
        >
          {continents.map((continent: any) => (
            <MenuItem
              key={continent.name.toUpperCase()}
              value={continent.name.toUpperCase()}
            >
              {continent.name}
            </MenuItem>
          ))}
        </Select>
        <Select
          fullWidth
          multiple
          name="country"
          label="Countries"
          input={<OutlinedInput label="Countries" />}
          value={scenario.scenario_hash.country}
          onChange={handleNewScenarioParamsChange}
          renderValue={(selected) => (
            <Box sx={{ display: "flex", flexWrap: "wrap", gap: 0.5 }}>
              {selected.map((value: any) => (
                <Chip key={value.toUpperCase()} label={value} />
              ))}
            </Box>
          )}
        >
          {countries.map((country: any) => (
            <MenuItem
              key={country.geoid.toUpperCase()}
              value={country.geoid.toUpperCase()}
            >
              {country.name}
            </MenuItem>
          ))}
        </Select>
      </DialogContent>
      <DialogActions>
        <Button onClick={handleClose}>Cancel</Button>
        <Button onClick={handleSubmit}>{helpText}</Button>
      </DialogActions>
    </Dialog>
  );
};

export default ScenarioFormModal;
