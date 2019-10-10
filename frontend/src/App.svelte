<div class="wrapper">
    <Nav></Nav>
    <main class="main">
        <svelte:component this={currentSelection} />
		<button on:click="{enter}">login</button>
    </main>
    <Footer></Footer>
</div>


<script>
    import Nav from './components/Nav.svelte'
    import Footer from './components/Footer.svelte'
	import Profile from './components/Profile.svelte'
	import Login from './components/Login.svelte'

	let currentSelection = Profile

	function enter() {
    	currentSelection = Login
	}
</script>


<style>
    :root {
        --nav-color: #222437;
        --count: #3E4551;
    }

    body {
        margin: 0;
        padding: 0;
        background-color: #F9F9F9;
        font-family: 'IBM Plex Sans', sans-serif;
    }

    .wrapper {
        display: grid;
        grid-template-areas: "nav nav nav" ". main ." "footer footer footer";
        grid-template-rows: 60px 1fr 170px;
        grid-template-columns: minmax(0, 240px) repeat(auto-fill, minmax(320px, 1fr)) minmax(0, 240px);
        /*grid-template-columns: auto minmax(320px, 1050px) auto;*/
        height: 100vh;
        width: 100%;
        margin: 0;
    }

    .main {
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
        grid-area: main;
        /*max-width: 1050px;*/
        /*border: 1px solid #000;*/
    }
</style>


