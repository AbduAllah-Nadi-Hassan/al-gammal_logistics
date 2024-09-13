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


// Language Switcher

// Function to get the current language
function getCurrentLanguage() {
    return document.documentElement.lang || 'en'; // Defaults to 'en' if lang attribute is not set
}

// Function to set the button label
function setLanguageSwitcher() {
    const currentLang = getCurrentLanguage();
    const switcherButton = document.getElementById('languageSwitcher');
    
    if (currentLang === 'en') {
        switcherButton.textContent = 'العربية'; // Show Arabic if current language is English
    } else {
        switcherButton.textContent = 'English'; // Show English if current language is not English
    }
}

// Event listener to switch the language
document.getElementById('languageSwitcher').addEventListener('click', function() {
    const currentLang = getCurrentLanguage();
    const newLang = currentLang === 'en' ? 'ar' : 'en'; // Toggle between 'en' and 'ar'

    // Redirect to change the language (this assumes you have a URL setup to change language)
    window.location.href = `/set_language/?language=${newLang}`;
});

// Initialize the language switcher button
setLanguageSwitcher();


////////////////////////////////////
function checkVisibility() {
    const switcher = document.querySelector('.language-switch');
    const navbar = document.querySelector('nav');
    const footer = document.querySelector('footer');

    const switcherRect = switcher.getBoundingClientRect();
    const navbarRect = navbar.getBoundingClientRect();
    const footerRect = footer.getBoundingClientRect();

    // Check if switcher overlaps with navbar or footer
    if (
        (switcherRect.top < navbarRect.bottom && switcherRect.bottom > navbarRect.top) ||
        (switcherRect.top < footerRect.bottom && switcherRect.bottom > footerRect.top)
    ) {
        switcher.classList.add('hidden');
    } else {
        switcher.classList.remove('hidden');
    }
}

window.addEventListener('scroll', checkVisibility);
window.addEventListener('resize', checkVisibility);

// Initial check
checkVisibility();


