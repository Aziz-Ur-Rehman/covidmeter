import React, { FC, useEffect, useState } from "react";
import { useHistory } from "react-router";
import loginRequest from "../../api/auth/login";
import SignInSide from "../../components/loginForm";

const Login: FC = () => {
  const [credentials, setCredentials] = useState({
    email: "",
    password: "",
  });
  const [message, setMessage] = useState<string>("");
  const history = useHistory();

  useEffect(() => {
    localStorage.removeItem("access");
    localStorage.removeItem("refresh");
  }, []);

  const handleChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setCredentials((prev) => ({
      ...prev,
      [event.target.name]: event.target.value,
    }));
  };

  const onSubmit = (event: React.ChangeEvent<HTMLInputElement>) => {
    event.preventDefault();
    setMessage("");

    const { email, password } = credentials;

    loginRequest({ email, password })
      .then((login_response) => {
        history.push("/");
      })
      .catch((err) => {
        if (err.response.status === 401) {
          setMessage(err.response.data.detail);
        } else {
          setMessage("Something went wrong!");
        }
      });
  };

  return (
    <SignInSide
      credentials={credentials}
      message={message}
      onChange={handleChange}
      onSubmit={onSubmit}
    />
  );
};

export default Login;
