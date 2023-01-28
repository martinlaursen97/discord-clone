import { writable } from 'svelte/store';

export const BASE_URL = 'http://127.0.0.1:8000'

export const selectedServer = writable({});

export const servers = writable([]);

