import React, { FC, useEffect, useState } from "react";
import { RootStateOrAny, useDispatch, useSelector } from "react-redux";
import { useHistory } from "react-router";
import loginRequest from "../../api/auth/login";
import signupRequest from "../../api/auth/signup";
import SignupForm from "../../components/SignupForm";
import validateSignUpForm from "../../utils/validator";
import { fetchCountriesDataAction } from "../home/slices/countries-data";

const Signup: FC = () => {
  const userInitialState = {
    email: "",
    first_name: "",
    last_name: "",
    date_of_birth: "",
    profile_picture: "",
    country: "",
    password: "",
    confirm_password: "",
  };

  const countries = useSelector(
    (state: RootStateOrAny) => state.countriesData.countries
  );

  const dispatch = useDispatch();

  const [user, setUser] = useState(userInitialState);
  const [errors, setErrors] = useState(userInitialState);
  const [message, setMessage] = useState<string>("");
  const [image, setImage] = useState<any>();
  const history = useHistory();

  useEffect(() => {
    localStorage.removeItem("access");
    localStorage.removeItem("refresh");
    if (!countries.length) dispatch(fetchCountriesDataAction());
    // eslint-disable-next-line
  }, []);

  const handleChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    if (event.target.name === "profile_picture" && event.target.files) {
      setImage(event.target.files[0]);
    }

    setUser((prev) => ({
      ...prev,
      [event.target.name]: event.target.value,
    }));
  };

  const onSubmit = () => {
    const user_info = Object.assign({}, user);
    const form_data = new FormData();

    Object.entries(user_info)
      .filter(([key, value]) => key !== "profile_picture")
      // eslint-disable-next-line
      .map(([key, value]) => {
        form_data.append(key, value);
      });

    if (user_info.profile_picture === "") {
      user_info.profile_picture = "";
    } else {
      form_data.append("profile_picture", image, user_info.profile_picture);
    }

    signupRequest(form_data)
      .then((response) => {
        const { email, password } = user_info;
        loginRequest({ email, password })
          .then((login_response) => {
            history.push("/");
          })
          .catch((err) => {});
      })
      .catch((err) => {
        if (err.response.status === 400) {
          setErrors(err.response.data);
        } else {
          setMessage(err.message);
        }
      });
  };

  const validateForm = (event: React.ChangeEvent<HTMLInputElement>) => {
    event.preventDefault();
    var payload = validateSignUpForm(user);
    if (payload.success) {
      setMessage("");
      setErrors(userInitialState);

      onSubmit();
    } else {
      setErrors(payload.errors);
    }
  };

  return (
    <SignupForm
      user={user}
      errors={errors}
      message={message}
      countries={countries}
      onChange={handleChange}
      onSubmit={validateForm}
    />
  );
};

export default Signup;
