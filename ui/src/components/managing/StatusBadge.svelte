<script >
    import { Badge } from 'flowbite-svelte';

    export let state;
    export let dark;

    const states = {
        completed: 'Completed',
        cancelled: 'Canceled',
        inreview: 'In review',
        inprogress: 'In progress'
    };

    const colors = {
        completed: 'green',
        cancelled: 'red',
        inreview: 'yellow',
        inprogress: 'purple'
    };
</script>

<Badge color={colors[state] ?? 'dark'} border={dark}>{states[state] ?? 'Unknown'}</Badge>