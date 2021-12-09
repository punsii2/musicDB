<script lang="ts">
    import { Button } from "sveltestrap";
    import { Card, CardHeader, CardTitle } from "sveltestrap";
    import { Container, Row, Col } from "sveltestrap";
    import { Icon } from "sveltestrap";
    import { Modal, ModalHeader, ModalBody } from "sveltestrap";

    export let id: number = undefined;
    export let first_name: string;
    export let last_name: string;
    export let gender: string;
    export let date_of_birth: string;
    export let date_of_death: string = undefined;
    export let born_in: string;
    export let memo: string;

    let showMemo: boolean = false;
    const toggleMemo = (): boolean => (showMemo = !showMemo);
</script>

<Card class="person-size">
    <CardHeader>
        <Container>
            <Row>
                <Col xs={{ size: 8, offset: 2 }}>
                    <CardTitle>{first_name} {last_name}</CardTitle>
                </Col>
                <Col xs={{ size: 2 }}>
                    <Button class="icon-size">
                        <Icon name="trash-fill" />
                    </Button>
                </Col>
            </Row>
        </Container>
    </CardHeader>
    <Container>
        <Row>
            <Col xs={{ size: 6 }}>Date of Birth:</Col>
            <Col>{date_of_birth}</Col>
        </Row>
        <Row>
            <Col xs={{ size: 6 }}>Date of Death:</Col>
            <Col>{date_of_death === undefined ? "--" : date_of_death}</Col>
        </Row>
        <Row>
            <Col xs={{ size: 6 }}>Born in:</Col>
            <Col>{born_in}</Col>
        </Row>
    </Container>
    <Button on:click={toggleMemo}>Show Memo</Button>
    <Modal isOpen={showMemo} toggle={toggleMemo}>
        <ModalHeader toggle={toggleMemo}
            >{first_name} {last_name} - Memo
        </ModalHeader>
        <ModalBody>
            {memo}
        </ModalBody>
    </Modal>
</Card>

<style>
    :global(.person-size) {
        width: 350px;
    }
    :global(.icon-size) {
        font-size: 10px;
    }
</style>
