import React, { FC } from "react";
import { BrowserRouter, Route, Switch } from "react-router-dom";
import Home from "../pages/home";
import Login from "../pages/login";
import ScenarioDetail from "../pages/scenario-detail";
import Scenarios from "../pages/scenarios";
import Signup from "../pages/signup";

const Router: FC = () => {
  return (
    <BrowserRouter>
      <Switch>
        <Route path="/signup">
          <Signup />
        </Route>
        <Route path="/login">
          <Login />
        </Route>
        <Route path="/scenario-detail">
          <ScenarioDetail />
        </Route>
        <Route path="/scenarios">
          <Scenarios />
        </Route>
        <Route path="/">
          <Home />
        </Route>
      </Switch>
    </BrowserRouter>
  );
};

export default Router;
