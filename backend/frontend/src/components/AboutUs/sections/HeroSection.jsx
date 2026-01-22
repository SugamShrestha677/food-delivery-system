import React from 'react';

const HeroSection = () => {
  return (
    <section className="hero-section">
      <div className="hero-container">
        <div className="hero-content">
          <h1 className="hero-title">Transforming Food Delivery</h1>
          <p className="hero-subtitle">
            We're building the future of food delivery by creating meaningful connections between customers, restaurants, and delivery partners across the nation.
          </p>
        </div>
        
        <div className="stats-container">
          <div className="stat-card">
            <div className="stat-content">
              <div className="stat-number">50k +</div>
              <div className="stat-label">Happy Customers</div>
            </div>
          </div>
          
          <div className="stat-card">
            <div className="stat-content">
              <div className="stat-number">100 +</div>
              <div className="stat-label">Partner Restaurants</div>
            </div>
          </div>
          
          <div className="stat-card">
            <div className="stat-content">
              <div className="stat-number">400K+</div>
              <div className="stat-label">Deliveries Completed</div>
            </div>
          </div>
          
          <div className="stat-card">
            <div className="stat-content">
              <div className="stat-number">10+</div>
              <div className="stat-label">Cities Served</div>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};

export default HeroSection;
