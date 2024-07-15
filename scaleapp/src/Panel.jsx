import React from 'react';

function Panel(props) {
  const { text, onClick } = props;

  return (
    <div className="panel">
      <h1>Scale Generator</h1>
      <h3>{text}</h3>  
      <button className="panel-button" onClick={onClick}>Click Me</button>
    </div>
  );
}

export default Panel;