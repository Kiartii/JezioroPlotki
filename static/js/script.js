document.addEventListener("DOMContentLoaded", function() {
        var button = document.querySelector('.navbar-toggler');
        var menu = document.querySelector('#navbarResponsive');

        button.addEventListener('click', function() {
            menu.classList.toggle('show');
        });
    });