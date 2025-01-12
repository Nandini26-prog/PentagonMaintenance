import React, { useEffect } from 'react'
import { useState } from 'react';
import { Link } from "react-router-dom";
import { useNavigate } from "react-router-dom";
import profile from '../images/profile.png'
//import LeaderBoard from './LeaderBoard';
import Feedback from './Feedback';


const ProfilePage = () => {
  const navigate = useNavigate();
  const email = localStorage.getItem("email")
  const type = localStorage.getItem("type")
  console.log(email, " type is: ", type)
  const logout = () => {
    localStorage.removeItem("token");
    localStorage.removeItem("type");
    navigate("/");
  };

  const getUserData = async () => {
    try {

      const response = await fetch(`http://localhost:8000/${email}/getUserData`);

      if (response.ok) {
        const result = await response.json();


      }


    }
    catch (err) {
      console.log("error in get,", err);
    }
  }





  useEffect(() => {
    getUserData();


  }, [])
  // console.log("selected users", languageUsers)







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
          {['Calender'].map((item, index) => (
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
      <h1 className="text-center font-bold text-5xl mt-10 mb-10">Welcome to profile page</h1>

      <div className="flex justify-center">
        <div className="border-solid border-2 border-black p-3 rounded-lg m-10">
          <img src={profile} alt="profile img" width="200" height="200" style={{
            borderTopLeftRadius: '10px',
            borderTopRightRadius: '10px',
            borderBottomLeftRadius: '10px',
            borderBottomRightRadius: '10px',
          }} />
        </div>

        <div className="border-solid border-2 border-black p-4 m-10 flex flex-col gap-10">
          <h1 className="text-3xl font-bold">Email:{email}</h1>

        </div>
      </div>
      <Feedback />




    </>
  )
}

export default ProfilePage