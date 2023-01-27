<script>
    import SideBar from "../components/SideBar.svelte";
    import { onMount } from "svelte";
    import { current_user } from "../stores";
    let servers = [];

    onMount(() => {
        current_user.subscribe((user) => {
            servers = user.servers;
        });
    });
</script>

<SideBar {servers} />
