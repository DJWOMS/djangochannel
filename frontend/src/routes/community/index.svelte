<script context="module">
    export function preload({params, query}) {
        return this.fetch(`http://127.0.0.1:8000/api/v2/groups/`).then(r => r.json()).then(groups => {
            return {groups};
        });
    }
</script>

<script>
    export let groups;
</script>


<svelte:head>
    <title>Сообщества</title>
</svelte:head>

<main class="main">
    <h1>Группы</h1>
    <div class="groups">
        {#each groups.results as group}
            <div class="block-group">
                <img class="miniature" src="{group.miniature}" alt="{group.title}">
                <h2><a rel='prefetch' href='community/{group.id}'>{group.title}</a></h2>
                <div class="group-desc">{group.desc}</div>
            </div>
        {/each}
    </div>
    <div class="sidebar">
        <form>
            <input value="" placeholder="Поиск">
        </form>
    </div>
</main>


<style>
    .main {
        display: grid;
        grid-template-columns: minmax(0, 240px) 2fr 1fr minmax(0, 240px);
        grid-template-rows: 60px repeat(auto-fit, 150px);
        grid-area: main;
        grid-column-gap: 15px;
    }

    h1 {
        background-color: #fff;
        line-height: unset;
        grid-column: 1 / -1;
        text-align: center;
        margin: 0;
    }

    .groups {
        grid-column: 2 / 3;
    }

    .block-group {
        display: grid;
        grid-template-columns: 1fr 5fr;
        grid-template-rows: 50px 100px;
        grid-gap: 15px;
        background-color: #fff;
        border: 1px solid #2222221f;
        padding: 25px;
    }

    .block-group h2 a:hover {
        box-shadow: 1px 1px #cbcbcb;
    }

    .miniature {
        width: 50px;
        height: 50px;
        border-radius: 50%;
        border: 1px solid #22222238;
    }

    .group-desc {
        grid-column: 1 / 3;
        font-size: 14px;
    }

    .sidebar {
        grid-column: 3 / 4;
    }
</style>