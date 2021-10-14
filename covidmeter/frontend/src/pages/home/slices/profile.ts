import { createAsyncThunk, createSlice } from "@reduxjs/toolkit";
import userProfileRequest from "../../../api/auth/user-profile";

export const setUserProfileAction: any = createAsyncThunk(
  "profile/setUserProfile",
  async () => {
    let access_token = localStorage.getItem("access");
    if (access_token) {
      const response = await userProfileRequest(access_token);
      return response;
    }
  }
);

export const userProfileSlice = createSlice({
  name: "profile",
  initialState: { user: {} },
  reducers: {},
  extraReducers: {
    [setUserProfileAction.pending]: (state: any) => {},
    [setUserProfileAction.fulfilled]: (state: any, action) => {
      state.user = action.payload;
    },
    [setUserProfileAction.rejected]: (state: any) => {},
  },
});
