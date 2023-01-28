<script>
    import axios from "axios";
    import { getCurrentUser } from "../api/crud";
    import { servers } from "../stores";

    const formData = {
        email: "",
        password: "",
    };

    async function handleSubmit() {
        try {
            const res = await axios.post(
                "http://127.0.0.1:8000/auth/login",
                `grant_type=&username=${formData.email}&password=${formData.password}&scope=&client_id=&client_secret=`
            );

            if (res.status !== 200) {
                alert("ERROR");
                return;
            }

            document.cookie = `token=${res.data.access_token}`;

            window.location.replace("/");
        } catch (err) {
            console.log(err);
        }
    }
</script>

<section>
    <div
        class="flex flex-col items-center justify-center px-6 py-8 mx-auto md:h-screen lg:py-0"
    >
        <div
            class="w-full bg-white rounded-lg shadow dark:border md:mt-0 sm:max-w-md xl:p-0"
        >
            <div class="p-6 space-y-4 md:space-y-6 sm:p-8">
                <h1
                    class="text-xl font-bold leading-tight tracking-tight text-gray-900 md:text-2xl dark:text-white"
                >
                    Sign in to your account
                </h1>
                <form class="space-y-4 md:space-y-6" action="#">
                    <div>
                        <label
                            for="email"
                            class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
                            >Your email</label
                        >
                        <input
                            type="email"
                            name="email"
                            id="email"
                            bind:value={formData.email}
                            class="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5"
                            placeholder="name@company.com"
                            required
                        />
                    </div>
                    <div>
                        <label
                            for="password"
                            class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
                            >Password</label
                        >
                        <input
                            type="password"
                            name="password"
                            id="password"
                            bind:value={formData.password}
                            placeholder="••••••••"
                            class="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5"
                            required
                        />
                    </div>

                    <button
                        type="button"
                        on:click={handleSubmit}
                        class="w-full text-white bg-slate-700 hover:bg-orange-500 focus:ring-4 focus:outline-none focus:ring-slate-200 font-medium rounded-lg text-sm px-5 py-2.5 text-center"
                        >Sign in</button
                    >
                </form>
            </div>
        </div>
    </div>
</section>
