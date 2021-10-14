import { createAsyncThunk, createSlice } from "@reduxjs/toolkit";
import continentRequest from "../../../api/covid/continent";

export const fetchContinentsDataAction: any = createAsyncThunk(
  "continents-data/fetchContinentsData",
  async () => {
    const response = await continentRequest();
    return response;
  }
);

export const continentsDataSlice = createSlice({
  name: "continents-data",
  initialState: { continents: [] },
  reducers: {},
  extraReducers: {
    [fetchContinentsDataAction.pending]: (state: any) => {},
    [fetchContinentsDataAction.fulfilled]: (state: any, action) => {
      state.continents = action.payload;
    },
    [fetchContinentsDataAction.rejected]: (state: any) => {},
  },
});
