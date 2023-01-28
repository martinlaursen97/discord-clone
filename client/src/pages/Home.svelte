<script>
    import { onMount } from "svelte";
    import SideBar from "../components/SideBar.svelte";
    import { getCurrentUser } from "../api/crud";
    import { servers } from "../stores";

    onMount(async () => {
        servers.set((await getCurrentUser()).servers);
    });
</script>

<SideBar servers={$servers} />
