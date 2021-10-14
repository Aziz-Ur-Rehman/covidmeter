import React, { FC, memo } from "react";
import { Chart } from "react-google-charts";

interface ChartProps {
  title: string;
  data: any;
  chartType: any;
  colors: Array<string>;
  valueField: Array<string>;
}

const CovidChart: FC<ChartProps> = ({
  title,
  data,
  chartType,
  colors,
  valueField,
}) => {
  if (data.length > 0) {
    var column_indexes: Array<number> = valueField.map((column) => {
      return data[0].indexOf(column);
    });
  }

  return (
    <Chart
      width="100%"
      chartType={chartType}
      loader={<div>Loading Chart</div>}
      data={data.map((data_row: Array<any>) => {
        let columns_value = data_row.filter(
          (_: any, index: number) => column_indexes.indexOf(index) !== -1
        );
        return [new Date(data_row[0])].concat(columns_value);
      })}
      options={{
        title: title,
        chartArea: { width: "55%" },
        colors: colors,
      }}
      legendToggle
    />
  );
};

export default memo(CovidChart);
