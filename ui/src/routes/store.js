import { writable } from 'svelte/store';

export const editor = writable([]);
export const searchValue = writable([]);
export const filteredCompanies = writable([]);

export const companiesStore = writable([
    {
        name: 'Microsoft',
        icon: 'https://upload.wikimedia.org/wikipedia/commons/4/44/Microsoft_logo.svg',
        contracts: [
            { id: 1, name: 'Office 365 Cleanup', revenue: '$300,000', createdAt: '2023-01-15' },
            { id: 2, name: 'Azure Cloud Support', revenue: '$450,000', createdAt: '2023-03-01' },
            { id: 3, name: 'Windows Update Support', revenue: '$600,000', createdAt: '2023-05-10' },
            { id: 4, name: 'Cybersecurity Audit', revenue: '$500,000', createdAt: '2023-08-20' }
        ],
        invoices: [
            { pending: 4, sum: 100, currency: "USD" },
            { paid: 19, sum: 1434, currency: "USD" },
            { overdue: 0, sum: 0, currency: "USD" }
        ],
        isOpen: false
    },
    {
        name: 'Apple Inc.',
        icon: 'https://upload.wikimedia.org/wikipedia/commons/f/fa/Apple_logo_black.svg',
        contracts: [
            { id: 1, name: 'iCloud Data Storage', revenue: '$800,000', createdAt: '2023-04-11' },
            { id: 2, name: 'MacOS Bug Fixes', revenue: '$500,000', createdAt: '2023-07-05' }
        ],
        invoices: [
            { pending: 2, sum: 300, currency: "USD" },
            { paid: 10, sum: 1200, currency: "USD" },
            { overdue: 1, sum: 150, currency: "USD" }
        ],
        isOpen: false
    },
    {
        name: 'Google',
        icon: 'https://upload.wikimedia.org/wikipedia/commons/2/2f/Google_2015_logo.svg',
        contracts: [
            { id: 1, name: 'Google Ads Management', revenue: '$900,000', createdAt: '2023-02-25' },
            { id: 2, name: 'YouTube Content Support', revenue: '$1,200,000', createdAt: '2023-06-12' }
        ],
        invoices: [
            { pending: 3, sum: 250, currency: "USD" },
            { paid: 15, sum: 1800, currency: "USD" },
            { overdue: 2, sum: 200, currency: "USD" }
        ],
        isOpen: false
    },
    {
        name: 'Amazon',
        icon: 'https://upload.wikimedia.org/wikipedia/commons/a/a9/Amazon_logo.svg',
        contracts: [
            { id: 1, name: 'AWS Cloud Infrastructure', revenue: '$2,000,000', createdAt: '2023-01-20' },
            { id: 2, name: 'Prime Delivery Optimization', revenue: '$800,000', createdAt: '2023-03-14' }
        ],
        invoices: [
            { pending: 5, sum: 500, currency: "USD" },
            { paid: 20, sum: 2200, currency: "USD" },
            { overdue: 0, sum: 0, currency: "USD" }
        ],
        isOpen: false
    },
    {
        name: 'Facebook',
        icon: 'https://upload.wikimedia.org/wikipedia/commons/5/51/Facebook_f_logo_%282019%29.svg',
        contracts: [
            { id: 1, name: 'Meta Data Archiving', revenue: '$1,500,000', createdAt: '2023-02-10' },
            { id: 2, name: 'Instagram API Maintenance', revenue: '$400,000', createdAt: '2023-05-22' },
            { id: 3, name: 'WhatsApp Server Upgrade', revenue: '$600,000', createdAt: '2023-07-18' }
        ],
        invoices: [
            { pending: 1, sum: 150, currency: "USD" },
            { paid: 18, sum: 1750, currency: "USD" },
            { overdue: 3, sum: 400, currency: "USD" }
        ],
        isOpen: false
    },
    {
        name: 'Tesla',
        icon: 'https://upload.wikimedia.org/wikipedia/commons/b/b7/Tesla_Motors_logo.svg',
        contracts: [
            { id: 1, name: 'Battery Management System', revenue: '$3,500,000', createdAt: '2023-03-05' },
            { id: 2, name: 'Autopilot Software', revenue: '$2,800,000', createdAt: '2023-06-15' }
        ],
        invoices: [
            { pending: 3, sum: 600, currency: "USD" },
            { paid: 12, sum: 2900, currency: "USD" },
            { overdue: 0, sum: 0, currency: "USD" }
        ],
        isOpen: false
    },
    {
        name: 'Netflix',
        icon: 'https://upload.wikimedia.org/wikipedia/commons/6/69/Netflix_logo.svg',
        contracts: [
            { id: 1, name: 'Content Delivery Network', revenue: '$900,000', createdAt: '2023-01-22' },
            { id: 2, name: 'Recommendation Algorithm', revenue: '$1,200,000', createdAt: '2023-04-10' }
        ],
        invoices: [
            { pending: 4, sum: 350, currency: "USD" },
            { paid: 17, sum: 1300, currency: "USD" },
            { overdue: 1, sum: 200, currency: "USD" }
        ],
        isOpen: false
    },
    {
        name: 'Spotify',
        icon: 'https://upload.wikimedia.org/wikipedia/commons/1/19/Spotify_logo_without_text.svg',
        contracts: [
            { id: 1, name: 'Music Data Analytics', revenue: '$400,000', createdAt: '2023-02-08' },
            { id: 2, name: 'Playlist Curation AI', revenue: '$600,000', createdAt: '2023-07-04' }
        ],
        invoices: [
            { pending: 2, sum: 200, currency: "USD" },
            { paid: 10, sum: 800, currency: "USD" },
            { overdue: 1, sum: 100, currency: "USD" }
        ],
        isOpen: false
    },
    {
        name: 'Salesforce',
        icon: 'https://upload.wikimedia.org/wikipedia/commons/a/ae/Salesforce_logo.svg',
        contracts: [
            { id: 1, name: 'CRM Enhancement', revenue: '$700,000', createdAt: '2023-03-20' },
            { id: 2, name: 'Customer Support Integration', revenue: '$550,000', createdAt: '2023-06-02' }
        ],
        invoices: [
            { pending: 0, sum: 0, currency: "USD" },
            { paid: 12, sum: 1500, currency: "USD" },
            { overdue: 3, sum: 400, currency: "USD" }
        ],
        isOpen: false
    },
    {
        name: 'Adobe',
        icon: 'https://upload.wikimedia.org/wikipedia/commons/1/1b/Adobe_icon_2020.svg',
        contracts: [
            { id: 1, name: 'Creative Cloud Optimization', revenue: '$1,100,000', createdAt: '2023-02-12' },
            { id: 2, name: 'Photoshop Cloud Storage', revenue: '$500,000', createdAt: '2023-04-23' }
        ],
        invoices: [
            { pending: 2, sum: 250, currency: "USD" },
            { paid: 15, sum: 2000, currency: "USD" },
            { overdue: 1, sum: 50, currency: "USD" }
        ],
        isOpen: false
    },
    {
        name: 'Uber',
        icon: 'https://upload.wikimedia.org/wikipedia/commons/c/cc/Uber_logo_2018.svg',
        contracts: [
            { id: 1, name: 'Rideshare Algorithm', revenue: '$1,300,000', createdAt: '2023-03-19' },
            { id: 2, name: 'Driver App Optimization', revenue: '$450,000', createdAt: '2023-06-18' }
        ],
        invoices: [
            { pending: 4, sum: 350, currency: "USD" },
            { paid: 10, sum: 1200, currency: "USD" },
            { overdue: 2, sum: 300, currency: "USD" }
        ],
        isOpen: false
    },
    {
        name: 'Zoom',
        icon: 'https://upload.wikimedia.org/wikipedia/commons/7/76/Zoom_Communications_Logo.svg',
        contracts: [
            { id: 1, name: 'Video Conferencing Support', revenue: '$2,100,000', createdAt: '2023-05-06' },
            { id: 2, name: 'Webinar Hosting', revenue: '$700,000', createdAt: '2023-07-20' }
        ],
        invoices: [
            { pending: 1, sum: 150, currency: "USD" },
            { paid: 20, sum: 2000, currency: "USD" },
            { overdue: 0, sum: 0, currency: "USD" }
        ],
        isOpen: false
    },
    {
        name: 'Slack',
        icon: 'https://upload.wikimedia.org/wikipedia/commons/7/76/Slack_Icon.png',
        contracts: [
            { id: 1, name: 'Messaging Infrastructure', revenue: '$1,000,000', createdAt: '2023-01-30' },
            { id: 2, name: 'Notification System', revenue: '$550,000', createdAt: '2023-04-25' }
        ],
        invoices: [
            { pending: 0, sum: 0, currency: "USD" },
            { paid: 18, sum: 1800, currency: "USD" },
            { overdue: 1, sum: 150, currency: "USD" }
        ],
        isOpen: false
    },
    {
        name: 'Airbnb',
        icon: 'https://upload.wikimedia.org/wikipedia/commons/d/da/Airbnb_Logo_Bélo.svg',
        contracts: [
            { id: 1, name: 'Property Management AI', revenue: '$1,600,000', createdAt: '2023-02-18' },
            { id: 2, name: 'Booking Optimization', revenue: '$750,000', createdAt: '2023-06-12' }
        ],
        invoices: [
            { pending: 2, sum: 200, currency: "USD" },
            { paid: 12, sum: 1300, currency: "USD" },
            { overdue: 0, sum: 0, currency: "USD" }
        ],
        isOpen: false
    },
    {
        name: 'Twitter',
        icon: 'https://upload.wikimedia.org/wikipedia/en/6/60/Twitter_Logo_as_of_2021.svg',
        contracts: [
            { id: 1, name: 'Tweet Analytics', revenue: '$900,000', createdAt: '2023-03-21' },
            { id: 2, name: 'Ad Management Platform', revenue: '$1,200,000', createdAt: '2023-08-05' }
        ],
        invoices: [
            { pending: 3, sum: 300, currency: "USD" },
            { paid: 14, sum: 1600, currency: "USD" },
            { overdue: 1, sum: 100, currency: "USD" }
        ],
        isOpen: false
    }
]);

export const companyInvoices = writable([
    {
        id: 1,
        name: 'Microsoft',
        invoices: [
            { status: 'pending', amount: 150, month: 'May 2024', currency: 'USD' },
            { status: 'paid', amount: 300, month: 'June 2024', currency: 'EUR' },
            { status: 'overdue', amount: 100, month: 'July 2024', currency: 'MDL' },
            { status: 'paid', amount: 500, month: 'July 2024', currency: 'USD' },
            { status: 'pending', amount: 250, month: 'May 2024', currency: 'EUR' },
            { status: 'paid', amount: 700, month: 'June 2024', currency: 'MDL' },
            { status: 'overdue', amount: 150, month: 'May 2024', currency: 'USD' },
            { status: 'pending', amount: 600, month: 'July 2024', currency: 'EUR' }
        ]
    },
    {
        id: 2,
        name: 'Apple Inc.',
        invoices: [
            { status: 'pending', amount: 200, month: 'May 2024', currency: 'EUR' },
            { status: 'paid', amount: 400, month: 'June 2024', currency: 'USD' },
            { status: 'overdue', amount: 300, month: 'July 2024', currency: 'MDL' },
            { status: 'paid', amount: 450, month: 'June 2024', currency: 'EUR' },
            { status: 'pending', amount: 500, month: 'May 2024', currency: 'USD' },
            { status: 'paid', amount: 250, month: 'July 2024', currency: 'MDL' },
            { status: 'overdue', amount: 300, month: 'June 2024', currency: 'EUR' },
            { status: 'pending', amount: 600, month: 'May 2024', currency: 'USD' }
        ]
    },
    {
        id: 3,
        name: 'Google',
        invoices: [
            { status: 'pending', amount: 100, month: 'May 2024', currency: 'MDL' },
            { status: 'paid', amount: 700, month: 'June 2024', currency: 'USD' },
            { status: 'overdue', amount: 200, month: 'July 2024', currency: 'EUR' },
            { status: 'paid', amount: 800, month: 'June 2024', currency: 'MDL' },
            { status: 'pending', amount: 400, month: 'May 2024', currency: 'USD' },
            { status: 'paid', amount: 600, month: 'July 2024', currency: 'EUR' },
            { status: 'overdue', amount: 150, month: 'June 2024', currency: 'MDL' },
            { status: 'pending', amount: 350, month: 'May 2024', currency: 'USD' }
        ]
    },
    {
        id: 4,
        name: 'Amazon',
        invoices: [
            { status: 'pending', amount: 300, month: 'May 2024', currency: 'USD' },
            { status: 'paid', amount: 600, month: 'June 2024', currency: 'EUR' },
            { status: 'overdue', amount: 250, month: 'July 2024', currency: 'MDL' },
            { status: 'paid', amount: 500, month: 'June 2024', currency: 'USD' },
            { status: 'pending', amount: 150, month: 'May 2024', currency: 'EUR' },
            { status: 'paid', amount: 750, month: 'July 2024', currency: 'MDL' },
            { status: 'overdue', amount: 350, month: 'June 2024', currency: 'USD' },
            { status: 'pending', amount: 200, month: 'May 2024', currency: 'EUR' }
        ]
    },
    {
        id: 5,
        name: 'Tesla',
        invoices: [
            { status: 'pending', amount: 500, month: 'May 2024', currency: 'EUR' },
            { status: 'paid', amount: 900, month: 'June 2024', currency: 'USD' },
            { status: 'overdue', amount: 350, month: 'July 2024', currency: 'MDL' },
            { status: 'paid', amount: 200, month: 'June 2024', currency: 'EUR' },
            { status: 'pending', amount: 250, month: 'May 2024', currency: 'USD' },
            { status: 'paid', amount: 600, month: 'July 2024', currency: 'MDL' },
            { status: 'overdue', amount: 450, month: 'June 2024', currency: 'USD' },
            { status: 'pending', amount: 300, month: 'May 2024', currency: 'EUR' }
        ]
    },
    {
        id: 6,
        name: 'Facebook',
        invoices: [
            { status: 'pending', amount: 200, month: 'May 2024', currency: 'USD' },
            { status: 'paid', amount: 400, month: 'June 2024', currency: 'EUR' },
            { status: 'overdue', amount: 300, month: 'July 2024', currency: 'MDL' },
            { status: 'paid', amount: 100, month: 'June 2024', currency: 'USD' },
            { status: 'pending', amount: 800, month: 'July 2024', currency: 'EUR' },
            { status: 'paid', amount: 600, month: 'June 2024', currency: 'MDL' },
            { status: 'overdue', amount: 350, month: 'May 2024', currency: 'USD' },
            { status: 'pending', amount: 250, month: 'July 2024', currency: 'EUR' }
        ]
    },
    {
        id: 7,
        name: 'Netflix',
        invoices: [
            { status: 'pending', amount: 300, month: 'May 2024', currency: 'EUR' },
            { status: 'paid', amount: 900, month: 'June 2024', currency: 'USD' },
            { status: 'overdue', amount: 150, month: 'July 2024', currency: 'MDL' },
            { status: 'paid', amount: 400, month: 'June 2024', currency: 'EUR' },
            { status: 'pending', amount: 500, month: 'May 2024', currency: 'USD' },
            { status: 'paid', amount: 600, month: 'July 2024', currency: 'MDL' },
            { status: 'overdue', amount: 200, month: 'June 2024', currency: 'USD' },
            { status: 'pending', amount: 250, month: 'May 2024', currency: 'EUR' }
        ]
    },
    {
        id: 8,
        name: 'Spotify',
        invoices: [
            { status: 'pending', amount: 400, month: 'May 2024', currency: 'MDL' },
            { status: 'paid', amount: 800, month: 'June 2024', currency: 'USD' },
            { status: 'overdue', amount: 200, month: 'July 2024', currency: 'EUR' },
            { status: 'paid', amount: 300, month: 'June 2024', currency: 'MDL' },
            { status: 'pending', amount: 600, month: 'May 2024', currency: 'USD' },
            { status: 'paid', amount: 100, month: 'July 2024', currency: 'EUR' },
            { status: 'overdue', amount: 350, month: 'June 2024', currency: 'MDL' },
            { status: 'pending', amount: 500, month: 'May 2024', currency: 'USD' }
        ]
    },
    {
        id: 9,
        name: 'Adobe',
        invoices: [
            { status: 'pending', amount: 250, month: 'May 2024', currency: 'EUR' },
            { status: 'paid', amount: 300, month: 'June 2024', currency: 'USD' },
            { status: 'overdue', amount: 150, month: 'July 2024', currency: 'MDL' },
            { status: 'paid', amount: 500, month: 'June 2024', currency: 'EUR' },
            { status: 'pending', amount: 450, month: 'May 2024', currency: 'USD' },
            { status: 'paid', amount: 600, month: 'July 2024', currency: 'MDL' },
            { status: 'overdue', amount: 300, month: 'June 2024', currency: 'EUR' },
            { status: 'pending', amount: 200, month: 'May 2024', currency: 'USD' }
        ]
    },
    {
        id: 10,
        name: 'IBM',
        invoices: [
            { status: 'pending', amount: 300, month: 'May 2024', currency: 'USD' },
            { status: 'paid', amount: 700, month: 'June 2024', currency: 'EUR' },
            { status: 'overdue', amount: 400, month: 'July 2024', currency: 'MDL' },
            { status: 'paid', amount: 600, month: 'June 2024', currency: 'USD' },
            { status: 'pending', amount: 150, month: 'May 2024', currency: 'EUR' },
            { status: 'paid', amount: 800, month: 'July 2024', currency: 'MDL' },
            { status: 'overdue', amount: 250, month: 'June 2024', currency: 'USD' },
            { status: 'pending', amount: 350, month: 'May 2024', currency: 'EUR' }
        ]
    }
]);

export const graphOptions = {
    chart: {
        height: '400px',
        maxWidth: '100%',
        type: 'area',
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
    fill: {
        type: 'gradient',
        gradient: {
            opacityFrom: 0.55,
            opacityTo: 0,
            shade: '#1C64F2',
            gradientToColors: ['#1C64F2']
        }
    },
    dataLabels: {
        enabled: false
    },
    stroke: {
        width: 6
    },
    grid: {
        show: false,
        strokeDashArray: 4,
        padding: {
            left: 2,
            right: 2,
            top: 0
        }
    },
    series: [
        {
            name: 'New users',
            data: [6500, 6418, 6456, 6526, 6356, 6456],
            color: '#1A56DB'
        }
    ],
    xaxis: {
        categories: ['01 February', '02 February', '03 February', '04 February', '05 February', '06 February', '07 February'],
        labels: {
            show: false
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
