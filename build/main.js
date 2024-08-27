"use strict";
function fetch_products() {
    fetch("products.json")
        .then(resp => resp.json())
        .then(products => {
        display_products(products); // Display products on the page
    });
}
function display_products(products) {
    const left_menu_container = document.getElementById("left-menu-container");
    const right_menu_container = document.getElementById("right-menu-container");
    console.log(products); // Logs products in console
}
fetch_products();
