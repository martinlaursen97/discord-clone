import { writable } from 'svelte/store';

export const BASE_URL = 'http://127.0.0.1:8000'
export const token = writable(document.cookie);
export const current_user = writable({});
export const selectedServer = writable({});
