<script>
  import { Route, Router } from "svelte-navigator";
  import ProtectedRoute from "./components/auth/ProtectedRoute.svelte";
  import Login from "./pages/Login.svelte";
  import Home from "./pages/Home.svelte";
</script>

<main
  class="w-full h-full mt-0 text-white bg-gray-600 min-height-screen min-width-screen absolute top-0 right-0 bottom-0 left-0"
>
  <Router>
    <ProtectedRoute path="/" component={Home} />
    <Route path="/login"><Login /></Route>
  </Router>
</main>
