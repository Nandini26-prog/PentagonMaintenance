import React from 'react'
import { useState } from 'react';
import namaste from './namaste.png'
import { Link } from "react-router-dom";
import { useNavigate } from "react-router-dom";
import axios from "axios";
import ForcastChart from './ForcastChart.js';

const UserDashboard = () => {
  const [selectedOption, setSelectedOption] = useState('Select a Machine');
  const [isDropdownOpen, setDropdownOpen] = useState(false);

  const toggleDropdown = () => {
    setDropdownOpen(!isDropdownOpen);
  };

  const handleOptionSelect = (option) => {
    setSelectedOption(option); // Update the placeholder to the selected option
    setDropdownOpen(false); // Close the dropdown
  };


  return (
    <>
      <nav
        style={{
          width: '100%',
          margin: 'auto',
          paddingTop: '20px',
          display: 'flex',
          justifyContent: 'space-between',
          alignItems: 'center',
          backgroundColor: '#0f172a',
        }}
      >
        <div
          style={{
            fontSize: '1.5rem',
            fontWeight: 'bold',
            marginLeft: '20px',
            marginBottom: '20px',
            display: 'inline-block',
          }}
        >
          <Link to={`/`}>
            <span style={{ color: '#f8f5f5' }}>Machine</span>
            <span style={{ color: 'orange' }}>Buddy</span>

          </Link>
        </div>

        <ul
          style={{
            display: 'flex',
            listStyleType: 'none',
            marginBottom: '20px',
          }}
        >
          <li style={{ margin: '15px', position: 'relative' }}>
            <Link
              to={`/dashboard`}
              style={{
                textDecoration: 'none',
                padding: '0.3rem 1.3rem',
                fontSize: '17px',
                fontWeight: 'bold',
                color: '#f8f5f5',
                position: 'relative',
                display: 'inline-block',
              }}
              onMouseEnter={(e) => {
                const underline = e.target.querySelector('.underline');
                if (underline) underline.style.width = '100%';
              }}
              onMouseLeave={(e) => {
                const underline = e.target.querySelector('.underline');
                if (underline) underline.style.width = '0%';
              }}
            >
              Home
              <span
                className="underline"
                style={{
                  display: 'block',
                  width: '0%',
                  height: '4px',
                  position: 'absolute',
                  bottom: '-2px',
                  left: '0',
                  backgroundColor: '#1565C0',
                  transition: 'width 0.5s ease',
                  borderRadius: '20px',
                }}
              />
            </Link>
          </li>

          {['Calender', 'Profile'].map((item, index) => (
            <li key={index} style={{ margin: '15px', position: 'relative' }}>
              <Link
                to={`/${item.toLowerCase()}`}
                style={{
                  textDecoration: 'none',
                  padding: '0.3rem 1.3rem',
                  fontSize: '17px',
                  fontWeight: 'bold',
                  color: '#f8f5f5',
                  position: 'relative',
                  display: 'inline-block',
                }}
                onMouseEnter={(e) => {
                  const underline = e.target.querySelector('.underline');
                  if (underline) underline.style.width = '100%';
                }}
                onMouseLeave={(e) => {
                  const underline = e.target.querySelector('.underline');
                  if (underline) underline.style.width = '0%';
                }}
              >
                {item}
                <span
                  className="underline"
                  style={{
                    display: 'block',
                    width: '0%',
                    height: '4px',
                    position: 'absolute',
                    bottom: '-2px',
                    left: '0',
                    backgroundColor: '#1565C0',
                    transition: 'width 0.5s ease',
                    borderRadius: '20px',
                  }}
                />
              </Link>
            </li>
          ))}

          <li style={{ margin: '15px' }}>
            <button
              style={{
                backgroundColor: '#ffffff',
                fontWeight: 'bold',
                padding: '0.5rem 1.3rem',
                borderRadius: '5px',
                transition: 'transform 0.2s ease, box-shadow 0.2s ease',
                color: '#1565C0',
                cursor: 'pointer',
              }}
              onMouseEnter={(e) => {
                e.target.style.transform = 'scale(1.05)';
                e.target.style.boxShadow = '0 0 10px rgba(0, 0, 0, 0.2)';
              }}
              onMouseLeave={(e) => {
                e.target.style.transform = 'scale(1)';
                e.target.style.boxShadow = 'none';
              }}
            >
              <Link
                to="/"
                style={{
                  textDecoration: 'none',
                  color: '#1565C0',
                }}
              >
                Log out
              </Link>
            </button>
          </li>
        </ul>
      </nav>
      <div
        style={{
          backgroundImage: `url(${namaste})`,
          backgroundSize: 'cover',
          backgroundRepeat: 'no-repeat',
          backgroundPosition: 'center',
          height: '120.5vh', // Set the height to cover the entire viewport
        }}
      >
        <div className=" text-white text-center p-6 ">
          <h1 className="text-4xl font-bold mb-4">Predictive Machine Maintenance</h1>
          <p className="text-xl mb-8">Utilize AI to prevent downtime and optimize maintenance schedules.</p>
          <div className="relative inline-block text-left">
            {/* Dropdown Placeholder Button */}
            <button
              onClick={toggleDropdown}
              className="bg-white text-black font-bold py-2 px-4 rounded "
            >
              {selectedOption}
            </button>

            {/* Dropdown Menu */}
            {isDropdownOpen && (
              <div className="absolute mt-2 w-48 bg-white rounded-md shadow-lg z-10">
                <ul className="py-1 text-gray-800">
                  <li
                    className="block px-4 py-2 hover:bg-blue-100 cursor-pointer"
                    onClick={() => handleOptionSelect('Lathe')}
                  >
                    Lathe
                  </li>
                  <li
                    className="block px-4 py-2 hover:bg-blue-100 cursor-pointer"
                    onClick={() => handleOptionSelect('CNC')}
                  >
                    CNC
                  </li>
                </ul>
              </div>
            )}
          </div>

          <div className=" text-white text-center p-6 ">
          <button
            className="bg-blue-800 text-white font-bold py-2 px-4 rounded transform transition-all hover:scale-105 hover:shadow-2xl hover:bg-blue-700"
          >
            <Link to="http://localhost:8505/" className="hover:text-gray-300">Live Analysis</Link>
          </button>
          </div>  
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
    </>
  )
}


export default UserDashboard;