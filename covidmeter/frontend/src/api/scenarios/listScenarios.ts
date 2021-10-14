import backend from "../axios.config";

const listScenariosRequest = async (token: string): Promise<any> => {
  const response: any = await backend.get(`/api/scenario/`, {
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

export default listScenariosRequest;
