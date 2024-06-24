document.getElementById('menu-toggle').addEventListener('click', function(event) {
    event.stopPropagation();  // Evitar que el clic se propague al documento
    var menu = document.getElementById('mobile-menu');
    menu.classList.toggle('hidden');
});

document.addEventListener('click', function(event) {
    var menu = document.getElementById('mobile-menu');
    var toggleButton = document.getElementById('menu-toggle');
    
    // Si el clic no está dentro del menú ni del botón de toggle, oculta el menú
    if (!menu.contains(event.target) && !toggleButton.contains(event.target)) {
        menu.classList.add('hidden');
    }
});

window.addEventListener('scroll', function() {
    var header = document.getElementById('header');
    if (window.scrollY > 50) {
        header.classList.add('bg-purple-300');
    } else {
        header.classList.remove('bg-purple-300');
    }
});