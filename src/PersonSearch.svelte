<script lang="ts">
    import { Container, Input, Table } from "sveltestrap";

    import Person from "./Person.svelte";
    export let persons: Person[];

    let searchText: string = "";
    let selectedPersonId: number = null;
    const showPerson = (id: number) => {
        console.log("showPerson called");
        if (id === selectedPersonId) {
            selectedPersonId = null;
        } else {
            selectedPersonId = id;
        }
    };
</script>

<br />
<Input bind:value={searchText} placeholder="filter text..." />
<Table hover>
    <thead>
        <tr>
            <th>Id</th>
            <th>First Name</th>
            <th>Last Name</th>
            <th>Born</th>
        </tr>
    </thead>
    <tbody>
        {#each persons as person}
            {#if JSON.stringify(person)
                .toLowerCase()
                .includes(searchText.toLowerCase())}
                <tr on:click={showPerson(person.id)}>
                    <th>{person.id}</th>
                    <th>{person.first_name}</th>
                    <th>{person.last_name}</th>
                    <th>{person.date_of_birth}</th>
                </tr>
                {#if person.id === selectedPersonId}
                    <th colspan="100%">
                        <Person {...person} />
                    </th>
                {/if}
            {/if}
        {/each}
    </tbody>
</Table>

<style>
</style>
