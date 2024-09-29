<script>
    import Menu from "../../components/dashboard/Menu.svelte";
    import Dashboard from "../../components/dashboard/Dashboard.svelte";
    import Clients from "../../components/dashboard/Clients.svelte";
    import Invoices from "../../components/dashboard/Invoices.svelte";
    import Contracts from "../../components/dashboard/Contracts.svelte";
    import Payments from "../../components/dashboard/Payments.svelte";
    import DataEditor from "../../components/dashboard/DataEditor.svelte";

    let currentPage = 'dashboard';

    function setPage(page) {
        currentPage = page;
    }
</script>

<div class="h-screen w-full bg-darkBlue flex flex-col max-h-screen">
    <Menu {currentPage} {setPage} />

    {#if currentPage === 'dashboard'}
        <Dashboard />
    {/if}

    {#if currentPage === 'contracts'}
        <Contracts {currentPage} {setPage} />
    {/if}

    {#if currentPage === 'clients'}
        <Clients />
    {/if}

    {#if currentPage === 'invoices'}
        <Invoices />
    {/if}

    {#if currentPage === 'payments'}
        <Payments />
    {/if}

    {#if currentPage === 'dataeditor'}
        <DataEditor />
    {/if}
</div>
