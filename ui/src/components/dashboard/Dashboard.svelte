<script>

    import {
        A, Button, Card, Chart, Dropdown, DropdownItem,
        Popover,
        Sidebar,
        SidebarDropdownItem,
        SidebarDropdownWrapper,
        SidebarGroup,
        SidebarItem,
        SidebarWrapper
    } from "flowbite-svelte";
    import {
        ArrowRightToBracketOutline,
        CartSolid,
        ChartPieSolid, ChevronDownOutline, ChevronRightOutline, EditOutline, FileLinesSolid,
        GridSolid, InfoCircleSolid,
        MailBoxSolid,
        UserSolid
    } from "flowbite-svelte-icons";
    import {quintOut} from "svelte/easing";
    import { slide } from 'svelte/transition';

    let options = {
        chart: {
            height: '400px',
            maxWidth: '100%',
            type: 'line',
            fontFamily: 'Inter, sans-serif',
            dropShadow: {
                enabled: false
            },
            toolbar: {
                show: false
            }
        },
        tooltip: {
            enabled: true,
            x: {
                show: false
            }
        },
        dataLabels: {
            enabled: false
        },
        stroke: {
            width: 6,
            curve: 'smooth'
        },
        grid: {
            show: true,
            strokeDashArray: 4,
            padding: {
                left: 2,
                right: 2,
                top: -26
            }
        },
        series: [
            {
                name: 'Clicks',
                data: [6500, 6418, 6456, 6526, 6356, 6456],
                color: '#1A56DB'
            },
            {
                name: 'CPC',
                data: [6456, 6356, 6526, 6332, 6418, 6500],
                color: '#7E3AF2'
            }
        ],
        legend: {
            show: false
        },
        xaxis: {
            categories: ['01 Feb', '02 Feb', '03 Feb', '04 Feb', '05 Feb', '06 Feb', '07 Feb'],
            labels: {
                show: true,
                style: {
                    fontFamily: 'Inter, sans-serif',
                    cssClass: 'text-xs font-normal fill-gray-500 dark:fill-gray-400'
                }
            },
            axisBorder: {
                show: false
            },
            axisTicks: {
                show: false
            }
        },
        yaxis: {
            show: false
        }
    };

    let spanClass = 'flex-1 ms-3 whitespace-nowrap';
</script>

<div in:slide={{ duration: 100, easing: quintOut, axis: 'x' }} class="flex flex-1 bg-lightBlue">
    <Sidebar class="bg-darkBlue h-full text-white font-semibold">
        <SidebarWrapper class="bg-darkBlue text-white">
            <SidebarGroup class="bg-darkBlue text-white">
                <SidebarItem label="Dashboard" class="hover:bg-lightBlue transition duration-150  text-white font-semibold">
                    <svelte:fragment slot="icon">
                        <ChartPieSolid class="w-6 h-6  text-white font-semibold transition duration-75 " />
                    </svelte:fragment>
                </SidebarItem>
                <SidebarItem label="Settings" {spanClass} class="hover:bg-lightBlue transition duration-150  text-white font-semibold">
                    <svelte:fragment slot="icon">
                        <GridSolid class="w-6 h-6 text-white font-semibold transition duration-75" />
                    </svelte:fragment>
                </SidebarItem>
                <SidebarItem label="Inbox" {spanClass} class="hover:bg-lightBlue transition duration-150 text-white font-semibold">
                    <svelte:fragment slot="icon">
                        <MailBoxSolid class="w-6 h-6 transition duration-75 text-white font-semibold" />
                    </svelte:fragment>
                    <svelte:fragment slot="subtext">
                        <span class="inline-flex justify-center items-center p-3 ms-3 w-3 h-3 text-sm text-white font-semibold bg-primary-700 rounded-full"> 3 </span>
                    </svelte:fragment>
                </SidebarItem>
                <SidebarItem label="Users" class="hover:bg-lightBlue transition duration-150 text-white font-semibold">
                    <svelte:fragment slot="icon">
                        <UserSolid class="w-6 h-6  text-white font-semibold transition duration-75" />
                    </svelte:fragment>
                </SidebarItem>
                <SidebarItem label="Sign In" class="hover:bg-lightBlue transition duration-150 text-white font-semibold">
                    <svelte:fragment slot="icon">
                        <ArrowRightToBracketOutline class="w-6 h-6  text-white font-semibold transition duration-75" />
                    </svelte:fragment>
                </SidebarItem>
                <SidebarItem label="Sign Up" class="hover:bg-lightBlue transition duration-150 text-white font-semibold">
                    <svelte:fragment slot="icon">
                        <EditOutline class="w-6 h-6  text-white font-semibold transition duration-75" />
                    </svelte:fragment>
                </SidebarItem>
            </SidebarGroup>
        </SidebarWrapper>
    </Sidebar>

    <div>
        <Card class="bg-lightBlue m-10">
            <div class="flex justify-between mb-5">
                <div class="grid gap-4 grid-cols-2">
                    <div>
                        <h5 class="inline-flex items-center text-gray-500 dark:text-gray-400 leading-none font-normal mb-2">
                            Clicks
                            <InfoCircleSolid id="b1" class="w-3 h-3 text-gray-400 hover:text-gray-900 dark:hover:text-white cursor-pointer ms-1" />
                            <Popover triggeredBy="#b1" class="text-sm text-gray-500 bg-white border border-gray-200 rounded-lg shadow-sm w-72 dark:bg-gray-800 dark:border-gray-600 dark:text-gray-400 z-10">
                                <div class="p-3 space-y-2">
                                    <h3 class="font-semibold text-gray-900 dark:text-white">Clicks growth - Incremental</h3>
                                    <p>Report helps navigate cumulative growth of community activities. Ideally, the chart should have a growing trend, as stagnating chart signifies a significant decrease of community activity.</p>
                                    <h3 class="font-semibold text-gray-900 dark:text-white">Calculation</h3>
                                    <p>For each date bucket, the all-time volume of activities is calculated. This means that activities in period n contain all activities up to period n, plus the activities generated by your community in period.</p>
                                    <A href="/"
                                    >Read more
                                        <ChevronRightOutline class="w-2 h-2 ms-1.5" /></A>
                                </div>
                            </Popover>
                        </h5>
                        <p class="text-gray-900 dark:text-white text-2xl leading-none font-bold">42,3k</p>
                    </div>
                    <div>
                        <h5 class="inline-flex items-center text-gray-500 dark:text-gray-400 leading-none font-normal mb-2">
                            CPC
                            <InfoCircleSolid id="b2" class="w-3 h-3 text-gray-400 hover:text-gray-900 dark:hover:text-white cursor-pointer ms-1" />
                            <Popover triggeredBy="#b2" class="text-sm text-gray-500 bg-white border border-gray-200 rounded-lg shadow-sm w-72 dark:bg-gray-800 dark:border-gray-600 dark:text-gray-400 z-10">
                                <div class="p-3 space-y-2">
                                    <h3 class="font-semibold text-gray-900 dark:text-white">CPC growth - Incremental</h3>
                                    <p>Report helps navigate cumulative growth of community activities. Ideally, the chart should have a growing trend, as stagnating chart signifies a significant decrease of community activity.</p>
                                    <h3 class="font-semibold text-gray-900 dark:text-white">Calculation</h3>
                                    <p>For each date bucket, the all-time volume of activities is calculated. This means that activities in period n contain all activities up to period n, plus the activities generated by your community in period.</p>
                                    <A href="/">Read more <ChevronRightOutline class="w-2 h-2 ms-1.5" /></A>
                                </div>
                            </Popover>
                        </h5>
                        <p class="text-gray-900 dark:text-white text-2xl leading-none font-bold">$5.40</p>
                    </div>
                </div>
                <div>
                    <Button color="light" class="px-3 py-2">Last week<ChevronDownOutline class="w-2.5 h-2.5 ms-1.5" /></Button>
                    <Dropdown class="w-40">
                        <DropdownItem>Yesterday</DropdownItem>
                        <DropdownItem>Today</DropdownItem>
                        <DropdownItem>Last 7 days</DropdownItem>
                        <DropdownItem>Last 30 days</DropdownItem>
                        <DropdownItem>Last 90 days</DropdownItem>
                    </Dropdown>
                </div>
            </div>
            <Chart {options} />
            <div class="grid grid-cols-1 items-center border-gray-200 border-t dark:border-gray-700 justify-between mt-2.5">
                <div class="pt-5">
                    <Button href="/" class="px-4 py-2.5 text-sm font-medium text-white inline-flex items-center bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 rounded-lg text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800">
                        <FileLinesSolid class="w-3.5 h-3.5 text-white me-2" />
                        View full report
                    </Button>
                </div>
            </div>
        </Card>
    </div>

</div>
