document.addEventListener("DOMContentLoaded", () => {
  const token = localStorage.getItem("access_token");

  if (!token) {
    console.error("❌ No access token found in localStorage");
    return;
  }

  fetch("http://127.0.0.1:8000/api/delivery/me/", {
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
      console.log("✅ Delivery person profile fetched:", data);
      
      // Update all fields in UI
      document.querySelectorAll(".username").forEach(el => {
        el.textContent = data.user.username;
      });
      document.querySelectorAll(".phone").forEach(el => {
        el.textContent = data.phone;
      });
      document.querySelectorAll(".license-number").forEach(el => {
        el.textContent = data.license_number;
      });
      document.querySelectorAll(".vehicle-type").forEach(el => {
        el.textContent = data.vehicle_type;
      });
      document.querySelectorAll(".vehicle-number").forEach(el => {
        el.textContent = data.vehicle_number;
      });
      document.querySelectorAll(".driver-id").forEach(el => {
        el.textContent = data.id;
      });
      document.querySelectorAll(".license-photo").forEach(el => {
        el.src = data.license_photo;
      });
      
      
      
      
      
      document.querySelectorAll(".usernamevalue").forEach(el => {
        el.value = data.user.username;
      });
      document.querySelectorAll(".phonevalue").forEach(el => {
        el.value = data.phone;
      });
      document.querySelectorAll(".vehicle-type-value").forEach(el => {
        el.value = data.vehicle_type;
      });
      document.querySelectorAll(".vehicle-number-value").forEach(el => {
        el.value = data.vehicle_number;
      });
      document.querySelectorAll(".driver-id-value").forEach(el => {
        el.value = data.id;
      });


    })
    .catch(error => {
      console.error("❌ Error fetching delivery person data:", error);
    });
});
