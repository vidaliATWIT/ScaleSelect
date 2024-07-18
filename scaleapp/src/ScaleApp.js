import React, { useState, useEffect } from 'react';
import axios from 'axios'
import Panel from './Panel'

function ScaleApp() {
    const [message, setMessage] = useState('');
  
    useEffect(() => {
      axios.get('http://ec2-3-15-33-68.us-east-2.compute.amazonaws.com/api/generate-scale/')
        .then(response => {
          setMessage(response.data.message);
        })
        .catch(error => {
          console.log(error);
        });
    }, []);
  
    const handleClick = async () => {
      try {
        const response = await axios.get('http://ec2-3-15-33-68.us-east-2.compute.amazonaws.com/api/generate-scale/');
        setMessage(response.data.message); 
        console.log('Button clicked and message fetched!');
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };

    return (
      <div>
        <Panel text={message} onClick={handleClick} />
      </div>
    );
  }
  
  export default ScaleApp;
