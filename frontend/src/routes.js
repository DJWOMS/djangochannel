import Profile from './components/Profile.svelte'
import Login from './components/Login.svelte'
import NotFound from './components/NotFound.svelte'

const routes = {
    '/': Profile,
    '/login' : Login,
    '*': NotFound,
};

export default routes