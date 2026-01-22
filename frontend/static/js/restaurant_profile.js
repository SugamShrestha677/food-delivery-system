document.addEventListener("DOMContentLoaded", () => {
  const token = localStorage.getItem("access_token");

  if (!token) {
    console.error("❌ No access token found in localStorage");
    return;
  }

  fetch("http://127.0.0.1:8000/api/restaurant/me/", {
    method: "GET",
    headers: {
      "Authorization": `Bearer ${token}`,
      "Content-Type": "application/json",
    },
  })
    .then(response => {
      if (!response.ok) {
        throw new Error("❌ Request failed with status " + response.status);
      }
      return response.json();
    })
    .then(data => {
      console.log("✅ Restaurant profile fetched:", data);
      // Example: show name in UI
      document.querySelectorAll(".restaurant_name").forEach(el => {
            el.textContent = data.restaurant_name;
        });
        document.querySelectorAll(".email").forEach(el => {
          el.textContent = data.email;
        });
        document.querySelectorAll(".owner_name").forEach(el => {
          el.textContent = data.owner_name;
        });
        document.querySelectorAll(".contact").forEach(el => {
          el.textContent = data.contact;
        });
        document.querySelectorAll(".profile").forEach(el => {
          el.src = data.logo;
        });








        // for form values
        document.querySelectorAll(".restaurant_name").forEach(el => {
              el.value = data.restaurant_name;
          });
        document.querySelectorAll(".delivery_fees").forEach(el => {
              el.value = data.delivery_fees;
          });
        document.querySelectorAll(".owner_name").forEach(el => {
              el.value = data.owner_name;
          });
        document.querySelectorAll(".contact").forEach(el => {
              el.value = data.contact;
          });
        document.querySelectorAll(".address").forEach(el => {
              el.value = data.address;
          });
      })
    .catch(error => {
      console.error("❌ Error fetching profile:", error);
    });
});
