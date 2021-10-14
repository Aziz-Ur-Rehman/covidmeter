import backend from "../axios.config";

interface Credentials {
  email: string;
  password: string;
}

const loginRequest = async (credential: Credentials): Promise<any> => {
  const response: any = await backend.post("/api/token/", credential);

  if (response.status === 200) {
    localStorage.setItem("access", response.data.access);
    localStorage.setItem("refresh", response.data.refresh);

    return response.data;
  } else {
    throw new Error(response);
  }
};

export default loginRequest;
