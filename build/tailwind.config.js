/** @type {import('tailwindcss').Config} */
module.exports = {
    darkMode: "class",
    content: ["./*.html", "./navbar.js"],
    theme: {
        extend: {
            colors: {
                "primary": "#0ea5e1",
                "primary-light": "#38bdf8",
                "primary-dark": "#0284c7",
                "background-light": "#f8fafc",
                "background-dark": "#0f1115",
                "surface-dark": "#1a1d23",
                "border-dark": "#2d323b",
                "accent-dark": "#1f2937",
            },
            fontFamily: {
                "display": ["Inter", "ui-sans-serif", "system-ui", "sans-serif", "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji"]
            },
            borderRadius: {
                "DEFAULT": "0.25rem",
                "lg": "0.5rem",
                "xl": "0.75rem",
                "2xl": "1rem",
                "3xl": "1.5rem",
                "full": "9999px"
            },
            animation: {
                'fade-in': 'fadeIn 0.6s ease-out',
                'slide-up': 'slideUp 0.6s ease-out',
            },
            keyframes: {
                fadeIn: {
                    '0%': { opacity: '0' },
                    '100%': { opacity: '1' },
                },
                slideUp: {
                    '0%': { opacity: '0', transform: 'translateY(20px)' },
                    '100%': { opacity: '1', transform: 'translateY(0)' },
                },
            },
        },
    },
    plugins: [
        require('@tailwindcss/forms'),
        require('@tailwindcss/container-queries'),
    ],
}
