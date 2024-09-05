/** @type {import('tailwindcss').Config} */
module.exports = {
  darkMode: "class",
  content: [
    './templates/**/*.{html,js}',
    './apps/blog/templates/**/*.html',
  ],
  theme: {
    extend: {
      colors: {
        'abdo-color': '#252f3c',
        /*'abdo-color-light': '#4b5563',*/
        'abdo-color-light': '#93b9c7',
        'abdo-color-dark': '#010101',
        'about-text': '#9ecffa',
        'dark-mode-color': '#282d34',
        'header-color': '#fefddf',
      },
    },
  },
  plugins: [],
}

// ./tailwindcss -i ./apps/blog/static/css/input.css -o ./apps/blog/static/css/output.css --watch

