import { writable } from 'svelte/store';
import { getCurrentUser } from './api/crud';

export const token = writable(document.cookie);
export const BASE_URL = 'http://127.0.0.1:8000'
export const current_user = writable({})
