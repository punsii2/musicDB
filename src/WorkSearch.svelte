<script lang="ts">
    import Work from "./Work.svelte";

    export let works: Object[];
</script>

{#each works as work}
    <Work {...work} /><br />
{/each}

<style>
</style>
