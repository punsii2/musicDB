<script lang="ts">
    import { Styles } from "sveltestrap";
    import { TabContent, TabPane } from "sveltestrap";
    export let name: string;

    import PersonSearch from "./PersonSearch.svelte";
    import persons from "./testdata/persons.json";
    import WorkSearch from "./WorkSearch.svelte";
    import works from "./testdata/works.json";
</script>

<main>
    <Styles />

    <TabContent>
        <TabPane tabId="music" tab={name}>Hello {name}</TabPane>
        <TabPane tabId="persons" tab="persons" active>
            <PersonSearch {persons} />
        </TabPane>
        <TabPane tabId="works" tab="works">
            <WorkSearch {works} />
        </TabPane>
    </TabContent>
</main>

<style>
    main {
        text-align: center;
        padding: 1em;
        max-width: 240px;
        margin: 0 auto;
    }

    @media (min-width: 640px) {
        main {
            max-width: none;
        }
    }
</style>
