document.addEventListener("DOMContentLoaded", () => {
  const token = localStorage.getItem("access_token");

  if (!token) {
    console.error("❌ No access token found in localStorage");
    return;
  }

  fetch("http://127.0.0.1:8000/api/restaurant/menu-items/", {
    method: "GET",
    headers: {
      "Authorization": `Bearer ${token}`,
      "Content-Type": "application/json",
    },
  })
    .then(response => {
      if (!response.ok) {
        throw new Error("❌ Failed to fetch menu items. Status: " + response.status);
      }
      return response.json();
    })
    .then(data => {
      console.log("✅ Menu items fetched:", data);

      const container = document.getElementById("menuItemsContainer");
      container.innerHTML = "";

      data.forEach(item => {
        const itemCard = document.createElement("div");
        itemCard.className = "bg-white rounded-xl shadow-md p-4";

        itemCard.innerHTML = `
          <img src="${item.photo}" alt="${item.items}" class="w-full h-40 object-cover rounded mb-4" />
          <div class="flex justify-between">

          <h3 class="text-xl font-bold text-brand-dark">${item.items}</h3>
          
          <button class="text-brand-gray hover:text-red-500 transition-colors">
          <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"></path>
          </svg>
          </button>
          </div>
          
          <p class="text-sm text-brand-gray mt-1">${item.description}</p>
          <p class="text-sm text-brand-gray mt-1">🏪 Restaurant: ${item.restaurant.restaurant_name}</p>
          <p class="text-sm text-brand-gray mt-1">⏱ Estimated Time: ${item.estimated_time}</p>
          <p class="text-sm text-brand-gray mt-1">💵 Price: Rs. ${item.price}</p>
          <p class="text-sm mt-1">✅ Available: <strong>${item.is_available ? "Yes" : "No"}</strong></p><br>
          <button 
  class="add-to-cart-btn bg-brand-orange hover:bg-brand-orange-dark text-white px-4 py-2 rounded-lg font-medium transition-colors"
  data-id="${item.id}" 
  data-name="${item.items}" 
  data-price="${item.price}" 
  data-image="${item.photo}">
  Add to Cart
</button>

        `;

        container.appendChild(itemCard);
      });

    })
    .catch(error => {
      console.error("❌ Error fetching menu items:", error);
    });
});


