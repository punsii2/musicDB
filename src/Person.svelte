<script lang="ts">
	import { Button } from "sveltestrap";
	import { Modal } from "sveltestrap";
	import { Card, CardHeader, CardTitle } from "sveltestrap";

	export let id: number = undefined;
	export let first_name: string;
	export let last_name: string;
	export let gender: string;
	export let date_of_birth: string;
	export let date_of_death: string = undefined;
	export let born_in: string;
	export let memo: string;

	let showMemo: boolean = false;
	const toggleMemo = () => (showMemo = !showMemo);
</script>

<Card>
	<CardHeader>
		<CardTitle>{first_name} {last_name}</CardTitle>
	</CardHeader>
	First Name: {first_name} <br />
	Last Name: {last_name} <br />
	Gender: {gender} <br />
	Date of Birth: {date_of_birth} <br />
	Date of death: {date_of_death} <br />
	Born in: {born_in} <br />
	<Button on:click={toggleMemo}>Show Memo</Button>
	<!--<Modal body {showMemo} {toggleMemo} header="{first_name} {last_name}">
		<p>{memo}</p>
	</Modal>-->
	<Modal body header="{first_name} {last_name}" isOpen={showMemo}>{memo}</Modal>
	<Button color="secondary" class="spacing-bot">Delete this Person!</Button>
</Card>

<style>
</style>
