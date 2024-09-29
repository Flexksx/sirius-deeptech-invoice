<script>
    import { Textarea, Label, Button } from 'flowbite-svelte';
    import {editor} from "../../routes/store.js";
    import {quintOut} from "svelte/easing";
    import {slide} from "svelte/transition";

    let tempData = JSON.stringify($editor, null, 2); // Hold a temporary copy for editing

    // Function to handle changes when input is made in the textarea
    function handleInput(event) {
        tempData = event.target.value;
    }

    // Function to handle saving the changes
    function saveChanges() {
        try {
            $editor = JSON.parse(tempData);
            alert("Changes saved!");
        } catch (e) {
            alert("Invalid JSON. Please correct the errors and try again.");
        }
    }

    function cancelChanges() {
        tempData = JSON.stringify($editor, null, 2); // Reset tempData
    }
</script>

<div in:slide={{duration: 100, easing: quintOut, axis: 'x' }} class="flex-1 overflow-y-auto flex flex-col min-h-0 m-5 lg:m-15 lg:p-10 md:p-5 sm:p-5 p-5 md:m-10 sm:m-5 bg-lightBlue rounded-2xl">
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

