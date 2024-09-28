import { writable } from 'svelte/store';

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
        isOpen: false
    },
    {
        name: 'Apple Inc.',
        icon: 'https://upload.wikimedia.org/wikipedia/commons/f/fa/Apple_logo_black.svg',
        contracts: [
            { id: 1, name: 'iCloud Data Storage', revenue: '$800,000', createdAt: '2023-04-11' },
            { id: 2, name: 'MacOS Bug Fixes', revenue: '$500,000', createdAt: '2023-07-05' }
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
        isOpen: false
    },
    {
        name: 'Amazon',
        icon: 'https://upload.wikimedia.org/wikipedia/commons/a/a9/Amazon_logo.svg',
        contracts: [
            { id: 1, name: 'AWS Cloud Infrastructure', revenue: '$2,000,000', createdAt: '2023-01-20' },
            { id: 2, name: 'Prime Delivery Optimization', revenue: '$800,000', createdAt: '2023-03-14' }
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
        isOpen: false
    },
    {
        name: 'Tesla',
        icon: 'https://upload.wikimedia.org/wikipedia/commons/b/b7/Tesla_Motors_logo.svg',
        contracts: [
            { id: 1, name: 'Battery Management System', revenue: '$3,500,000', createdAt: '2023-03-05' },
            { id: 2, name: 'Autopilot Software', revenue: '$2,800,000', createdAt: '2023-06-15' }
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
        isOpen: false
    },
    {
        name: 'Spotify',
        icon: 'https://upload.wikimedia.org/wikipedia/commons/1/19/Spotify_logo_without_text.svg',
        contracts: [
            { id: 1, name: 'Music Data Analytics', revenue: '$400,000', createdAt: '2023-02-08' },
            { id: 2, name: 'Playlist Curation AI', revenue: '$600,000', createdAt: '2023-07-04' }
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
        isOpen: false
    },
    {
        name: 'Adobe',
        icon: 'https://upload.wikimedia.org/wikipedia/commons/1/1b/Adobe_icon_2020.svg',
        contracts: [
            { id: 1, name: 'Creative Cloud Optimization', revenue: '$1,100,000', createdAt: '2023-02-12' },
            { id: 2, name: 'Photoshop Cloud Storage', revenue: '$500,000', createdAt: '2023-04-23' }
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
        isOpen: false
    },
    {
        name: 'Zoom',
        icon: 'https://upload.wikimedia.org/wikipedia/commons/7/76/Zoom_Communications_Logo.svg',
        contracts: [
            { id: 1, name: 'Video Conferencing Support', revenue: '$2,100,000', createdAt: '2023-05-06' },
            { id: 2, name: 'Webinar Hosting', revenue: '$700,000', createdAt: '2023-07-20' }
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
        isOpen: false
    },
    {
        name: 'Airbnb',
        icon: 'https://upload.wikimedia.org/wikipedia/commons/d/da/Airbnb_Logo_Bélo.svg',
        contracts: [
            { id: 1, name: 'Property Management AI', revenue: '$1,600,000', createdAt: '2023-02-18' },
            { id: 2, name: 'Booking Optimization', revenue: '$750,000', createdAt: '2023-06-12' }
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
        isOpen: false
    }
]);