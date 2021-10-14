import backend from "../axios.config";

const countryRequest = async (country_id: string = ""): Promise<any> => {
  const response: any = await backend.get(`/api/covid/country/${country_id}`);

  if (response.status === 200) {
    return response.data;
  } else {
    throw new Error(response);
  }
};

export default countryRequest;
