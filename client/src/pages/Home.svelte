<script>
    import SideBar from "../components/SideBar.svelte";
    import { BASE_URL } from "../stores";

    const servers = [1, 2, 3];
</script>

<SideBar {servers} />
