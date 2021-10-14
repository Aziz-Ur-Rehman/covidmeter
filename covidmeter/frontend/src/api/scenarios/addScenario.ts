import backend from "../axios.config";

const addScenarioRequest = async (
  scenario_data: any,
  token: string | null
): Promise<any> => {
  const response: any = await backend.post(`/api/scenario/`, scenario_data, {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  });

  if (response.status === 201) {
    return response.data;
  } else {
    throw new Error(response);
  }
};

export default addScenarioRequest;
