<script>
    import { onMount } from "svelte";
    import { webSocket } from "../stores";

    let message = "";

    async function createPost() {
        webSocket.send(message);
        message = "";
    }

    onMount(async () => {
        document
            .getElementById("large-input")
            .addEventListener("keyup", function (event) {
                event.preventDefault();
                if (event.key === "Enter" && message.length > 0) {
                    createPost();
                }
            });
    });
</script>

<div class="mt-80 ml-32 mr-80">
    <input
        type="text"
        id="large-input"
        class="block w-full p-4 text-gray-900 border border-gray-300 rounded-lg bg-gray-50 sm:text-md focus:ring-blue-500 focus:border-blue-500"
        bind:value={message}
        on:submit|preventDefault={createPost}
    />
</div>

{message}
