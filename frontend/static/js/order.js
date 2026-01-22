// Sample orders data
        let orders = [
            {
                id: 'ORD-963',
                customer: 'Emma Wilson',
                phone: '+1-555-5257',
                items: 'Chicken Pasta, Garlic Bread',
                status: 'pending',
                time: '11:54 AM',
                total: '$16.00'
            },
            {
                id: 'ORD-957',
                customer: 'James Miller',
                phone: '+1-555-6014',
                items: 'Fish & Chips, Fries',
                status: 'pending',
                time: '11:53 AM',
                total: '$34.00'
            },
            {
                id: 'ORD-962',
                customer: 'Sophie Taylor',
                phone: '+1-555-8297',
                items: 'Burger Deluxe, Soup',
                status: 'pending',
                time: '11:49 AM',
                total: '$40.00'
            },
            {
                id: 'ORD-961',
                customer: 'David Brown',
                phone: '+1-555-4521',
                items: 'Burger Deluxe, Fries',
                status: 'pending',
                time: '11:46 AM',
                total: '$26.00'
            },
            {
                id: 'ORD-960',
                customer: 'Lisa Chen',
                phone: '+1-555-7890',
                items: 'Margherita Pizza',
                status: 'preparing',
                time: '11:30 AM',
                total: '$22.00'
            },
            {
                id: 'ORD-959',
                customer: 'Mike Johnson',
                phone: '+1-555-3456',
                items: 'Caesar Salad, Breadsticks',
                status: 'preparing',
                time: '11:25 AM',
                total: '$18.50'
            },
            {
                id: 'ORD-958',
                customer: 'Sarah Davis',
                phone: '+1-555-9876',
                items: 'Pasta Carbonara',
                status: 'delivered',
                time: '10:45 AM',
                total: '$24.00'
            },
            {
                id: 'ORD-956',
                customer: 'Tom Wilson',
                phone: '+1-555-2468',
                items: 'Chicken Parmesan',
                status: 'cancelled',
                time: '10:30 AM',
                total: '$28.00'
            }
        ];

        let filteredOrders = [...orders];
        let currentFilter = 'all';

        // Mobile menu functionality
        const mobileMenuBtn = document.getElementById('mobileMenuBtn');
        const sidebar = document.getElementById('sidebar');
        const mobileOverlay = document.getElementById('mobileOverlay');

        function toggleMobileMenu() {
            sidebar.classList.toggle('sidebar-hidden');
            mobileOverlay.classList.toggle('hidden');
        }

        mobileMenuBtn.addEventListener('click', toggleMobileMenu);
        mobileOverlay.addEventListener('click', toggleMobileMenu);

        // Status badge styling
        function getStatusBadge(status) {
            const badges = {
                pending: 'px-2 py-1 bg-brand-light-yellow text-brand-orange text-xs rounded-full',
                preparing: 'px-2 py-1 bg-blue-100 text-brand-blue text-xs rounded-full',
                ready: 'px-2 py-1 bg-green-100 text-brand-green text-xs rounded-full',
                delivered: 'px-2 py-1 bg-green-100 text-brand-green text-xs rounded-full',
                cancelled: 'px-2 py-1 bg-red-100 text-brand-red text-xs rounded-full'
            };
            return badges[status] || badges.pending;
        }

        // Action buttons based on status
        function getActionButtons(order) {
            const { status, id } = order;
            
            switch(status) {
                case 'pending':
                    return `
                        <button class="accept-btn px-3 py-1 bg-brand-green hover:bg-brand-green/90 text-white text-sm rounded transition-colors mr-2" data-id="${id}">
                            Accept
                        </button>
                        <button class="cancel-btn px-3 py-1 bg-brand-red hover:bg-brand-red/90 text-white text-sm rounded transition-colors mr-2" data-id="${id}">
                            Cancel
                        </button>
                        <button class="view-btn p-1 text-brand-gray hover:text-brand-orange transition-colors" data-id="${id}">
                            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"></path>
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"></path>
                            </svg>
                        </button>
                    `;
                case 'preparing':
                    return `
                        <button class="ready-btn px-3 py-1 bg-brand-green hover:bg-brand-green/90 text-white text-sm rounded transition-colors mr-2" data-id="${id}">
                            Mark Ready
                        </button>
                        <button class="view-btn p-1 text-brand-gray hover:text-brand-orange transition-colors" data-id="${id}">
                            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"></path>
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"></path>
                            </svg>
                        </button>
                    `;
                case 'ready':
                    return `
                        <button class="deliver-btn px-3 py-1 bg-brand-green hover:bg-brand-green/90 text-white text-sm rounded transition-colors mr-2" data-id="${id}">
                            Mark Delivered
                        </button>
                        <button class="view-btn p-1 text-brand-gray hover:text-brand-orange transition-colors" data-id="${id}">
                            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"></path>
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"></path>
                            </svg>
                        </button>
                    `;
                default:
                    return `
                        <button class="view-btn p-1 text-brand-gray hover:text-brand-orange transition-colors" data-id="${id}">
                            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"></path>
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"></path>
                            </svg>
                        </button>
                    `;
            }
        }

        // Render orders table
        function renderOrders() {
            const tbody = document.getElementById('ordersTableBody');
            const emptyState = document.getElementById('emptyState');
            
            if (filteredOrders.length === 0) {
                tbody.innerHTML = '';
                emptyState.classList.remove('hidden');
                return;
            }
            
            emptyState.classList.add('hidden');
            
            tbody.innerHTML = filteredOrders.map(order => `
                <tr class="border-b border-brand-light-gray order-row fade-in" data-status="${order.status}">
                    <td class="p-4 text-sm text-black font-medium">${order.id}</td>
                    <td class="p-4">
                        <div class="text-sm text-black font-medium">${order.customer}</div>
                        <div class="text-xs text-brand-gray">${order.phone}</div>
                    </td>
                    <td class="p-4 text-sm text-brand-gray">${order.items}</td>
                    <td class="p-4">
                        <span class="${getStatusBadge(order.status)}">${order.status.charAt(0).toUpperCase() + order.status.slice(1)}</span>
                    </td>
                    <td class="p-4 text-sm text-brand-gray">
                        <div class="flex items-center gap-1">
                            <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"></path>
                            </svg>
                            ${order.time}
                        </div>
                    </td>
                    <td class="p-4 text-sm text-black font-medium">${order.total}</td>
                    <td class="p-4">
                        <div class="flex items-center gap-1">
                            ${getActionButtons(order)}
                        </div>
                    </td>
                </tr>
            `).join('');
            
            // Add event listeners to action buttons
            addActionListeners();
        }

        // Add event listeners to action buttons
        function addActionListeners() {
            // Accept buttons
            document.querySelectorAll('.accept-btn').forEach(btn => {
                btn.addEventListener('click', function() {
                    const orderId = this.dataset.id;
                    updateOrderStatus(orderId, 'preparing');
                });
            });

            // Cancel buttons
            document.querySelectorAll('.cancel-btn').forEach(btn => {
                btn.addEventListener('click', function() {
                    const orderId = this.dataset.id;
                    updateOrderStatus(orderId, 'cancelled');
                });
            });

            // Ready buttons
            document.querySelectorAll('.ready-btn').forEach(btn => {
                btn.addEventListener('click', function() {
                    const orderId = this.dataset.id;
                    updateOrderStatus(orderId, 'ready');
                });
            });

            // Deliver buttons
            document.querySelectorAll('.deliver-btn').forEach(btn => {
                btn.addEventListener('click', function() {
                    const orderId = this.dataset.id;
                    updateOrderStatus(orderId, 'delivered');
                });
            });

            // View buttons
            document.querySelectorAll('.view-btn').forEach(btn => {
                btn.addEventListener('click', function() {
                    const orderId = this.dataset.id;
                    viewOrderDetails(orderId);
                });
            });
        }

        // Update order status
        function updateOrderStatus(orderId, newStatus) {
            const orderIndex = orders.findIndex(order => order.id === orderId);
            if (orderIndex !== -1) {
                orders[orderIndex].status = newStatus;
                
                // Add success animation
                const row = document.querySelector(`tr[data-status="${orders[orderIndex].status}"]`);
                if (row) {
                    row.style.backgroundColor = '#f0fdf4';
                    setTimeout(() => {
                        row.style.backgroundColor = '';
                    }, 1000);
                }
                
                updateCounts();
                filterOrders();
                renderOrders();
            }
        }

        // View order details (placeholder)
        function viewOrderDetails(orderId) {
            const order = orders.find(order => order.id === orderId);
            if (order) {
                alert(`Order Details:\n\nID: ${order.id}\nCustomer: ${order.customer}\nPhone: ${order.phone}\nItems: ${order.items}\nStatus: ${order.status}\nTime: ${order.time}\nTotal: ${order.total}`);
            }
        }

        // Update counts
        function updateCounts() {
            const counts = {
                all: orders.length,
                pending: orders.filter(o => o.status === 'pending').length,
                preparing: orders.filter(o => o.status === 'preparing').length,
                ready: orders.filter(o => o.status === 'ready').length,
                delivered: orders.filter(o => o.status === 'delivered').length,
                cancelled: orders.filter(o => o.status === 'cancelled').length
            };

            // Update status cards
            document.getElementById('totalOrdersCount').textContent = counts.all;
            document.getElementById('pendingCount').textContent = counts.pending;
            document.getElementById('preparingCount').textContent = counts.preparing;
            document.getElementById('readyCount').textContent = counts.ready;
            document.getElementById('deliveredCount').textContent = counts.delivered;
            document.getElementById('cancelledCount').textContent = counts.cancelled;

            // Update tab counts
            document.getElementById('allTabCount').textContent = counts.all;
            document.getElementById('pendingTabCount').textContent = counts.pending;
            document.getElementById('preparingTabCount').textContent = counts.preparing;
            document.getElementById('readyTabCount').textContent = counts.ready;
            document.getElementById('deliveredTabCount').textContent = counts.delivered;
            document.getElementById('cancelledTabCount').textContent = counts.cancelled;
        }

        // Filter orders
        function filterOrders() {
            const searchTerm = document.getElementById('searchInput').value.toLowerCase();
            const statusFilter = document.getElementById('statusFilter').value;
            
            filteredOrders = orders.filter(order => {
                const matchesSearch = !searchTerm || 
                    order.id.toLowerCase().includes(searchTerm) ||
                    order.customer.toLowerCase().includes(searchTerm) ||
                    order.items.toLowerCase().includes(searchTerm);
                
                const matchesStatus = currentFilter === 'all' || order.status === currentFilter;
                const matchesDropdown = statusFilter === 'all' || order.status === statusFilter;
                
                return matchesSearch && matchesStatus && matchesDropdown;
            });
        }

        // Tab functionality
        document.querySelectorAll('.tab-button').forEach(btn => {
            btn.addEventListener('click', function() {
                // Remove active class from all tabs
                document.querySelectorAll('.tab-button').forEach(tab => {
                    tab.classList.remove('active');
                });
                
                // Add active class to clicked tab
                this.classList.add('active');
                
                // Update current filter
                currentFilter = this.dataset.status;
                
                // Filter and render orders
                filterOrders();
                renderOrders();
            });
        });

        // Search functionality
        document.getElementById('searchInput').addEventListener('input', function() {
            filterOrders();
            renderOrders();
        });

        // Status filter functionality
        document.getElementById('statusFilter').addEventListener('change', function() {
            filterOrders();
            renderOrders();
        });

        // Add new order simulation
        function addNewOrder() {
            const newOrderIds = ['ORD-964', 'ORD-965', 'ORD-966', 'ORD-967'];
            const customers = ['Alex Thompson', 'Maria Garcia', 'John Smith', 'Emily Davis'];
            const phones = ['+1-555-1111', '+1-555-2222', '+1-555-3333', '+1-555-4444'];
            const items = ['Spaghetti Bolognese', 'Chicken Caesar Wrap', 'Vegetarian Pizza', 'Grilled Salmon'];
            const totals = ['$28.50', '$15.00', '$32.00', '$42.00'];
            
            const randomIndex = Math.floor(Math.random() * newOrderIds.length);
            const currentTime = new Date().toLocaleTimeString('en-US', { 
                hour: 'numeric', 
                minute: '2-digit',
                hour12: true 
            });
            
            const newOrder = {
                id: newOrderIds[randomIndex],
                customer: customers[randomIndex],
                phone: phones[randomIndex],
                items: items[randomIndex],
                status: 'pending',
                time: currentTime,
                total: totals[randomIndex]
            };
            
            orders.unshift(newOrder);
            updateCounts();
            filterOrders();
            renderOrders();
            
            // Show notification
            showNotification(`New order ${newOrder.id} received from ${newOrder.customer}`);
        }

        // Show notification
        function showNotification(message) {
            const notification = document.createElement('div');
            notification.className = 'fixed top-4 right-4 bg-brand-orange text-white px-6 py-3 rounded-lg shadow-lg z-50 notification-badge';
            notification.textContent = message;
            
            document.body.appendChild(notification);
            
            setTimeout(() => {
                notification.remove();
            }, 3000);
        }

        // Initialize
        document.addEventListener('DOMContentLoaded', function() {
            updateCounts();
            filterOrders();
            renderOrders();
            
            // Add new order every 30 seconds
            setInterval(addNewOrder, 30000);
            
            // Auto-update counts every 10 seconds
            setInterval(updateCounts, 10000);
        });

        // Responsive handling
        window.addEventListener('resize', function() {
            if (window.innerWidth < 768) {
                sidebar.classList.add('sidebar-hidden');
                mobileOverlay.classList.add('hidden');
            }
        });