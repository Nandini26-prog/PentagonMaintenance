import React from 'react';
import namaste from './namaste.png'
import { Link } from "react-router-dom";
import './Navbar.css';
const LandingPage = () => {
  return (
    <>
    <div>
    <nav className="navbar">
      <div className="navbar-logo">
        <Link to={`/`}>
        <span className="logo-machine">Machine</span>
        <span className="logo-buddy">Buddy</span>
        </Link>
      </div>
        <ul className="navbar-links">
          <li><Link to="/">Home</Link></li>
          <li><Link to="/Login">Log In</Link></li>
          <li><Link to="/Register">Register</Link></li>
        </ul>
    </nav>
    <div
      style={{
        backgroundImage: `url(${namaste})`,
        backgroundSize: 'cover',
        backgroundRepeat: 'no-repeat',
        backgroundPosition: 'center',
        height: '105.5vh', // Set the height to cover the entire viewport
      }}
    >
      <div className=" text-white text-center p-6 ">
        <h1 className="text-4xl font-bold mb-4">Predictive Machine Maintenance</h1>
        <p className="text-xl mb-8">Utilize AI to prevent downtime and optimize maintenance schedules.</p>
        <button
          className="bg-blue-800 text-white font-bold py-2 px-4 rounded transform transition-all hover:scale-105 hover:shadow-2xl hover:bg-blue-700"
        >
          <Link to="/register" className="hover:text-gray-300">Get Started</Link>
        </button>
      </div>
      <div className="py-12">
        <div className="max-w-4xl mx-auto grid grid-cols-1 md:grid-cols-3 gap-6">
          {/* Feature 1 */}
          <div className="text-center bg-gray-200 p-6 max-w-sm mx-auto rounded-lg shadow-md transform transition-all hover:scale-105 hover:shadow-2xl hover:bg-gray-300">
            <h2 className="font-bold text-lg">Real-Time Monitoring</h2>
            <p>Monitor systems in real-time to detect issues before they escalate.</p>
          </div>
          {/* Feature 2 */}
          <div className="text-center bg-gray-200 p-6 max-w-sm mx-auto rounded-lg shadow-md transform transition-all hover:scale-105 hover:shadow-2xl hover:bg-gray-300">
            <h2 className="font-bold text-lg">Predictive Analysis</h2>
            <p>Our AI algorithms predict failures and suggest the optimal maintenance schedule.</p>
          </div>
          {/* Feature 3 */}
          <div className="text-center bg-gray-200 p-6 max-w-sm mx-auto rounded-lg shadow-md transform transition-all hover:scale-105 hover:shadow-2xl hover:bg-gray-300">
            <h2 className="font-bold text-lg">Cost Reduction</h2>
            <p>Reduce maintenance costs by preventing unnecessary repairs and downtime.</p>
          </div>
        </div>
      </div>
      <div
        style={{
          backgroundColor: 'rgba(243, 244, 246, 0.8)', // Equivalent to gray-100 with 80% opacity
          padding: '1.5rem', // py-6 equivalent
        }}
      >
        <div className="max-w-4xl mx-auto">
          <h2 className="text-center font-bold text-2xl mb-4">
            The Power of AI in Maintenance
          </h2>
          <p>
            By harnessing the power of AI and predictive modeling, our app analyzes
            data from your systems to forecast potential issues, ensuring
            that maintenance can be conducted just in time to prevent failures. This
            proactive approach guarantees the longevity of your equipment and
            minimizes downtime.
          </p>
        </div>
      </div>
    </div>
    </div>
    </>
  );
};

export default LandingPage;
