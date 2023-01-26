<script>
    import SideBarIcon from "./SideBarIcon.svelte";
    import SideBarNewServerIcon from "./SideBarNewServerIcon.svelte";

    export let servers;
</script>

<div
    class="fixed top-0 left-0 h-screen w-20 flex flex-col bg-slate-700 text-white shadow"
>
    {#each servers as server}
        <SideBarIcon {server} />
    {/each}
    <SideBarNewServerIcon />
</div>

<style>
</style>
