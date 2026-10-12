document.addEventListener('DOMContentLoaded', function() {
  particlesJS('particles-js', {
    "particles": {
      "number": {
        "value": 80,
        "density": {
          "enable": true,
          "value_area": 800
        }
      },
      "color": {
        "value": "#000000"
      },
      "shape": {
        "type": "circle"
      },
      "opacity": {
        "value": 0.6,
        "random": false
      },
      "size": {
        "value": 3,
        "random": true
      },
      "line_linked": {
        "enable": true,
        "distance": 150,
        "color": "#000000",
        "opacity": 0.4,
        "width": 1
      },
      "move": {
        "enable": true,
        "speed": 2,
        "direction": "none",
        "random": false,
        "straight": false,
        "out_mode": "out",
        "bounce": false
      }
    },
    "interactivity": {
      "detect_on": "canvas",
      "events": {
        "onhover": {
          "enable": true,
          "mode": "grab"
        },
        "onclick": {
          "enable": true,
          "mode": "push"
        },
        "resize": true
      },
      "modes": {
        "grab": {
          "distance": 140,
          "line_linked": {
            "opacity": 1
          }
        },
        "push": {
          "particles_nb": 4
        }
      }
    },
    "retina_detect": true
  });

  // On the homepage research section, foreground content can block direct canvas
  // mouse events. Mirror pointer coordinates into particles.js so hover effects
  // remain interactive across the full section area.
  var particlesEl = document.getElementById('particles-js');
  var particlesSection = particlesEl && particlesEl.closest('.research-directions-section--with-particles');

  if (particlesEl && particlesSection && window.pJSDom && window.pJSDom[0] && window.pJSDom[0].pJS) {
    var pJS = window.pJSDom[0].pJS;

    particlesSection.addEventListener('mousemove', function(event) {
      var canvas = pJS.canvas && pJS.canvas.el;
      if (!canvas) {
        return;
      }

      var rect = canvas.getBoundingClientRect();
      var pxratio = (pJS.canvas && pJS.canvas.pxratio) ? pJS.canvas.pxratio : 1;
      pJS.interactivity.mouse.pos_x = (event.clientX - rect.left) * pxratio;
      pJS.interactivity.mouse.pos_y = (event.clientY - rect.top) * pxratio;
      pJS.interactivity.status = 'mousemove';
    });

    particlesSection.addEventListener('mouseleave', function() {
      pJS.interactivity.mouse.pos_x = null;
      pJS.interactivity.mouse.pos_y = null;
      pJS.interactivity.status = 'mouseleave';
    });
  }
});