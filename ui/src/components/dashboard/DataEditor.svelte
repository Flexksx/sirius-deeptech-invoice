<script>
    import { Textarea, Label, Button } from 'flowbite-svelte';
    import { editor } from "../../routes/store.js";
    import { quintOut } from "svelte/easing";
    import { slide } from "svelte/transition";
    import axios from 'axios';

    export let setPage;

    let loading = false;
    let tempData = JSON.stringify($editor, null, 2);

    function handleInput(event) {
        tempData = event.target.value;
    }

    async function saveChanges() {
        loading = true;

        try {
            const response = await axios.post('http://127.0.0.1:5000/confirm', JSON.parse(tempData), {
                headers: {
                    'Content-Type': 'application/json',
                },
            });

            // Extract the HTML content from the response
            const htmlContent = response.data.html;

            // Create a blob for the HTML content
            const blob = new Blob([htmlContent], { type: 'text/html' });
            const url = URL.createObjectURL(blob);

            // Create a link to download the HTML file
            const link = document.createElement('a');
            link.href = url;
            link.download = 'invoice.html';  // Specify the filename for the downloaded file
            document.body.appendChild(link);
            link.click();  // Trigger the download
            document.body.removeChild(link);  // Remove the link after downloading

            setPage("contracts");
        } catch (e) {
            alert("An error occurred: " + e.message);
        } finally {
            loading = false;
        }
    }


    function cancelChanges() {
        tempData = JSON.stringify($editor, null, 2);
    }
</script>

<div in:slide={{ duration: 100, easing: quintOut, axis: 'x' }} class="flex-1 overflow-y-auto flex flex-col min-h-0 m-5 lg:m-15 lg:p-10 md:p-5 sm:p-5 p-5 md:m-10 sm:m-5 bg-lightBlue rounded-2xl">
    {#if loading === false}
        <div>
            <Label for="json-editor" class="mb-2 text-white text-2xl">Edit JSON</Label>
            <Textarea
                    id="json-editor"
                    placeholder="Enter your JSON here..."
                    rows="30"
                    bind:value={tempData}
                    on:input={handleInput}
                    class="font-mono bg-lightBlue text-white"
            />

            <div class="mt-4 flex gap-2">
                <Button on:click={saveChanges} color="primary">Save</Button>
            </div>
        </div>
    {/if}

    {#if loading === true}
        <div transition:slide class="flex items-center h-32 justify-center">
            <h1 class="text-white text-2xl mr-10">Hold on while we handle the magic...</h1>
            <svg class="animate-spin h-16 w-16 text-primary-700" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
                <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.97 7.97 0 014 12H0c0 2.042.768 3.9 2.031 5.291l2-2z"></path>
            </svg>
        </div>
    {/if}
</div>
