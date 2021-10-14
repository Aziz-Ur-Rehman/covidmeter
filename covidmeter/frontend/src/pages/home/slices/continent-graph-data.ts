import { createAsyncThunk, createSlice } from "@reduxjs/toolkit";
import graphDataRequest from "../../../api/graph/graph-data";

export const fetchContinentGraphDataAction: any = createAsyncThunk(
  "continent-graph-data/fetchContinentGraphData",
  async (continent_name: string) => {
    const response = await graphDataRequest(`continent/${continent_name}`);
    return response;
  }
);

export const continentGraphDataSlice = createSlice({
  name: "continent-graph-data",
  initialState: { graphData: { data: [] } },
  reducers: {},
  extraReducers: {
    [fetchContinentGraphDataAction.pending]: (state: any) => {},
    [fetchContinentGraphDataAction.fulfilled]: (state: any, action) => {
      state.graphData = action.payload;
    },
    [fetchContinentGraphDataAction.rejected]: (state: any) => {},
  },
});
