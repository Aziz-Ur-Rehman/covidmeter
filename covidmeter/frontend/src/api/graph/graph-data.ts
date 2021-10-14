import backend from "../axios.config";

const graphDataRequest = async (url_key: string = ""): Promise<any> => {
  const response: any = await backend.get(`/api/covid/graph/${url_key}`);

  if (response.status === 200) {
    return response.data;
  } else {
    throw new Error(response);
  }
};

export default graphDataRequest;
