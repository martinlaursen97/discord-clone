import { writable } from 'svelte/store';

export const token = writable(document.cookie);
export const BASE_URL = 'http://127.0.0.1:8000'
