<script>
    import { slide } from 'svelte/transition';
    import { UserSettingsOutline, PhoneOutline, TrashBinOutline } from 'flowbite-svelte-icons';
    import {Button} from "flowbite-svelte";
    import {filteredCompanies, companiesStore, searchValue} from "../../routes/store.js";

    export let setPage;

    export let currentPage;

    function handleClick(page) {
        setPage(page);
    }

    $: $filteredCompanies = $companiesStore.filter(company =>
        company.name.toLowerCase().includes($searchValue)
    );

    const toggleManage = (index) => {
        $filteredCompanies[index].isOpen = !$filteredCompanies[index].isOpen;
    };

    const callCompany = (companyName) => {
        alert(`Calling ${companyName}...`);
    };

    const deleteContract = (contractName) => {
        alert(`Deleting ${contractName}...`);
    };

    const viewInvoices = (contractName) => {
        alert(`Viewing invoices for ${contractName}...`);
    };

    function viewModal(id) {
        console.log(id);
    }
</script>

<div class="space-y-5 mt-10 font-main">
    {#each $filteredCompanies as company, index}
        <div class="bg-darkBlue p-5 rounded-lg shadow-md">
            <div class="flex items-center justify-between">
                <div class="flex items-center gap-5">
                    <img src={company.icon} alt="Company Icon" class="w-16 h-16 rounded-full"/>
                    <div class="text-xl font-semibold text-white">{company.name}</div>

                </div>
                <div class="flex">
                    <div class="flex mr-10 gap-10 justify-between">
                        <div class="flex-col">
                            <div class="text-xl font-semibold text-gray-500 font-mono">Pending: {company.invoices[0].pending}</div>
                            <div class="text-xl font-semibold text-gray-500 font-mono">Total: {company.invoices[0].sum} {company.invoices[0].currency}</div>
                        </div>

                        <div class="flex-col">
                            <div class="text-xl font-semibold text-red-500 font-mono">Overdue: {company.invoices[2].overdue}</div>
                            <div class="text-xl font-semibold text-red-500 font-mono">Total: {company.invoices[2].sum} {company.invoices[2].currency}</div>
                        </div>

                        <div class="flex-col">
                            <div class="text-xl font-semibold text-green-500 font-mono">Paid: {company.invoices[1].paid}</div>
                            <div class="text-xl font-semibold text-green-500 font-mono">Total: {company.invoices[1].sum} {company.invoices[1].currency}</div>
                        </div>
                    </div>

                    <Button
                            on:click={() => toggleManage(index)}
                            class="flex items-center gap-2 p-2 text-white hover:text-primary transition"
                    >
                        <UserSettingsOutline class="w-6 h-6"/>
                        Manage
                    </Button>
                </div>
            </div>

            {#if company.isOpen}
                <div class="mt-4 p-4 bg-darkBlue rounded-lg border-2 border-lightGray" transition:slide>
                    <div class="text-lg font-semibold text-white">Contracts for {company.name}</div>
                    <div class="space-y-4 mt-3">
                        {#each company.contracts as contract}
                            <div class="p-3 bg-lightBlue rounded-lg shadow-sm">
                                <div class="flex justify-between items-center">
                                    <div>
                                        <div class="text-white text-md font-semibold">{contract.name}</div>
                                        <div class="text-sm text-gray-200">Created: {contract.createdAt}</div>
                                        <div class="text-sm text-gray-200">Revenue: {contract.revenue}</div>
                                    </div>
                                    <div class="flex gap-2">
                                        <Button
                                                on:click={() => callCompany(company.name)}
                                                class="p-2 text-blue-300 hover:bg-blue-400 rounded-full"
                                                color="info"
                                                pill
                                        >
                                            <PhoneOutline class="w-6 h-6"/>
                                        </Button>
                                        <Button
                                                on:click={() => deleteContract(contract.name)}
                                                class="p-2 text-red-300 hover:bg-red-400 rounded-full"
                                                color="failure"
                                                pill
                                        >
                                            <TrashBinOutline class="w-6 h-6"/>
                                        </Button>
                                    </div>
                                </div>
                                <div class="flex gap-5">
                                    <Button class="mt-5"
                                            on:click={() => viewInvoices(contract.name)}>
                                        View Invoices
                                    </Button>
                                    <Button outline class="mt-5"
                                            on:click={() => viewModal(contract.id)}>
                                        View Contract
                                    </Button>
                                </div>
                            </div>
                        {/each}
                    </div>
                </div>
            {/if}
        </div>
    {/each}
</div>
