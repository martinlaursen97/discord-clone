<script>
    import SideBar from "../components/SideBar.svelte";
    import Modal from "../components/ServerFormModal.svelte";
    import { onMount } from "svelte";
    import { getCurrentUser } from "../api/crud";

    let servers = [];

    onMount(async () => {
        let user = await getCurrentUser();

        servers = user.servers;
    });
</script>

<SideBar {servers} />
