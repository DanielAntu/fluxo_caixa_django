const currentUrl = window.location.pathname;
const navlinks = document.querySelectorAll("nav a");
const value_input = document.querySelector(".value_rs");
const nature = document.querySelector("#id_nature");
const type_cash = document.querySelector("#id_type_cash");

const formatRealInput = (text) => {
    clearValue_ = text.replace(/[^0-9,]/g, "");

    if (clearValue_.split(",").length > 2) {
        clearValue_ = clearValue_.slice(0, -1);
        return clearValue_;
    }

    if (clearValue_[0] === ",") {
        clearValue_ = clearValue_.replace(",", "");
        return clearValue_;
    }

    const parts = clearValue_.split(",");

    if (parts.length == 2 && parts[1].length > 2) {
        clearValue_ = parts[0] + "," + parts[1].slice(0, 2);
        return clearValue_;
    }

    return clearValue_;
};

function activeLink(currentUrl, navlinks) {
    navlinks.forEach((link) => {
        if (link.getAttribute("href") === currentUrl) {
            link.classList.add("active");
        }
    });
}

if (currentUrl === "/") {
    value_input.addEventListener("input", (e) => {
        updated_value = formatRealInput(e.target.value);
        e.target.value = updated_value;
        e.stopPropagation();
    });

    nature.addEventListener("change", () => {
        if (nature.value === "output") {
            type_cash.setAttribute("disabled", "");
        } else {
            type_cash.removeAttribute("disabled");
        }
    });
}

activeLink(currentUrl, navlinks);
