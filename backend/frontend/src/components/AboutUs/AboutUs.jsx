import React from 'react';
import './AboutUs.css';
import HeroSection from './sections/HeroSection';
import ValuesSection from './sections/ValuesSection';
import StorySection from './sections/StorySection';
import ServicesSection from './sections/ServicesSection';
import CTASection from './sections/CTASection';

const AboutUs = () => {
  return (
    <div className="about-us">
      <HeroSection />
      <ValuesSection />
      <StorySection />
      <ServicesSection />
      <CTASection />
    </div>
  );
};

export default AboutUs;
