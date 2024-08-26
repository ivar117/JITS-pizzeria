"use strict";
function fetch_products() {
    fetch("products.json")
        .then(resp => resp.json())
        .then(products => {
        display_products(products);
    });
}
function display_products(products) {
    const left_menu_container = document.getElementById("left-menu-container");
    const right_menu_container = document.getElementById("right-menu-container");
    console.log(products);
}
fetch_products();
