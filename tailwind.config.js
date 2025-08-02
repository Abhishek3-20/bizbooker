// tailwind.config.js
module.exports = {
    content: [
      "./templates/**/*.html",
      "./**/templates/**/*.html",
      "./static/src/**/*.{js,jsx}",
      "./**/*.py"
    ],
    theme: {
        extend: {
          colors: {
            brandbg: '#bbbdbd', // Optional named color
          },
        },
      },
      plugins: [require('daisyui')],
      daisyui: {
        themes: [{
          bizbooker: {
            "primary": "#4CAF50",
            // ... (other theme colors)
            "base-100": "#FFFFFF", // ← Must be white
          }
        }],
        base: true,    // ← Required for components
        styled: true   // ← Required for buttons
      }
    }