import React from 'react';
import { features } from '../data/mock';

const About = () => {
  return (
    <div className="min-h-screen bg-gray-50">
      {/* Hero Section */}
      <section className="bg-gradient-to-r from-orange-500 to-amber-500 text-white py-20">
        <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
          <h1 className="text-4xl md:text-5xl font-bold mb-4">About Freshwala</h1>
          <p className="text-xl md:text-2xl text-white/90">
            Bringing Traditional Flavors to Modern Homes
          </p>
        </div>
      </section>

      {/* Story Section */}
      <section className="py-16 bg-white">
        <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
          <h2 className="text-3xl font-bold text-gray-900 mb-6">Our Story</h2>
          <div className="space-y-4 text-gray-700 leading-relaxed">
            <p>
              Freshwala was born out of a deep love for authentic South Indian flavors and traditional home cooking. We noticed that in today's fast-paced world, many families struggle to find the time to prepare traditional items like homemade pickles, fresh batters, and spice powders from scratch.
            </p>
            <p>
              Our mission is simple: to bring the rich taste of Andhra & Telangana kitchens straight to your home, prepared with love and age-old recipes passed down through generations. Every product at Freshwala is crafted with the same care and attention that goes into homemade preparations.
            </p>
            <p>
              We source only the finest ingredients and maintain strict quality standards to ensure that every jar of pickle, every batch of batter, and every packet of spice powder meets our high expectations. Because for us, it's not just about selling products—it's about sharing tradition, taste, and the warmth of home-cooked goodness.
            </p>
          </div>
        </div>
      </section>

      {/* Features */}
      <section className="py-16 bg-gradient-to-b from-white to-orange-50">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <h2 className="text-3xl font-bold text-center text-gray-900 mb-12">What Makes Us Special</h2>
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
            {features.map((feature) => (
              <div key={feature.id} className="text-center space-y-4">
                <div className="w-24 h-24 mx-auto rounded-full overflow-hidden shadow-lg">
                  <img
                    src={feature.icon}
                    alt={feature.title}
                    className="w-full h-full object-cover"
                  />
                </div>
                <h3 className="text-xl font-bold text-gray-900">{feature.title}</h3>
                <p className="text-gray-600">{feature.description}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Values Section */}
      <section className="py-16 bg-white">
        <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
          <h2 className="text-3xl font-bold text-gray-900 mb-8 text-center">Our Values</h2>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
            <div className="text-center">
              <div className="bg-orange-100 w-16 h-16 rounded-full flex items-center justify-center mx-auto mb-4">
                <span className="text-3xl">🌿</span>
              </div>
              <h3 className="font-bold text-gray-900 mb-2">Quality First</h3>
              <p className="text-gray-600 text-sm">
                We never compromise on the quality of our ingredients or preparation methods.
              </p>
            </div>
            <div className="text-center">
              <div className="bg-orange-100 w-16 h-16 rounded-full flex items-center justify-center mx-auto mb-4">
                <span className="text-3xl">❤️</span>
              </div>
              <h3 className="font-bold text-gray-900 mb-2">Made with Love</h3>
              <p className="text-gray-600 text-sm">
                Every product is prepared with the same care as a home-cooked meal.
              </p>
            </div>
            <div className="text-center">
              <div className="bg-orange-100 w-16 h-16 rounded-full flex items-center justify-center mx-auto mb-4">
                <span className="text-3xl">🤝</span>
              </div>
              <h3 className="font-bold text-gray-900 mb-2">Customer Trust</h3>
              <p className="text-gray-600 text-sm">
                Building lasting relationships through consistent quality and service.
              </p>
            </div>
          </div>
        </div>
      </section>
    </div>
  );
};

export default About;
