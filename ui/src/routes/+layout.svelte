<script>
    import "../app.css";
</script>

<style>
    *,
    *::before,
    *::after {
        box-sizing: border-box;
    }

    ::-webkit-scrollbar {
        width: 12px;
        height: 12px;
    }

    ::-webkit-scrollbar-track {
        background: #EB4F27;
        border-radius: 10px;
    }

    ::-webkit-scrollbar-thumb {
        background-color: #111828;
        border-radius: 10px;
        border: 3px solid #EB4F27;
    }

    ::-webkit-scrollbar-thumb:hover {
        background-color: #0F1A24;
    }

    * {
        scrollbar-width: thin;
        scrollbar-color: #111828 #EB4F27;
    }

</style>

<slot />