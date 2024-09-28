<script>
    import Icon from '$lib/assets/icon.png'
    export let setPage;

    export let currentPage;

    function handleClick(page) {
        setPage(page);
    }

</script>

<div class="bg-lightBlue min-h-16 flex justify-between items-center border-b-1 border-lightGray font-main">
    <div class="first-half ml-5 flex items-center">
        <img src="{Icon}" alt="Icon" class="max-w-10 max-h-10" />
        <div class="ml-2 text-white font-medium text-3xl">Invoice.ai</div>
    </div>

    <div class="second-half flex mr-5">
        <button
                on:click={() => handleClick("dashboard")}
                class="mr-5 sm:mr-5 md:mr-10 lg:mr-20 transform hover:scale-105 transition duration-100 ease-in-out hover:cursor-pointer focus:outline-none"
                class:text-primary-700={currentPage === 'dashboard'}
                class:underline={currentPage === 'dashboard'}
                class:text-white={currentPage === 'dashboard'}
                class:text-textLightGray={currentPage !== 'dashboard'}>
            Dashboard
        </button>

        <button
                on:click={() => handleClick("contracts")}
                class="mr-5 sm:mr-5 md:mr-10 lg:mr-20 transform hover:scale-105 transition duration-100 ease-in-out hover:cursor-pointer focus:outline-none"
                class:text-primary-700={currentPage === 'contracts'}
                class:underline={currentPage === 'contracts'}
                class:text-white={currentPage === 'contracts'}
                class:text-textLightGray={currentPage !== 'contracts'}>
            Contracts
        </button>

        <button
                on:click={() => handleClick("invoices")}
                class="mr-5 sm:mr-5 md:mr-10 lg:mr-20 transform hover:scale-105 transition duration-100 ease-in-out hover:cursor-pointer focus:outline-none"
                class:text-primary-700={currentPage === 'invoices'}
                class:underline={currentPage === 'invoices'}
                class:text-white={currentPage === 'invoices'}
                class:text-textLightGray={currentPage !== 'invoices'}>
            Invoices
        </button>

        <button
                on:click={() => handleClick("payments")}
                class="mr-5 sm:mr-5 md:mr-10 lg:mr-20 transform hover:scale-105 transition duration-100 ease-in-out hover:cursor-pointer focus:outline-none"
                class:text-primary-700={currentPage === 'payments'}
                class:underline={currentPage === 'payments'}
                class:text-white={currentPage === 'payments'}
                class:text-textLightGray={currentPage !== 'payments'}>
            Payments
        </button>

        <button
                on:click={() => handleClick("clients")}
                class="mr-5 sm:mr-5 md:mr-10 lg:mr-20 transform hover:scale-105 transition duration-100 ease-in-out hover:cursor-pointer focus:outline-none"
                class:text-primary-700={currentPage === 'clients'}
                class:underline={currentPage === 'clients'}
                class:text-white={currentPage === 'clients'}
                class:text-textLightGray={currentPage !== 'clients'}>
            Clients
        </button>
    </div>
</div>

<style>

</style>