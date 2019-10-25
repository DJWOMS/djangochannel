<script context="module">
	export function preload({ params, query }) {
		return this.fetch(`http://127.0.0.1:8000/api/v2/groups/`).then(r => r.json()).then(groups => {
			return { groups };
		});
	}
</script>

<script>
	export let groups;
</script>

<style>

</style>

<svelte:head>
	<title>Сообщества</title>
</svelte:head>

<h1>Recent posts</h1>

<ul>
	{#each groups.results as group}

		<h2><a rel='prefetch' href='community/{group.id}'>{group.title}</a></h2>
	{/each}
</ul>