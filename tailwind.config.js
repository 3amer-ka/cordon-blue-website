module.exports = {
  darkMode: "class",
  content: ["./*.html"],
  theme: {
      extend: {
          colors: {
              "primary": "#0ea5e9",
              "background-light": "#f8fafc",
              "background-dark": "#0f1115",
              "surface-dark": "#1a1d23",
          },
          fontFamily: {
              "display": ["Inter", "sans-serif"]
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
