import React, { useEffect } from "react";
import { RootStateOrAny, useDispatch, useSelector } from "react-redux";
import { useHistory } from "react-router";
import HeaderAppBar from "../../components/appBar";
import FullFeaturedCrudGrid from "../../components/dataTable";
import { setUserProfileAction } from "../home/slices/profile";
import { fetchScenariosAction } from "./slices/scenarios";

const Scenarios = () => {
  const user = useSelector((state: RootStateOrAny) => state.profile.user);
  const scenarios = useSelector(
    (state: RootStateOrAny) => state.scenarios.results
  );

  const dispatch = useDispatch();
  const history = useHistory();

  useEffect(() => {
    let token = localStorage.getItem("access");
    if (!token) {
      history.push("/login");
    }
    dispatch(setUserProfileAction());
    dispatch(fetchScenariosAction(token));
    // eslint-disable-next-line
  }, []);

  return (
    <div>
      <HeaderAppBar user={user} />
      <FullFeaturedCrudGrid data={scenarios} />
    </div>
  );
};

export default Scenarios;
