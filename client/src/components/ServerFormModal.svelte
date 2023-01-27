<script>
    import { Modal, Label, Input } from "flowbite-svelte";
    import { create } from "../api/crud";
    import { current_user } from "../stores";
    import { get } from "svelte/store";

    let formModal = false;
    let serverName = "";

    async function createServer() {
        let newObject = await create("servers", { name: serverName });
        let currentUser = get(current_user);

        currentUser.servers = [...currentUser.servers, newObject];
        current_user.set(currentUser);

        formModal = false;
        return newObject;
    }
</script>

<button
    on:click={() => (formModal = true)}
    class="relative flex items-center justify-center text-xl h-16 w-16 mt-2  mx-auto shadow-lg bg-orange-400 text-white hover:bg-orange-500 rounded-3xl hover:rounded-xl transition-all duration-200 ease-linear cursor-pointer"
    >+</button
>
<Modal bind:open={formModal} size="xs" autoclose={false} class="w-full">
    <form class="flex flex-col space-y-6" action="#">
        <h3 class="text-xl font-medium text-gray-900 p-0">
            Enter server details
        </h3>
        <Label class="space-y-2">
            <span>Server name</span>
            <Input
                type="text"
                name="name"
                bind:value={serverName}
                placeholder="..."
                required
            />
        </Label>
        <button
            class="relative flex items-center justify-center text-xl h-12 w-full mt-2  mx-auto shadow-lg bg-slate-500 text-white hover:bg-orange-400 rounded-lg transition-all duration-200 ease-linear cursor-pointer"
            type="button"
            on:click|preventDefault={createServer}
        >
            Create server
        </button>
    </form>
</Modal>
