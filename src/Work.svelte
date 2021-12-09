<script lang="ts">
    import { Button } from "sveltestrap";
    import { Modal } from "sveltestrap";
    import { Card, CardHeader, CardTitle, CardSubtitle } from "sveltestrap";

    export let id: number = undefined;
    export let type: string;
    export let title: string;
    export let subtitle: string;
    export let directory: string;
    export let directory_no: string = undefined;
    export let comp_date_from: string;
    export let comp_date_to: number;
    export let memo: string;
    export let duplicate: string;
    export let date_original: string;
    export let date_version: string;
    export let set: string;

    let showMemo: boolean = false;
    const toggleMemo = () => (showMemo = !showMemo);
</script>

<Card>
    <CardHeader>
        <CardTitle>{title}<br /></CardTitle>
        <CardSubtitle>({subtitle})</CardSubtitle>
    </CardHeader>
    Type: {type} <br />
    Directory: {directory} <br />
    Directory_no: {directory_no} <br />
    Comp date from: {comp_date_from} <br />
    Comp date to: {comp_date_to} <br />
    duplicate: {duplicate} <br />
    Date: {date_version} <br />
    Date of Original: {date_original} <br />
    Set: {set} <br />
    <Button on:click={toggleMemo}>Show Memo</Button>
    <!--<Modal body {showMemo} {toggleMemo} header="{first_name} {last_name}">
		<p>{memo}</p>
	</Modal>-->
    <Modal body header="{title} - Memo" isOpen={showMemo}>{memo}</Modal>
</Card>

<style>
</style>
