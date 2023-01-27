
import { token, BASE_URL } from "../stores";
import { get } from 'svelte/store';
import axios from "axios";


export async function getCurrentUser() {
    const value = get(token)
    try {
        const res = await axios.get(
            `${BASE_URL}/auth/current-user`,
            {
                headers: {
                    Authorization: `Bearer ${value.split("token=")[1]}`,
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
    const value = get(token)
    try {
        const res = await axios.post(
            `${BASE_URL}/${resource}`,
            newObject,
            {
                headers: {
                    Authorization: `Bearer ${value.split("token=")[1]}`,
                },

            }
        );
        const createdObject = res.data;

        return createdObject;
    } catch (err) {
        return null;
    }
}
