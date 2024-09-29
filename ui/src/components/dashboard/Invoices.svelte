<script>
    import { Search, Button, Badge, Indicator } from 'flowbite-svelte';
    import { SearchOutline } from 'flowbite-svelte-icons';
    import { searchValue } from "../../routes/store.js";
    import { companyInvoices, companiesStore } from "../../routes/store.js";
    import { quintOut } from "svelte/easing";
    import { slide } from 'svelte/transition';

    const cap = (string) => {
        if (!string) return '';
        return string.charAt(0).toUpperCase() + string.slice(1).toLowerCase();
    };

    const icon = (companyName) => {
        return $companiesStore.find(company => company.name === companyName);
    };
</script>

<div in:slide={{ duration: 100, easing: quintOut, axis: 'x' }} class="flex-1 overflow-y-auto flex flex-col min-h-0 m-5 lg:m-15 lg:p-10 md:p-5 sm:p-5 p-5 md:m-10 sm:m-5 bg-lightBlue rounded-2xl">
    <div class="flex items-center justify-between flex-wrap">
        <div class="flex gap-3 justify-center items-center">
            <div class="text-white font-main text-6xl">Scheduled Invoices</div>
        </div>
        <div class="mr-10">
            <form class="flex gap-2">
                <Search bind:value={$searchValue} size="md" class="bg-lightBlue border-lightGray w-96 text-white font-semibold" />
                <Button class="p-2.5">
                    <SearchOutline class="w-6 h-6" />
                </Button>
            </form>
        </div>
    </div>

    <div class="flex flex-col mt-5">
        <div class="flex p-4 rounded-lg mb-2 font-main text-white text-3xl">
            <div class="font-semibold flex-1 text-primary-700">Company</div>
            <div class="font-semibold flex-1 text-center text-primary-700">May 2024</div>
            <div class="font-semibold flex-1 text-center text-primary-700">June 2024</div>
            <div class="font-semibold flex-1 text-center text-primary-700">July 2024</div>
        </div>

        {#each $companyInvoices as company}
            <div class="flex bg-darkBlue text-white p-4 rounded-lg shadow-md mb-2 divide-x divide-lightGray">
                <div class="flex flex-1 items-center gap-5">
                    <img src={icon(company.name)?.icon} alt="Company Icon" class="w-12 h-12 rounded-full"/>
                    <h2 class="text-3xl font-semibold font-main text-white flex-1">{company.name}</h2>
                </div>


                <div class="text-center flex-1">
                    {#each company.invoices.filter(invoice => invoice.month === 'May 2024') as invoice}
                        <p class="font-semibold">
                            <Badge color={invoice.status === 'paid' ? 'green' : invoice.status === 'pending' ? 'red' : 'red'} rounded class="px-2.5 py-0.5">
                                <Indicator color={invoice.status === 'paid' ? 'green' : invoice.status === 'pending' ? 'red' : 'red'} size="xs" class="me-1" />
                                {cap(invoice.status)}
                            </Badge>
                            <span class="cursor-pointer transition-colors duration-300 hover:text-primary-700 hover:underline">
                                {invoice.amount} {invoice.currency}
                            </span>
                        </p>
                    {:else}
                        <p>No invoices</p>
                    {/each}
                </div>

                <div class="text-center flex-1">
                    {#each company.invoices.filter(invoice => invoice.month === 'June 2024') as invoice}
                        <p class="font-semibold">
                            <Badge color={invoice.status === 'paid' ? 'green' : invoice.status === 'pending' ? 'red' : 'red'} rounded class="px-2.5 py-0.5">
                                <Indicator color={invoice.status === 'paid' ? 'green' : invoice.status === 'pending' ? 'red' : 'red'} size="xs" class="me-1" />
                                {cap(invoice.status)}
                            </Badge>
                            <span class="cursor-pointer transition-colors duration-300 hover:text-primary-700 hover:underline">
                                {invoice.amount} {invoice.currency}
                            </span>
                        </p>
                    {:else}
                        <p>No invoices</p>
                    {/each}
                </div>

                <div class="text-center flex-1">
                    {#each company.invoices.filter(invoice => invoice.month === 'July 2024') as invoice}
                        <p class="font-semibold">
                            <Badge color={invoice.status === 'paid' ? 'green' : invoice.status === 'pending' ? 'red' : 'red'} rounded class="px-2.5 py-0.5">
                                <Indicator color={invoice.status === 'paid' ? 'green' : invoice.status === 'pending' ? 'red' : 'red'} size="xs" class="me-1" />
                                {cap(invoice.status)}
                            </Badge>
                            <span class="cursor-pointer transition-colors duration-300 hover:text-primary-700 hover:underline">
                                {invoice.amount} {invoice.currency}
                            </span>
                        </p>
                    {:else}
                        <p>No invoices</p>
                    {/each}
                </div>
            </div>
        {/each}
    </div>
</div>
