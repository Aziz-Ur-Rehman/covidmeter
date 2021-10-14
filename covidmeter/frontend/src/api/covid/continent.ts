import backend from "../axios.config";

const continentRequest = async (continent_id: string = ""): Promise<any> => {
  const response: any = await backend.get(
    `/api/covid/continent/${continent_id}`
  );

  if (response.status === 200) {
    return response.data;
  } else {
    throw new Error(response);
  }
};

export default continentRequest;
