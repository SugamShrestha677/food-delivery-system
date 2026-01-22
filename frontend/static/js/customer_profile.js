document.addEventListener('DOMContentLoaded', () => {
  const tabButtons = document.querySelectorAll('.tab-button');
  const tabContents = document.querySelectorAll('.tab-content');

  function switchTab(tabName) {
      tabButtons.forEach(btn => btn.classList.remove('active'));
      tabContents.forEach(content => content.classList.add('hidden'));

      const activeTabButton = document.querySelector(`.tab-button[data-tab="${tabName}"]`);
      const activeContent = document.getElementById(`${tabName}Tab`);

      if (activeTabButton && activeContent) {
          activeTabButton.classList.add('active');
          activeContent.classList.remove('hidden');
          activeContent.classList.add('fade-in');
      } else {
          console.warn("Tab not found:", tabName);
      }
  }

  // Attach events
  tabButtons.forEach(btn => {
      btn.addEventListener('click', () => {
          const tabName = btn.getAttribute('data-tab');
          switchTab(tabName);
      });
  });

  // Initialize the first tab
  switchTab('general');
});    
    




class LogoutModal {
        constructor() {
            this.modal = document.getElementById('logoutModal');
            this.logoutBtn = document.getElementById('logoutBtn');
            this.showModalBtn = document.getElementById('showModalBtn');
            this.closeModalBtn = document.getElementById('closeModalBtn');
            this.cancelBtn = document.getElementById('cancelBtn');
            this.confirmLogoutBtn = document.getElementById('confirmLogoutBtn');
            this.successMessage = document.getElementById('successMessage');
            
            this.init();
        }

        init() {
            if (this.logoutBtn) this.logoutBtn.addEventListener('click', () => this.showModal());
            if (this.showModalBtn) this.showModalBtn.addEventListener('click', () => this.showModal());
            if (this.closeModalBtn) this.closeModalBtn.addEventListener('click', () => this.hideModal());
            if (this.cancelBtn) this.cancelBtn.addEventListener('click', () => this.hideModal());
            if (this.confirmLogoutBtn) this.confirmLogoutBtn.addEventListener('click', () => this.confirmLogout());

            this.modal?.addEventListener('click', (e) => {
                if (e.target === this.modal || e.target.classList.contains('bg-black')) {
                    this.hideModal();
                }
            });

            document.addEventListener('keydown', (e) => {
                if (e.key === 'Escape' && !this.modal.classList.contains('hidden')) {
                    this.hideModal();
                }
            });
        }

        showModal() {
            this.modal.classList.remove('hidden');
            setTimeout(() => this.modal.classList.add('show'), 10);
            setTimeout(() => this.cancelBtn?.focus(), 300);
        }

        hideModal() {
            this.modal.classList.remove('show');
            setTimeout(() => this.modal.classList.add('hidden'), 300);
        }

        confirmLogout() {
            const originalText = this.confirmLogoutBtn.innerHTML;
            this.confirmLogoutBtn.innerHTML = `
                <svg class="animate-spin -ml-1 mr-2 h-4 w-4 text-white inline" fill="none" viewBox="0 0 24 24">
                    <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
                    <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                </svg>
                Logging out...`;
            this.confirmLogoutBtn.disabled = true;

            setTimeout(() => {
                this.hideModal();
                this.showSuccessMessage();
                this.confirmLogoutBtn.innerHTML = originalText;
                this.confirmLogoutBtn.disabled = false;

                // Redirect or perform actual logout
                // window.location.href = '/login';
            }, 1500);
        }
    }
let logoutModalInstance;

    document.addEventListener('DOMContentLoaded', () => {
        logoutModalInstance = new LogoutModal();

        document.querySelectorAll('[data-logout]').forEach(trigger => {
            trigger.addEventListener('click', (e) => {
                e.preventDefault();
                logoutModalInstance.showModal();
            });
        });
    });

    function showLogoutModal() {
        logoutModalInstance?.showModal();
    }

    function handleLogout() {
        logoutModalInstance?.showModal();
    }










    
    document.addEventListener("DOMContentLoaded", () => {
    const customerToken = localStorage.getItem("customer_access_token"); // Or sessionStorage

    fetch("http://127.0.0.1:8000/api/auth/me/", {
        method: "GET",
        headers: {
            "Authorization": `Bearer ${customerToken}`,
            "Content-Type": "application/json"
        }
    })
    .then(response => {
        if (!response.ok) {
            throw new Error("Failed to fetch user data");
        }
        return response.json();
    })
    .then(data => {
        console.log("User Info:", data);

        // Displaying user info in HTML
        document.querySelectorAll(".username").forEach(el => {
            el.textContent = data.username;
        });
        document.querySelectorAll(".email").forEach(el => {
            el.textContent = data.email;
        });
        document.querySelectorAll(".profile").forEach(el => {
            el.src = data.photo;
        });

        document.getElementById("email").textContent = data.email;
        document.getElementById("role").textContent = data.role;
        document.getElementById("photo").src = data.photo;
        // document.querySelectorAll(".profile-photo").src=data.photo;
        document.getElementById("generalRestaurantName").value = data.username || '';
        document.getElementById("emails").value = data.email || '';
        document.getElementById("generalid").value = data.id || '';
        document.getElementById("generalPhone").value = data.phone || '';
        document.getElementById("generalAddress").value = data.address || '';
        document.getElementById("dateJoined").value = data.date_joined || '';

    })
    .catch(error => {
        console.error("Error:", error);
    });
});




document.addEventListener("DOMContentLoaded", () => {
    const navButtons = document.querySelectorAll(".nav-item");
    const pages = document.querySelectorAll(".page-content");

    navButtons.forEach(button => {
        button.addEventListener("click", () => {
            const page = button.getAttribute("data-page");

            // Hide all pages
            pages.forEach(p => p.classList.add("hidden"));

            // Show the selected page
            const selectedPage = document.getElementById(`${page}Page`);
            if (selectedPage) {
                selectedPage.classList.remove("hidden");
            }
        });
    });
});

