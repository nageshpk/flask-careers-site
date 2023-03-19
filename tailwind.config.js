/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./templates/**/*.html",
    "./static/src/**/*.js",
    "./node_modules/flowbite/**/*.js"
  ],
  theme: {
    extend: {
      colors: {
        jovian: '#1f2937',
      },
    },
  },
  plugins: [
    require("flowbite/plugin")
  ],
}