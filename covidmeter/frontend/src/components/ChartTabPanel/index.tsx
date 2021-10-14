import React, { FC } from "react";
import { MenuItem, Select } from "@mui/material";
import CovidChart from "../charts";

interface ChartTabPanelProps {
  field: string;
  chartType: string;
  fieldsList: Array<string>;
  region: string;
  regionType: string;
  data: any;
  handleFieldChange: (value: string) => void;
  handleChartTypeChange: (value: string) => void;
}

const ChartTabPanel: FC<ChartTabPanelProps> = ({
  field,
  chartType,
  fieldsList,
  data,
  region,
  regionType,
  handleFieldChange,
  handleChartTypeChange,
}) => {
  return (
    <div>
      <Select
        value={field}
        label=""
        variant="standard"
        onChange={(event: any) => {
          handleFieldChange(event.target.value);
        }}
      >
        {fieldsList.map((fld: string) => (
          <MenuItem value={fld}>{fld[0].toUpperCase() + fld.slice(1)}</MenuItem>
        ))}
      </Select>
      <Select
        value={chartType}
        label=""
        variant="standard"
        onChange={(event: any) => {
          handleChartTypeChange(event.target.value);
        }}
        sx={{ marginLeft: 4 }}
      >
        <MenuItem value={"AreaChart"}>Line Chart</MenuItem>
        <MenuItem value={"ColumnChart"}>Bar Chart</MenuItem>
      </Select>
      <CovidChart
        data={data.data}
        title={region ? `${region} - ${regionType}` : "World-wide stats"}
        chartType={chartType}
        colors={/deaths/i.test(field) ? ["#FF0101"] : ["#008080"]}
        valueField={[field]}
      />
    </div>
  );
};

export default ChartTabPanel;
