import { writable } from 'svelte/store';
import { get } from 'svelte/store';


export const BASE_URL = 'http://127.0.0.1:8000'

export const selectedServer = writable({});

export const servers = writable([]);


export const webSocket = new WebSocket(`ws://127.0.0.1:8000/posts/1/ws?token=${document.cookie.split("token=")[1]}`)

