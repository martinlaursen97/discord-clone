<script>
    import { selectedServer } from "../stores";
    import { get } from "svelte/store";
    export let server;

    import { onMount } from "svelte";

    function selectServer() {
        selectedServer.set(server);
    }

    onMount(() => {
        if (!get(selectedServer).id) {
            selectedServer.set(server);
        }
    });
</script>

{#if $selectedServer}
    {#if $selectedServer.id === server.id}
        <button
            class="relative flex items-center justify-center text-xl h-16 w-16 mt-2  mx-auto shadow-lg bg-orange-400 text-white hover:bg-orange-500 rounded-3xl hover:rounded-xl transition-all duration-200 ease-linear cursor-pointer"
        >
            {server.name} 132
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
