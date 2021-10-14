import { createAsyncThunk, createSlice } from "@reduxjs/toolkit";
import graphDataRequest from "../../../api/graph/graph-data";

export const fetchCountryGraphDataAction: any = createAsyncThunk(
  "country-graph-data/fetchCountryGraphData",
  async (country_geoid: string) => {
    const response = await graphDataRequest(`country/${country_geoid}`);
    return response;
  }
);

export const countryGraphDataSlice = createSlice({
  name: "country-graph-data",
  initialState: { graphData: { data: [] } },
  reducers: {},
  extraReducers: {
    [fetchCountryGraphDataAction.pending]: (state: any) => {},
    [fetchCountryGraphDataAction.fulfilled]: (state: any, action) => {
      state.graphData = action.payload;
    },
    [fetchCountryGraphDataAction.rejected]: (state: any) => {},
  },
});
