module.exports = {
  darkMode: "class",
  content: ["./*.html", "./navbar.js"],
  theme: {
      extend: {
          colors: {
              "primary": "#0369a1",
              "background-light": "#f8fafc",
              "background-dark": "#0f1115",
              "surface-dark": "#1a1d23",
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
      },
  },
  plugins: [
    require('@tailwindcss/forms'),
    require('@tailwindcss/container-queries'),
  ],
}
