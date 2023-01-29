<script>
    import { onMount } from "svelte";
    import SideBar from "../components/SideBar.svelte";
    import { getCurrentUser } from "../api/crud";
    import { servers } from "../stores";
    import Posts from "../components/Posts.svelte";
    import MembersList from "../components/MembersList.svelte";

    onMount(async () => {
        servers.set((await getCurrentUser()).servers);
    });
</script>

<SideBar servers={$servers} />
{#if localStorage.getItem("selectedServerId")}
    <Posts />
{/if}

<MembersList />
