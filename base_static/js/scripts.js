var currentUrl = window.location.pathname;
var navlinks = document.querySelectorAll("nav a");

function activeLink(currentUrl, navlinks) {
    navlinks.forEach((link) => {
        if (link.getAttribute("href") === currentUrl) {
            link.classList.add("active");
        }
    });
}

activeLink(currentUrl, navlinks);
