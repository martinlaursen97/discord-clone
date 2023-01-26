<script>
  import { Route, Router } from "svelte-navigator";
  import ProtectedRoute from "./components/auth/ProtectedRoute.svelte";
  import Login from "./pages/Login.svelte";
  import Home from "./pages/Home.svelte";
</script>

<main class="bg-slate-700 w-full">
  <Router>
    <ProtectedRoute path="/" component={Home} />
    <Route path="/login"><Login /></Route>
  </Router>
</main>
