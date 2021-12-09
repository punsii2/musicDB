<script lang="ts">
	import { Styles } from "sveltestrap";
	import Person from "./Person.svelte";
	import persons from "./persons.json";
	import Nested from "./Nested.svelte";
	export let name: string;
	console.log(persons);
	console.log(typeof(persons));
	let countA = 1;
	let countB = 1;
	let numbers = [];
	function incrementCountA() {
		countA += 1;
	}
	function incrementCountB() {
		countB += 1;
	}
	function addNumbers() {
		numbers[numbers.length] = " " + (numbers.length + 1);
		numbers[numbers.length] = " " + (numbers.length + 1);
		numbers = numbers.slice(1);
	}
</script>

<main>
	<Styles />
	{#each persons as person}
		<Person {...person} />
	{/each}
	<button on:click={incrementCountA}> Add to A </button>
	{#if countA > numbers.length}
		<button on:click={incrementCountB}> Add to B </button>
	{/if}
	<button on:click={addNumbers}> Push to list </button>
	<Nested prop={1234} />
	<p>list: {numbers}</p>
	<h1>Hello {name}!</h1>
	<p>
		Visit the <a href="https://svelte.dev/tutorial">Svelte tutorial</a> to learn
		how to build Svelte apps.
	</p>
	<p>
		A is {countA}
	</p>
	<p>
		B is {countB}
	</p>
	<Nested prop="new text" />
</main>

<style>
	main {
		text-align: center;
		padding: 1em;
		max-width: 240px;
		margin: 0 auto;
	}

	h1 {
		color: #ff3e00;
		text-transform: uppercase;
		font-size: 4em;
		font-weight: 100;
	}

	p {
		color: purple;
		font-family: "Comic Sans MS", cursive;
		font-size: 2em;
	}

	@media (min-width: 640px) {
		main {
			max-width: none;
		}
	}
</style>
