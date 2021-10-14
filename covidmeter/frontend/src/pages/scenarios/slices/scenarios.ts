import { createAsyncThunk, createSlice } from "@reduxjs/toolkit";
import listScenariosRequest from "../../../api/scenarios/listScenarios";

export const fetchScenariosAction: any = createAsyncThunk(
  "scenarios/fetchScenarios",
  async (token: string) => {
    const response = await listScenariosRequest(token);
    return response;
  }
);

export const scenarioSlice = createSlice({
  name: "scenarios",
  initialState: { results: [] },
  reducers: {},
  extraReducers: {
    [fetchScenariosAction.pending]: (state: any) => {},
    [fetchScenariosAction.fulfilled]: (state: any, action) => {
      state.results = action.payload.results;
    },
    [fetchScenariosAction.rejected]: (state: any) => {},
  },
});
