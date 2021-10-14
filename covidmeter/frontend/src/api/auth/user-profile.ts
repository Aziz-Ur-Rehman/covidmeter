import backend from "../axios.config";

const userProfileRequest = async (token: string): Promise<any> => {
  const response: any = await backend.get("/api/user/profile/", {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  });

  if (response.status === 200) {
    return response.data;
  } else {
    throw new Error(response);
  }
};

export default userProfileRequest;
