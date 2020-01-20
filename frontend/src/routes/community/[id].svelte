<script context="module">
	export async function preload({ params, query }) {
		const res = await this.fetch(`http://127.0.0.1:8000/api/v2/groups/${params.id}/`);
		const data = await res.json();

		if (res.status === 200) {
			return { group: data };
		} else {
			this.error(res.status, data.message);
		}
	}
</script>

<script>
	export let group;
</script>


<svelte:head>
	<title>{group.title}</title>
</svelte:head>

<h1>{group.title}</h1>

<div class='content'>
	{#each group.entry as entry}
	<h4>{entry.title}</h4>
<!--	{@html entry.html}-->
	{/each}
</div>


<style>

</style>