import React, { Fragment, FC, memo } from "react";
import Box from "@mui/material/Box";
import Drawer from "@mui/material/Drawer";
import List from "@mui/material/List";
import Divider from "@mui/material/Divider";
import ListItem from "@mui/material/ListItem";
import ListItemIcon from "@mui/material/ListItemIcon";
import ListItemText from "@mui/material/ListItemText";
import DashboardIcon from "@mui/icons-material/Dashboard";
import StyledLink from "../styledLink";
import LoginIcon from "@mui/icons-material/Login";
import AppRegistrationIcon from "@mui/icons-material/AppRegistration";
import LogoutIcon from "@mui/icons-material/Logout";
import CompareIcon from "@mui/icons-material/Compare";

interface SiderDrawerProps {
  user: any;
  open: boolean;
  toggleDrawer: (open: boolean) => void;
}

const SideDrawer: FC<SiderDrawerProps> = ({ user, open, toggleDrawer }) => {
  const list = () => (
    <Box
      role="presentation"
      onClick={() => {
        toggleDrawer(false);
      }}
      onKeyDown={() => {
        toggleDrawer(false);
      }}
    >
      <List>
        <ListItem component={StyledLink} to="/">
          <ListItemIcon>
            <DashboardIcon />
          </ListItemIcon>
          <ListItemText primary={"Dashboard"} />
        </ListItem>
      </List>
      <Divider />
      {user && user.email ? (
        <List>
          <ListItem component={StyledLink} to="/scenarios">
            <ListItemIcon>
              <CompareIcon />
            </ListItemIcon>
            <ListItemText primary={"Scenarios"} />
          </ListItem>
          <ListItem component={StyledLink} to="/login">
            <ListItemIcon>
              <LogoutIcon />
            </ListItemIcon>
            <ListItemText primary={"Logout"} />
          </ListItem>
        </List>
      ) : (
        <List>
          <ListItem component={StyledLink} to="/login">
            <ListItemIcon>
              <LoginIcon />
            </ListItemIcon>
            <ListItemText primary={"Login"} />
          </ListItem>
          <ListItem component={StyledLink} to="/signup">
            <ListItemIcon>
              <AppRegistrationIcon />
            </ListItemIcon>
            <ListItemText primary={"Signup"} />
          </ListItem>
        </List>
      )}
    </Box>
  );

  return (
    <Fragment>
      <Drawer
        open={open}
        onClose={() => {
          toggleDrawer(false);
        }}
      >
        {list()}
      </Drawer>
    </Fragment>
  );
};

export default memo(SideDrawer);
