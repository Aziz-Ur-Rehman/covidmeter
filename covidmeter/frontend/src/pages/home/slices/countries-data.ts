import { createAsyncThunk, createSlice } from "@reduxjs/toolkit";
import countryRequest from "../../../api/covid/country";

export const fetchCountriesDataAction: any = createAsyncThunk(
  "countries-data/fetchCountriesData",
  async () => {
    const response = await countryRequest();
    return response;
  }
);

export const countriesDataSlice = createSlice({
  name: "countries-data",
  initialState: { countries: [] },
  reducers: {},
  extraReducers: {
    [fetchCountriesDataAction.pending]: (state: any) => {},
    [fetchCountriesDataAction.fulfilled]: (state: any, action) => {
      state.countries = action.payload;
    },
    [fetchCountriesDataAction.rejected]: (state: any) => {},
  },
});
