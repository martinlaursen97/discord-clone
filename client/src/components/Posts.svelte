<script>
    import { onDestroy } from "svelte";
    import { read } from "../api/crud";
    import { selectedServer } from "../stores";

    let posts;

    let unsubscribe = selectedServer.subscribe(async () => {
        let serverId = localStorage.getItem("selectedServerId");
        posts = await read("posts/server", serverId);
    });

    onDestroy(unsubscribe);
</script>

{JSON.stringify(posts)}
