import backend from "../axios.config";

const signupRequest = async (user_info: any): Promise<any> => {
  const response: any = await backend.post("/api/user/", user_info, {
    headers: {
      "content-type": "multipart/form-data",
    },
  });
  if (response.status === 201) {
    return response.data;
  } else {
    throw new Error(response);
  }
};

export default signupRequest;
