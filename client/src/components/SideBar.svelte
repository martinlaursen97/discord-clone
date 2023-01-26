<script>
    import SideBarIcon from "./SideBarIcon.svelte";

    export let data;
</script>

<div
    class="fixed top-0 left-0 h-screen w-20 flex flex-col bg-slate-700 text-white shadow"
>
    {#each data.servers as serverInformation}
        <SideBarIcon {serverInformation} />
    {/each}
</div>

<style>
</style>
