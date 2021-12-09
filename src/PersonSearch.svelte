<script lang="ts">
    import Person from "./Person.svelte";

    export let persons: Object[];
</script>

{#each persons as person}
    <Person {...person} /><br />
{/each}

<style>
</style>
