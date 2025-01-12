import React from 'react'
import { Link } from "react-router-dom";
import { useNavigate } from "react-router-dom";
import heatmap from '../images/top5.png'
import img1 from '../images/box_plot.png'
import img2 from '../images/feature_weights_plot.png'
import img3 from '../images/xgb_importance_plot.png'

const Reports = () => {
  const navigate = useNavigate();
  const logout = () => {
    localStorage.removeItem("token");
    localStorage.removeItem("type");
    navigate("/");
  };
  const type = localStorage.getItem("type")
  return (
    <div>
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
              to={`/`}
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


      <div className="flex justify-center items-center" style={{margin:'50px', marginBottom: '30px'}}>
        <div className=''>
          <div className='text-2xl font-bold text-center'>Parameter vs. Fault Severity</div>

          <img src={img2} alt="heatmap" height="500" width="500" />
        </div>
      </div>
      <div className="flex justify-center items-center" style={{margin:'50px', marginBottom: '30px'}}>
        <div className='mt-8'>
          <div className='text-2xl font-bold text-center mt-4'>Threshold Exceedance Visualization:</div>
          <div><br></br></div>
          <img src={img3} alt="avp" height="500" width="550" />
        </div>
      </div>
      <div className="flex justify-center items-center" style={{margin:'50px', marginBottom: '30px'}}>
        <div className='mt-6'>
          <div className='text-2xl font-bold text-center'>Heat Map for Component-Wise Fault Severity</div>
          <div><br></br></div>
          <img src={heatmap} alt="heatmap" height="500" width="500" />
        </div>
      </div>
      <div className="flex justify-center items-center" style={{margin:'50px', marginBottom: '30px'}}>

        <div>
          <div className='text-2xl font-bold text-center'>Heat Correlation Visualization</div>
          <div><br></br></div>
          <img src={img1} alt="avp" height="550" width="550" />
        </div>
      </div>
    </div>
  )
}

export default Reports