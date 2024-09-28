<script>
    import Icon from '$lib/assets/icon.png'
    export let setPage;

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
        <button on:click={() => handleClick("dashboard")} class="mr-5 sm:mr-5 md:mr-10 lg:mr-20 text-textLightGray hover:text-white transform hover:scale-105 transition duration-100 ease-in-out hover:cursor-pointer focus:outline-none">
            Dashboard
        </button>

        <button on:click={() => handleClick("contracts")} class="mr-5 sm:mr-5 md:mr-10 lg:mr-20 text-textLightGray hover:text-white transform hover:scale-105 transition duration-100 ease-in-out hover:cursor-pointer focus:outline-none">
            Contracts
        </button>

        <button on:click={() => handleClick("invoices")} class="mr-5 sm:mr-5 md:mr-10 lg:mr-20 text-textLightGray hover:text-white transform hover:scale-105 transition duration-100 ease-in-out hover:cursor-pointer focus:outline-none">
            Invoices
        </button>

        <button on:click={() => handleClick("payments")} class="mr-5 sm:mr-5 md:mr-10 lg:mr-20 text-textLightGray hover:text-white transform hover:scale-105 transition duration-100 ease-in-out hover:cursor-pointer focus:outline-none">
            Payments
        </button>

        <button on:click={() => handleClick("clients")} class="mr-5 sm:mr-5 md:mr-10 lg:mr-20 text-textLightGray hover:text-white transform hover:scale-105 transition duration-100 ease-in-out hover:cursor-pointer focus:outline-none">
            Clients
        </button>

    </div>
</div>

<style>

</style>