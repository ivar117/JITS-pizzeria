"use strict";
function fetch_products() {
    fetch("products.json")
        .then(resp => resp.json())
        .then(products => {
        display_products(products); // Display products on the page
    });
}
function display_products(products) {
    const menu_items_container = document.getElementById("menu-items-container");
    const left_menu_container = menu_items_container.querySelector("#left");
    const right_menu_container = menu_items_container.querySelector("#right");
    let direction = 0;
    for (const product of products) {
        const menu_item = document.createElement("div");
        menu_item.classList.add("menu-item");
        menu_item.classList.add("bubble");
        menu_item.innerHTML = `
        <div class="top">
            <span class="name">${product.name}</span>
            <span class="price">${product.price} kr</span>
        </div>
        <div class="bottom">
            <span class="description">${product.desc}</span>
        </div>
        `;
        if (direction % 2 == 0) {
            left_menu_container.appendChild(menu_item);
        }
        else {
            right_menu_container.appendChild(menu_item);
        }
        direction++;
    }
}
fetch_products();
