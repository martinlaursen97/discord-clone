
import axios from "axios";
import { BASE_URL } from "../stores";


export async function getCurrentUser() {
    const value = document.cookie.split("token=")[1]

    try {
        const res = await axios.get(
            `${BASE_URL}/auth/current-user`,
            {
                headers: {
                    Authorization: `Bearer ${value}`,
                },
            }
        );
        const user = res.data;

        return user;
    } catch (err) {
        return null;
    }
}

export async function create(resource, newObject) {
    const value = document.cookie.split("token=")[1]
    try {
        const res = await axios.post(
            `${BASE_URL}/${resource}`,
            newObject,
            {
                headers: {
                    Authorization: `Bearer ${value}`,
                },

            }
        );
        const createdObject = res.data;


        return createdObject;
    } catch (err) {
        return null;
    }
}

export async function read(resource) {

}
