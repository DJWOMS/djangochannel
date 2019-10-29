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

<style>
    .main {
        grid-template-rows: 60px repeat(auto-fit, 150px);
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

</style>

<svelte:head>
    <title>Сообщества</title>
</svelte:head>

<main class="main">
    <h1>Группы</h1>
    <div class="groups">
        {#each groups.results as group}
            <div>
                <img src="{group.miniature}" alt="{group.title}">
                <h2><a rel='prefetch' href='community/{group.id}'>{group.title}</a></h2>
            </div>
        {/each}
    </div>
</main>
