import backend from "../axios.config";

const DeleteScenarioRequest = async (
  scenario_id: number,
  token: string | null
): Promise<any> => {
  const response: any = await backend.delete(`/api/scenario/${scenario_id}/`, {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  });

  if (response.status === 204) {
    return response.data;
  } else {
    throw new Error(response);
  }
};

export default DeleteScenarioRequest;
