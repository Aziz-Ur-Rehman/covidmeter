import backend from "../axios.config";

const updateScenarioRequest = async (
  scenario_id: number,
  scenario_data: any,
  token: string | null
): Promise<any> => {
  const response: any = await backend.patch(
    `/api/scenario/${scenario_id}/`,
    scenario_data,
    {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    }
  );

  if (response.status === 200) {
    return response.data;
  } else {
    throw new Error(response);
  }
};

export default updateScenarioRequest;
