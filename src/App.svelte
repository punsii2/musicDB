<script lang="ts">
    import { Router, Link, Route } from "svelte-routing";
    import { Styles } from "sveltestrap";
    import { Nav, NavItem, NavLink } from "sveltestrap";

    import PersonSearch from "./PersonSearch.svelte";
    import persons from "./testdata/persons.json";
    import WorkSearch from "./WorkSearch.svelte";
    import works from "./testdata/works.json";

    // needed for routing
    //export let to = "";
    //function getProps({ location, href, isPartiallyCurrent, isCurrent }) {
    //    const isActive =
    //        href === "/" ? isCurrent : isPartiallyCurrent || isCurrent;

    //    // The object returned here is spread on the anchor element's attributes
    //    if (isActive) {
    //        return { class: "active" };
    //    }
    //    return {};
    //}
    export let url = "";
    export let name: string;
</script>

<Router {url}>
    <Styles />
    <Nav tabs>
        <NavItem>
            <Link to="/"> {name} </Link>
        </NavItem>
        <NavItem>
            <Link to="Person"> Person </Link>
        </NavItem>
        <NavItem>
            <Link to="Work">Work</Link>
        </NavItem>
    </Nav>

    <main>
        <Route path="Person" component={PersonSearch} {persons} />
        <!--<Route path="Person/:id" component={Person} />-->
        <Route path="Work" component={WorkSearch} />
        <!--<Route path="Work/:id" component={WorkSearch} />-->
    </main>
</Router>

<style>
    :global(body) {
        background-image: url("http://sfwallpaper.com/images/website-background-6.jpg");
        background-repeat: repeat;
    }

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
