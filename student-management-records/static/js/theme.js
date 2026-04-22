document.addEventListener('DOMContentLoaded', () => {
    const body = document.body;
    const toggleButtons = document.querySelectorAll('[data-theme-toggle]');
    const savedTheme = localStorage.getItem('theme');
    const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
    const initialTheme = savedTheme || (prefersDark ? 'dark' : 'light');

    const applyTheme = (theme) => {
        const isDarkMode = theme === 'dark';
        body.classList.toggle('dark-mode', isDarkMode);

        toggleButtons.forEach((button) => {
            button.textContent = isDarkMode ? 'Day Mode' : 'Dark Mode';
            button.setAttribute('aria-label', isDarkMode ? 'Switch to day mode' : 'Switch to dark mode');
        });
    };

    applyTheme(initialTheme);

    toggleButtons.forEach((button) => {
        button.addEventListener('click', () => {
            const nextTheme = body.classList.contains('dark-mode') ? 'light' : 'dark';
            localStorage.setItem('theme', nextTheme);
            applyTheme(nextTheme);
        });
    });
});
