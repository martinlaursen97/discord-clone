
import { token, BASE_URL } from "../stores";
import { get } from 'svelte/store';
import axios from "axios";


export async function getCurrentUser() {
    const value = get(token)
    try {
        const res = await axios.post(
            `${BASE_URL}/auth/current-user`,
            null,
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
