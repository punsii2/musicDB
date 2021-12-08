<script lang="ts">
	import { Styles } from "sveltestrap";
	import Person from "./Person.svelte";
	import Nested from "./Nested.svelte";
	export let name: string;
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
	$: {
		console.log(`countA is ${countA}\n countB is ${countB}`);
	}

	let test_person_1 = {
		first_name: "John",
		last_name: "Doe",
		gender: "male",
		date_of_birth: "1.2.3.4",
		date_of_death: "5.6.7.8",
		born_in: "1999",
		memo: "my favoute person",
	};
	let test_person_2 = {
		first_name: "John",
		last_name: "Doe",
		gender: "male",
		date_of_birth: "1.2.3.4",
		born_in: "2005",
		memo: "my second favoute person",
	};
</script>

<main>
	<Styles/>
	<Person {...test_person_1} />
	<Person {...test_person_2} />
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
