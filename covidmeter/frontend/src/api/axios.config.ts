import axios from "axios";
import { API_BASE_URL } from "../config";

const backend = axios.create({
  baseURL: API_BASE_URL,
});

export default backend;
