import { createAsyncThunk, createSlice } from "@reduxjs/toolkit";
import graphDataRequest from "../../../api/graph/graph-data";

export const fetchWorldGraphDataAction: any = createAsyncThunk(
  "world-graph-data/fetchWorldGraphData",
  async () => {
    const response = await graphDataRequest();
    return response;
  }
);

export const worldGraphDataSlice = createSlice({
  name: "world-graph-data",
  initialState: { graphData: { data: [] } },
  reducers: {},
  extraReducers: {
    [fetchWorldGraphDataAction.pending]: (state: any) => {},
    [fetchWorldGraphDataAction.fulfilled]: (state: any, action) => {
      state.graphData = action.payload;
    },
    [fetchWorldGraphDataAction.rejected]: (state: any) => {},
  },
});
