<script>
    import { onDestroy } from "svelte";
    import { read } from "../api/crud";
    import { selectedServer } from "../stores";
    import Post from "./Post.svelte";
    import { webSocket } from "../stores";
    import { validate_component } from "svelte/internal";

    let posts = [];

    let unsubscribe = selectedServer.subscribe(async (value) => {
        if (typeof value === "number") {
            posts = await read("posts/server", value);
        }
    });

    webSocket.onmessage = async function (event) {
        posts = [...posts, JSON.parse(event.data)];
    };

    onDestroy(unsubscribe);
</script>

<div>
    {#each posts as post}
        <Post {post} />
    {/each}
</div>
