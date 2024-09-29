<script>
    import LastRange from '../managing/LastRange.svelte';
    import {
        Button,
        Card,
        Checkbox,
        Dropdown,
        Heading,
        Input,
        Table,
        TableBody,
        TableBodyCell,
        TableBodyRow,
        TableHead,
        TableHeadCell
    } from 'flowbite-svelte';
    import {
        CalendarMonthOutline,
        ChevronDownOutline,
        ChevronRightOutline
    } from 'flowbite-svelte-icons';
    import CreditCard from '../managing/CreditCard.svelte';
    import StatusBadge from '../managing/StatusBadge.svelte';
    import {quintOut} from "svelte/easing";
    import { slide } from 'svelte/transition';

    export let dark = false;

    const headers = [
        'Transaction',
        'Date & Time',
        'Amount',
        'Reference number',
        'Payment method',
        'Status'
    ];
    const data = [
        ['Payment from Bonnie Green', 'Apr 23 ,2021', '$2300', '0047568936', 475, 'completed'],
        ['Payment refund to #00910', 'Apr 23 ,2021', '-$670', '0078568936', 924, 'completed'],
        ['Payment failed from #087651', 'Apr 18 ,2021', '$234', '0088568934', 826, 'cancelled'],
        ['Payment from Lana Byrd', 'Apr 15 ,2021', '$5000', '0018568911', 634, 'inprogress'],
        ['Payment from Jese Leos', 'Apr 15 ,2021', '$2300', '0045568939', 163, 'completed'],
        ['Refund to THEMESBERG LLC', 'Apr 11 ,2021', '-$560', '0031568935', 443, 'inreview'],
        ['Payment from Lana Lysle', 'Apr 6 ,2021', '$1437', '0023568934', 223, 'inreview'],
        ['Payment to Joseph Mcfall', 'Apr 1 ,2021', '$980', '0057568935', 362, 'completed'],
        ['Payment from Alphabet', 'Mar 23 ,2021', '$11,436', '00836143841', 772, 'inprogress'],
        ['Payment from Bonnie Green', 'Mar 23 ,2021', '$560', '0031568935', 123, 'completed'],
        ['Payment from Bonnie Green', 'Apr 23 ,2021', '$2300', '0047568936', 475, 'completed'],
        ['Payment refund to #00910', 'Apr 23 ,2021', '-$670', '0078568936', 924, 'completed'],
        ['Payment failed from #087651', 'Apr 18 ,2021', '$234', '0088568934', 826, 'cancelled'],
        ['Payment from Lana Byrd', 'Apr 15 ,2021', '$5000', '0018568911', 634, 'inprogress'],
        ['Payment from Jese Leos', 'Apr 15 ,2021', '$2300', '0045568939', 163, 'completed'],
        ['Refund to THEMESBERG LLC', 'Apr 11 ,2021', '-$560', '0031568935', 443, 'inreview'],
        ['Payment from Lana Lysle', 'Apr 6 ,2021', '$1437', '0023568934', 223, 'inreview'],
        ['Payment to Joseph Mcfall', 'Apr 1 ,2021', '$980', '0057568935', 362, 'completed'],
        ['Payment from Alphabet', 'Mar 23 ,2021', '$11,436', '00836143841', 772, 'inprogress'],
        ['Payment from Bonnie Green', 'Mar 23 ,2021', '$560', '0031568935', 123, 'completed'],
        ['Payment from Bonnie Green', 'Apr 23 ,2021', '$2300', '0047568936', 475, 'completed'],
        ['Payment refund to #00910', 'Apr 23 ,2021', '-$670', '0078568936', 924, 'completed'],
        ['Payment failed from #087651', 'Apr 18 ,2021', '$234', '0088568934', 826, 'cancelled'],
        ['Payment from Lana Byrd', 'Apr 15 ,2021', '$5000', '0018568911', 634, 'inprogress'],
        ['Payment from Jese Leos', 'Apr 15 ,2021', '$2300', '0045568939', 163, 'completed'],
        ['Refund to THEMESBERG LLC', 'Apr 11 ,2021', '-$560', '0031568935', 443, 'inreview'],
        ['Payment from Lana Lysle', 'Apr 6 ,2021', '$1437', '0023568934', 223, 'inreview'],
        ['Payment to Joseph Mcfall', 'Apr 1 ,2021', '$980', '0057568935', 362, 'completed'],
        ['Payment from Alphabet', 'Mar 23 ,2021', '$11,436', '00836143841', 772, 'inprogress'],
        ['Payment from Bonnie Green', 'Mar 23 ,2021', '$560', '0031568935', 123, 'completed']
    ];
</script>

<div
        in:slide={{ duration: 100, easing: quintOut, axis: 'x' }}
        class="m-10 flex-1 flex flex-col min-h-0 box-border overflow-y-auto rounded-2xl"
>
<Card class="shadow-sm max-w-none bg-lightBlue rounded-2xl border-none border-2">
    <div class="items-center justify-between lg:flex rounded-2xl">
        <div class="mb-4 mt-px lg:mb-0 rounded-2xl">
            <Heading tag="h3" class="-ml-0.25 mb-2 text-6xl font-semibold text-white rounded-2xl font-main">
                Transactions
            </Heading>
            <span class="text-white font-normal rounded-2xl font-main text-2xl">
                    List of latest transactions
                </span>
        </div>
        <div class="items-center justify-between gap-3 space-y-4 sm:flex sm:space-y-0 text-white">
            <div class="flex items-center text-white">
                <Button color="alternative" class="w-fit whitespace-nowrap px-4 py-2 text-white bg-lightBlue border-lightGray hover:bg-darkBlue">
                    Filter by status
                    <ChevronDownOutline size="lg" />
                </Button>
                <Dropdown class="w-44 space-y-3 p-3 text-sm text-white  bg-lightBlue" placement="bottom-start">
                    <li><Checkbox class="accent-primary-600 text-white bg-lightBlue">Completed (56)</Checkbox></li>
                    <li><Checkbox checked class="text-white  bg-lightBlue">Cancelled (56)</Checkbox></li>
                    <li><Checkbox class="accent-primary-600 text-white  bg-lightBlue">In progress (56)</Checkbox></li>
                    <li><Checkbox checked class="text-white  bg-lightBlue">In review (97)</Checkbox></li>
                </Dropdown>
            </div>
            <div class="flex items-center space-x-4 text-white">
                <Input placeholder="From" class="w-full text-white bg-lightBlue border-lightGray">
                    <CalendarMonthOutline slot="left" size="md" />
                </Input>
                <Input placeholder="To" class="w-full text-white bg-lightBlue border-lightGray">
                    <CalendarMonthOutline slot="left" size="md" />
                </Input>
            </div>
        </div>
    </div>
    <div>
        <Table
                hoverable={true}
                noborder
                striped
                color="custom"
                class="mt-6 min-w-full divide-y divide-lightGray dark:divide-gray-600 bg-darkBlue text-white"
        >
        <TableHead class="bg-lightBlue text-white">
            {#each headers as header}
                <TableHeadCell class="whitespace-nowrap p-4 font-normal">{header}</TableHeadCell>
            {/each}
        </TableHead>
        <TableBody>
            {#each data as [name, date, amount, reference, method, status], i}
                <TableBodyRow class={i % 2 === 0 ? 'bg-lightBlue' : 'bg-darkBlue'}>
                    <TableBodyCell class="px-4 font-normal">{name}</TableBodyCell>
                    <TableBodyCell class="px-4 font-normal text-white">
                        {date}
                    </TableBodyCell>
                    <TableBodyCell class="px-4">{amount}</TableBodyCell>
                    <TableBodyCell class="px-4 font-normal text-gray-500 dark:text-gray-400">
                        {reference}
                    </TableBodyCell>
                    <TableBodyCell class="flex items-center gap-2 px-4 font-normal text-gray-500 dark:text-gray-400">
                        <CreditCard number={method} /> <span>••• {method}</span>
                    </TableBodyCell>
                    <TableBodyCell class="px-4 font-normal">
                        <StatusBadge state={status} {dark} />
                    </TableBodyCell>
                </TableBodyRow>
            {/each}
        </TableBody>
        </Table>
    </div>
    <div class="-mb-1 flex items-center justify-between pt-3 sm:pt-6">
        <LastRange />
        <a
                href="#top"
                class="inline-flex items-center rounded-lg p-1 text-xs font-medium uppercase text-primary-700 hover:bg-gray-100 dark:text-primary-500 dark:hover:bg-gray-700 sm:text-sm"
        >
            Transactions report <ChevronRightOutline size="lg" />
        </a>
    </div>
</Card>
</div>


