  document.addEventListener("DOMContentLoaded", () => {
    const logoutBtn = document.getElementById("logoutBtn");
    const logoutModal = document.getElementById("logoutModal");
    const cancelLogout = document.getElementById("cancelLogout");
    const confirmLogout = document.getElementById("confirmLogout");

    function showModal() {
      logoutModal.classList.remove("hidden");
      setTimeout(() => logoutModal.classList.remove("opacity-0"), 10);
    }

    function hideModal() {
      logoutModal.classList.add("opacity-0");
      setTimeout(() => logoutModal.classList.add("hidden"), 300);
    }

    logoutBtn.addEventListener("click", showModal);
    cancelLogout.addEventListener("click", hideModal);

    confirmLogout.addEventListener("click", () => {
      // Replace with your logout URL or logic
      window.location.href = "/logout/";
    });

    // Optional: click outside modal to close
    logoutModal.addEventListener("click", (e) => {
      if (e.target === logoutModal) hideModal();
    });
  });

