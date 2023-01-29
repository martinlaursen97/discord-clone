<script>
    import { selectedServer } from "../stores";
    import { read } from "../api/crud";
    import { onDestroy } from "svelte";
    import Member from "./Member.svelte";

    let members = [];

    let unsubscribe = selectedServer.subscribe(async (value) => {
        if (typeof value === "number") {
            members = await read("users/server", value);
        }
    });

    onDestroy(unsubscribe);
</script>

<div
    class="fixed top-0 right-0 h-screen w-64 flex flex-col bg-slate-700 text-white shadow"
>
    {#each members as member}
        <Member {member} />
    {/each}
</div>
