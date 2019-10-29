<script>
    import Nav from '../components/Nav.svelte';
    import Footer from '../components/Footer.svelte'

    export let segment;
</script>

<style>
    @font-face {
        font-family: IBM Plex Sans;
        font-style: normal;
        font-display: swap;
        font-weight: 100;
        src: local("IBM"), local("IBM"), url(fonts/IBM_Plex_Sans/IBMPlexSans-Regular.ttf) format("ttf");
    }

    :root {
        --nav-color: #222437;
        --count: #3E4551;
    }

    .wrapper {
        display: grid;
        /*grid-template-areas: "nav nav nav" ". main ." "footer footer footer";*/
        grid-template-areas: "nav nav nav" "main main main" "footer footer footer";
        grid-template-rows: 60px 1fr 170px;
        grid-template-columns: minmax(0, 240px) repeat(auto-fill, minmax(320px, 1fr)) minmax(0, 240px);
        /*grid-template-columns: auto minmax(320px, 1050px) auto;*/
        height: 100vh;
        width: 100%;
        margin: 0;
    }
</style>

<div class="wrapper">
    <Nav {segment}/>
    <slot></slot>
    <Footer/>
</div>
