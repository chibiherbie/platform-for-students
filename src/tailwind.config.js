/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./student/templates/student/*.{html,js}"],
  theme: {
    colors: {
      "gray-btn": "#2f2f38"
    },
    fontFamily: {
      'display': ['Oswald'],
      'body': ['"Oswald"'],
    },
    extend: {},
  },
  plugins: [],
}

