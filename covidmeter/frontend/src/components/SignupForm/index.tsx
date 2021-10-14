import LockOutlinedIcon from "@mui/icons-material/LockOutlined";
import React, { FC, memo } from "react";
import { createTheme, ThemeProvider } from "@mui/material/styles";
import { Link } from "react-router-dom";
import Alert from "@mui/material/Alert";
import Avatar from "@mui/material/Avatar";
import Box from "@mui/material/Box";
import Button from "@mui/material/Button";
import Container from "@mui/material/Container";
import CssBaseline from "@mui/material/CssBaseline";
import Grid from "@mui/material/Grid";
import InputLabel from "@mui/material/InputLabel";
import MenuItem from "@mui/material/MenuItem";
import Select from "@mui/material/Select";
import TextField from "@mui/material/TextField";
import Typography from "@mui/material/Typography";

interface SignInSideProps {
  user: any;
  errors: any;
  message: string;
  countries: Array<any>;
  onChange: (event: React.ChangeEvent<HTMLInputElement>) => void;
  onSubmit: (event: React.ChangeEvent<HTMLInputElement>) => void;
}

const theme = createTheme();

const SignUpSide: FC<SignInSideProps> = ({
  user,
  errors,
  message,
  countries,
  onChange,
  onSubmit,
}) => {
  return (
    <ThemeProvider theme={theme}>
      <Container component="main" maxWidth="xs">
        <CssBaseline />
        <Box
          sx={{
            marginTop: 8,
            display: "flex",
            flexDirection: "column",
            alignItems: "center",
          }}
        >
          <Avatar sx={{ m: 1, bgcolor: "secondary.main" }}>
            <LockOutlinedIcon />
          </Avatar>
          <Typography component="h1" variant="h5">
            Sign up
          </Typography>
          {message ? (
            <Alert variant="outlined" severity="info">
              {message}
            </Alert>
          ) : (
            ""
          )}
          <Box
            component="form"
            onSubmit={(event: any) => onSubmit(event)}
            sx={{ mt: 3 }}
          >
            <Grid container spacing={2}>
              <Grid item xs={12} sm={6}>
                <TextField
                  name="first_name"
                  id="first_name"
                  label="First Name"
                  error={errors.first_name ? true : false}
                  value={user.first_name}
                  helperText={errors.first_name}
                  onChange={(event: any) => onChange(event)}
                  variant="standard"
                  autoFocus
                  required
                  fullWidth
                />
              </Grid>
              <Grid item xs={12} sm={6}>
                <TextField
                  id="last_name"
                  label="Last Name"
                  name="last_name"
                  error={errors.last_name ? true : false}
                  value={user.last_name}
                  helperText={errors.last_name}
                  onChange={(event: any) => onChange(event)}
                  variant="standard"
                  required
                  fullWidth
                />
              </Grid>
              <Grid item xs={12}>
                <TextField
                  id="email"
                  label="Email Address"
                  name="email"
                  type="email"
                  error={errors.email ? true : false}
                  value={user.email}
                  helperText={errors.email}
                  onChange={(event: any) => onChange(event)}
                  variant="standard"
                  required
                  fullWidth
                />
              </Grid>
              <Grid item xs={12}>
                <TextField
                  id="date_of_birth"
                  label="Date of birth"
                  name="date_of_birth"
                  type="date"
                  error={errors.date_of_birth ? true : false}
                  value={user.date_of_birth}
                  helperText={errors.date_of_birth}
                  InputLabelProps={{ shrink: true }}
                  onChange={(event: any) => onChange(event)}
                  variant="standard"
                  required
                  fullWidth
                />
              </Grid>
              <Grid item xs={12}>
                <InputLabel id="country-label">Country</InputLabel>
                <Select
                  labelId="country-label"
                  id="country"
                  name="country"
                  error={errors.country ? true : false}
                  value={user.country}
                  onChange={(event: any) => onChange(event)}
                  fullWidth
                  label="Country"
                >
                  {countries.map((country) => {
                    return (
                      <MenuItem value={country.id}>{country.name}</MenuItem>
                    );
                  })}
                </Select>
              </Grid>
              <Grid item md={6}>
                <label htmlFor="profile_picture">Profile Picture</label>
              </Grid>
              <Grid item md={6}>
                <input
                  id="profile_picture"
                  name="profile_picture"
                  type="file"
                  accept="image/*"
                  value={user.profile_picture}
                  onChange={(event: any) => onChange(event)}
                />
              </Grid>
              <Grid item xs={12}>
                <TextField
                  name="password"
                  label="Password"
                  type="password"
                  id="password"
                  error={errors.password ? true : false}
                  value={user.password}
                  helperText={errors.password}
                  onChange={(event: any) => onChange(event)}
                  variant="standard"
                  required
                  fullWidth
                />
              </Grid>
              <Grid item xs={12}>
                <TextField
                  name="confirm_password"
                  label="Confirm Password"
                  type="password"
                  id="confirm_password"
                  error={errors.confirm_password ? true : false}
                  value={user.confirm_password}
                  helperText={errors.confirm_password}
                  onChange={(event: any) => onChange(event)}
                  variant="standard"
                  required
                  fullWidth
                />
              </Grid>
            </Grid>
            <Button
              type="submit"
              fullWidth
              variant="contained"
              sx={{ mt: 3, mb: 2 }}
            >
              Sign Up
            </Button>
            <Grid container justifyContent="flex-end">
              <Grid item>
                <Link to="/login">Already have an account? Sign in</Link>
              </Grid>
            </Grid>
          </Box>
        </Box>
      </Container>
    </ThemeProvider>
  );
};

export default memo(SignUpSide);
