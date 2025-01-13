import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import { useNavigate } from "react-router-dom";
import { useEffect } from 'react';
import axios from "axios";

//Calendar display
const daysInMonth = (year, month) => new Date(year, month, 0).getDate();
const month = 2; // April (months are 0-indexed)
const year = 2024;
const days = Array.from({ length: daysInMonth(year, month + 1) }, (_, i) => i + 1);

const Calender = () => {
  const navigate = useNavigate();
  const updateUserReminders = async (email, updatedReminders) => {
    try {
      // Make a POST request to your API endpoint
      const response = await axios.post('http://localhost:8000/updateUserReminders', {
        email,
        reminders: reminders
      });

      // Check if the update was successful
      if (response.status === 200) {
        // Update the local storage item named 'rem' with the new reminders data
        localStorage.setItem('rem', JSON.stringify(reminders));
        console.log('Reminders updated successfully.');
      } else {
        console.error('Failed to update reminders.');
      }
    } catch (error) {
      console.error('Error updating reminders:', error);
    }
  };
  const type = localStorage.getItem("type")
  const [expanded, setExpanded] = useState(true)
  const logout = () => {

    localStorage.removeItem("token");
    localStorage.removeItem("type");
    navigate("/");
  };
  const [reminders, setReminders] = useState(() => {
    // Load reminders from localStorage or initialize to an empty object
    const storedReminders = localStorage.getItem('reminders');
    return storedReminders ? JSON.parse(storedReminders) : {};
  });
  const handleDayClick = (day) => {
    const reminder = prompt(`Set reminder for March ${day}, 2024:`);
    if (reminder) {
      setReminders({ ...reminders, [day]: reminder });
    }
  };
  useEffect(() => {
    // Update localStorage whenever reminders change
    const email = localStorage.getItem('email');
    updateUserReminders(email, JSON.stringify(reminders));
    localStorage.setItem('reminders', JSON.stringify(reminders));
  }, [reminders]);

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
          {['Profile'].map((item, index) => (
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
      <div className="text-5xl">
        <b style={{ 'marginLeft': '150px' }}>January 2025</b>
      </div>

      <div className="grid grid-cols-7 gap-4 p-4" style={{ 'marginLeft': '150px', 'marginRight': '150px' }}>
        {days.map((day) => (
          <div key={day} className="border-4 border-blue-500 p-4 flex flex-col" style={{ 'borderStyle': 'double' }}>
            <button onClick={() => handleDayClick(day)} className="text-lg font-bold">
              {day}
            </button>
            <div className="mt-2 text-sm">{reminders[day]}</div>
          </div>
        ))}
      </div>
    </>
  );
};

export default Calender;
