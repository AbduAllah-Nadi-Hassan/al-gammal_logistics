document.addEventListener("DOMContentLoaded", function() {
    const currentLocation = location.href;
    const menuItems = document.querySelectorAll('.nav-item a');

    menuItems.forEach(item => {
        if (item.href === currentLocation) {
            // Remove active class from all menu items
            menuItems.forEach(link => link.classList.remove('active'));
            // Add active class to the current menu item
            item.classList.add('active');
        }
    });
});

document.addEventListener("DOMContentLoaded", function() {
    const menuItems = document.querySelectorAll('.nav-item a');

    menuItems.forEach(item => {
        item.addEventListener('click', function(event) {
            // Prevent default action (which is jumping directly to the section)
            // event.preventDefault();

            // Remove active class from all menu items
            menuItems.forEach(link => link.classList.remove('active'));

            // Add active class to the clicked menu item
            item.classList.add('active');

            // Scroll to the section smoothly
            const targetId = item.getAttribute('href').substring(1);
            const targetSection = document.getElementById(targetId);
            window.scrollTo({
                top: targetSection.offsetTop,
                behavior: 'smooth'
            });
        });
    });
});


// Show the arrow when the user scrolls down 100px from the top
window.onscroll = function() {
    var backToTopButton = document.getElementById("back-to-top");
    if (document.body.scrollTop > 100 || document.documentElement.scrollTop > 100) {
        backToTopButton.style.display = "block";
    } else {
        backToTopButton.style.display = "none";
    }
};

// spinner
// window.addEventListener("load", function() {
//     const loadingScreen = document.getElementById('loading-screen');
//     loadingScreen.style.display = 'none';
// });



// article page 

document.querySelectorAll('.page-link').forEach(link => {
    link.addEventListener('click', function(e) {
        e.preventDefault(); // Prevent the default link behavior

        // Remove 'active' class from all links
        document.querySelectorAll('.page-link').forEach(item => {
            item.classList.remove('active');
        });

        // Add 'active' class to the clicked link
        this.classList.add('active');
    });
});

// owl Carsoule


    // Main News carousel
    $(".main-carousel").owlCarousel({
        autoplay: true,
        smartSpeed: 1500,
        items: 1,
        dots: true,
        loop: true,
        center: true,
    });


    // Tranding carousel
    $(".tranding-carousel").owlCarousel({
        autoplay: true,
        smartSpeed: 2000,
        items: 1,
        dots: false,
        loop: true,
        nav : true,
        navText : [
            '<i class="fa fa-angle-left"></i>',
            '<i class="fa fa-angle-right"></i>'
        ]
    });
