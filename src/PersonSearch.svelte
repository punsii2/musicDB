<script lang="ts">
    import {
        FormGroup,
        Label,
        Input,
        ListGroup,
        ListGroupItem,
    } from "sveltestrap";

    import Person from "./Person.svelte";

    export let persons: Object[];

    let search_text: string = "";
</script>

<FormGroup>
    <Label for="person_filter">Filter</Label>
    <Input
        bind:value={search_text}
        type="search"
        name="search"
        id="person_filter"
        placeholder="filter text..." />
</FormGroup>
<ListGroup>
    {#each persons as person}
        {#if JSON.stringify(person)
            .toLowerCase()
            .includes(search_text.toLowerCase())}
            <ListGroupItem>
		<!--{person.first_name} {person.last_name}-->
		<Person {...person} /><br />
            </ListGroupItem>
        {/if}
    {/each}
</ListGroup>

<style>
</style>
