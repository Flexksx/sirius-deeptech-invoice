<script>
    import { slide } from 'svelte/transition';
    import { UserSettingsOutline, PhoneOutline, TrashBinOutline } from 'flowbite-svelte-icons';
    import {Button} from "flowbite-svelte";
    import {filteredCompanies, companiesStore, searchValue} from "../../routes/store.js";

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
</script>

<div class="space-y-5 mt-10 font-main">
    {#each $filteredCompanies as company, index}
        <div class="bg-darkBlue p-5 rounded-lg shadow-md">
            <div class="flex items-center justify-between">
                <div class="flex items-center gap-3">
                    <img src={company.icon} alt="Company Icon" class="w-12 h-12 rounded-full"/>
                    <div class="text-xl font-semibold text-white">{company.name}</div>
                </div>
                <Button
                        on:click={() => toggleManage(index)}
                        class="flex items-center gap-2 p-2 text-white hover:text-primary transition"
                >
                    <UserSettingsOutline class="w-6 h-6"/>
                    Manage
                </Button>
            </div>

            {#if company.isOpen}
                <div class="mt-4 p-4 bg-darkBlue rounded-lg border-2 border-primary-700" transition:slide>
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
                                <Button class="mt-5"
                                        on:click={() => viewInvoices(contract.name)}>
                                    View Invoices
                                </Button>
                            </div>
                        {/each}
                    </div>
                </div>
            {/if}
        </div>
    {/each}
</div>
