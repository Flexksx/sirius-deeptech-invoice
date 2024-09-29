<script>
    import {Search, Button} from 'flowbite-svelte';
    import {SearchOutline, PlusOutline} from 'flowbite-svelte-icons';
    import { slide } from 'svelte/transition';
    import { Dropzone } from 'flowbite-svelte';
    import ContractList from "../managing/ContractList.svelte";
    import {searchValue} from "../../routes/store.js";
    import { Modal } from 'flowbite-svelte';
    import {quintOut} from "svelte/easing";

    let defaultModal = false;
    let value = [];
    const dropHandle = (event) => {
        value = [];
        event.preventDefault();
        if (event.dataTransfer.items) {
            [...event.dataTransfer.items].forEach((item, i) => {
                if (item.kind === 'file') {
                    const file = item.getAsFile();
                    value.push(file.name);
                    value = value;
                }
            });
        } else {
            [...event.dataTransfer.files].forEach((file, i) => {
                value = file.name;
            });
        }
    };

    const handleChange = (event) => {
        const files = event.target.files;
        if (files.length > 0) {
            value.push(files[0].name);
            value = value;
        }
    };

    const showFiles = (files) => {
        return files.length + " file(s) selected.";
    };

    let visible = false;

</script>

<div in:slide={{duration: 100, easing: quintOut, axis: 'x' }} class="flex-1 overflow-y-auto flex flex-col min-h-0 m-5 lg:m-15 lg:p-10 md:p-5 sm:p-5 p-5 md:m-10 sm:m-5 bg-lightBlue rounded-2xl">
    <div class="flex items-center justify-between flex-wrap">
        <div class="flex gap-3 justify-center items-center">
            <div class="text-white font-main text-6xl">Contracts</div>
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

    {#if visible}
        <div class="mt-5 p-5 rounded-lg flex flex-col justify-center items-center" transition:slide>
            <Dropzone
                    class="bg-lightBlue hover:bg-darkBlue max-w-2xl"
                    id="dropzone"
                    on:drop={dropHandle}
                    on:dragover={(event) => {event.preventDefault();}}
                    on:change={handleChange}>
                <svg aria-hidden="true" class="mb-3 w-10 h-10 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12" /></svg>
                {#if value.length === 0}
                    <p class="mb-2 text-sm text-white dark:text-white"><span class="font-semibold">Click to upload</span> or drag and drop</p>
                    <p class="text-xs text-white dark:text-white">SVG, PNG, JPG or GIF (MAX. 800x400px)</p>
                {:else}
                    <p class="text-white">{showFiles(value)}</p>
                {/if}
            </Dropzone>
            <div class="mt-3 flex flex-1 gap-3">
                <Button outline color="red">Cancel</Button>
                <Button outline>Confirm</Button>
            </div>
        </div>
    {/if}

    <div>
        <ContractList />
    </div>
</div>

<Modal title="Upload Contract" classHeader="bg-lightBlue" classBody="border-lightGray" classFooter="bg-lightBlue" classBackdrop="bg-lightGray" class="bg-darkBlue border-lightGray" size="lg" bind:open={defaultModal} autoclose>
    <div class="mt-5 p-5 rounded-lg flex flex-col justify-center items-center" transition:slide>
        <Dropzone
                class="bg-lightBlue hover:bg-darkBlue max-w-2xl"
                id="dropzone"
                on:drop={dropHandle}
                on:dragover={(event) => {event.preventDefault();}}
                on:change={handleChange}>
            <svg aria-hidden="true" class="mb-3 w-10 h-10 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12" /></svg>
            {#if value.length === 0}
                <p class="mb-2 text-sm text-gray-500 dark:text-gray-400"><span class="font-semibold">Click to upload</span> or drag and drop</p>
                <p class="text-xs text-gray-500 dark:text-gray-400">SVG, PNG, JPG or GIF (MAX. 800x400px)</p>
            {:else}
                <p>{showFiles(value)}</p>
            {/if}
        </Dropzone>
    </div>
     <svelte:fragment slot="footer">
         <Button outline color="red">Cancel</Button>
         <Button outline>Confirm</Button>
    </svelte:fragment>
</Modal>

<div class="absolute bottom-5 right-5">
    <Button
            on:click={() => (defaultModal = true)}
            pill={true}
            class="w-16 h-16 text-3xl font-bold rounded-full flex items-center justify-center">
        <PlusOutline />
    </Button>
</div>