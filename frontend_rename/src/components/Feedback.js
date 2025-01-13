import React, { useState } from "react";

const MachinePredictionForm = () => {
  // State for input fields
  const [inputField1, setInputField1] = useState("");
  const [inputField2, setInputField2] = useState("");

  // Handle changes in input fields
  const handleInputChange1 = (event) => {
    setInputField1(event.target.value);
  };

  const handleInputChange2 = (event) => {
    setInputField2(event.target.value);
  };

  // Handle form submission
  const handleSubmit = (event) => {
    event.preventDefault();
    // Example: Sending data to an API
    console.log("Input Field 1:", inputField1);
    console.log("Input Field 2:", inputField2);
    // Perform any additional logic, e.g., API call
  };

  return (
    <div className="flex justify-center items-center ">
    <form onSubmit={handleSubmit}>
      <div>
      <h1 className="text-3xl text-center ">Machine Health Inputs</h1>
        <label htmlFor="field1">Last Service Date</label>
        <input
          id="field1"
          type="text"
          value={inputField1}
          onChange={handleInputChange1}
          required
          class="bg-gray-50 
          border border-gray-300 
          text-black text-sm 
          rounded-lg 
          focus:ring-blue-500 
          focus:border-blue-500 
          block w-full p-2.5  
          dark:border-gray-600 
          dark:placeholder-gray-400 
          dark:text-white 
          dark:focus:ring-blue-500 
          dark:focus:border-blue-500"
        />
      </div>
      <div>
        <label htmlFor="field2">Average Working Hours</label>
        <input
          id="field2"
          type="text"
          value={inputField2}
          onChange={handleInputChange2}
          required
          class="bg-gray-50 
          border border-gray-300 
          text-black text-sm 
          rounded-lg 
          focus:ring-blue-500 
          focus:border-blue-500 
          block w-full p-2.5  
          dark:border-gray-600 
          dark:placeholder-gray-400 
          dark:text-white 
          dark:focus:ring-blue-500 
          dark:focus:border-blue-500"
        />
      </div>
      <br/>
      <button type="button" class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 me-2 mb-2 dark:bg-blue-600 dark:hover:bg-blue-700 focus:outline-none dark:focus:ring-blue-800 text-center" onClick={handleSubmit}>Submit</button>
    </form>
    </div>
  );
};

export default MachinePredictionForm;
