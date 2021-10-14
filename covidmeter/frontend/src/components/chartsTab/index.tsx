import React, { FC, memo, useEffect, useState } from "react";
import Box from "@mui/material/Box";
import TabContext from "@mui/lab/TabContext";
import TabList from "@mui/lab/TabList";
import TabPanel from "@mui/lab/TabPanel";
import Tab from "@mui/material/Tab";
import ChartTabPanel from "../ChartTabPanel";

interface ChartsTabProps {
  data: any;
}

const ChartsTab: FC<ChartsTabProps> = ({ data }) => {
  const [value, setValue] = useState<string>("1");
  const [region, setRegion] = useState<string>("");
  const [regionType, setRegionType] = useState<string>("");

  const [dailyField, setDailyField] = useState<string>("cases");
  const [cumField, setCumField] = useState<string>("Cumulative Cases");

  const [dailyChartType, setDailyChartType] = useState<string>("ColumnChart");
  const [cumChartType, setCumChartType] = useState<string>("AreaChart");

  const handleChange = (_: any, newValue: string) => {
    setValue(newValue);
  };

  useEffect(() => {
    if (data.country) {
      setRegion(data.country.name);
      setRegionType("Country Stats");
    } else if (data.continent) {
      setRegion(data.continent.name);
      setRegionType("Continent Stats");
    }
  }, [data.country, data.continent]);

  return (
    <Box sx={{ paddingLeft: 2 }}>
      <TabContext value={value}>
        <Box sx={{ borderBottom: 1, borderColor: "divider" }}>
          <TabList variant="scrollable" onChange={handleChange}>
            <Tab label="Daily Stats" value="1" />
            <Tab label="Cumulative Stats" value="2" />
          </TabList>
        </Box>
        <TabPanel sx={{ paddingRight: 0, paddingLeft: 0 }} value="1">
          <ChartTabPanel
            field={dailyField}
            chartType={dailyChartType}
            fieldsList={["cases", "deaths"]}
            region={region}
            regionType={regionType}
            data={data}
            handleFieldChange={setDailyField}
            handleChartTypeChange={setDailyChartType}
          />
        </TabPanel>
        <TabPanel sx={{ paddingRight: 0, paddingLeft: 0 }} value="2">
          <ChartTabPanel
            field={cumField}
            chartType={cumChartType}
            fieldsList={["Cumulative Cases", "Cumulative Deaths"]}
            region={region}
            regionType={regionType}
            data={data}
            handleFieldChange={setCumField}
            handleChartTypeChange={setCumChartType}
          />
        </TabPanel>
      </TabContext>
    </Box>
  );
};

export default memo(ChartsTab);
