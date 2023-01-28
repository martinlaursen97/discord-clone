<script>
    import { onMount } from "svelte";
    import { selectedServer } from "../stores";
    export let server;

    let selectedServerId = 0;

    function selectServer() {
        localStorage.setItem("selectedServerId", server.id);
        selectedServerId = server.id;
        selectedServer.set(server.id);
    }

    onMount(() => {
        const storageServerId = parseInt(
            localStorage.getItem("selectedServerId")
        );
        selectedServer.set(storageServerId);
        selectedServerId = parseInt(localStorage.getItem("selectedServerId"));
    });
</script>

{#if selectedServerId}
    {#if selectedServerId === server.id && $selectedServer == server.id}
        <button
            class="relative flex items-center justify-center text-xl h-16 w-16 mt-2  mx-auto shadow-lg bg-orange-400 text-white hover:bg-orange-500 rounded-3xl hover:rounded-xl transition-all duration-200 ease-linear cursor-pointer"
        >
            {server.name}
        </button>
    {:else}
        <button
            class="relative flex items-center justify-center text-xl h-16 w-16 mt-2  mx-auto shadow-lg bg-slate-500 text-white hover:bg-orange-400 rounded-3xl hover:rounded-xl transition-all duration-200 ease-linear cursor-pointer"
            on:click={selectServer}
        >
            {server.name}
        </button>
    {/if}
{/if}
