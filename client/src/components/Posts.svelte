<script>
    import { onDestroy } from "svelte";
    import { read } from "../api/crud";
    import { selectedServer } from "../stores";
    import Post from "./Post.svelte";
    let posts = [];

    let unsubscribe = selectedServer.subscribe(async (value) => {
        if (typeof value === "number") {
            posts = await read("posts/server", value);
        }
    });

    onDestroy(unsubscribe);
</script>

<div>
    {#each posts as post}
        <Post {post} />
    {/each}
</div>
