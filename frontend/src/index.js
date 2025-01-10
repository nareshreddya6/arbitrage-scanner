import React from "react";
import ReactDOM from "react-dom";
import "./index.css"; // Optional if you have a global CSS file
import ArbitrageDashboard from "./ArbitrageDashboard"; // Import your main component

ReactDOM.render(
  <React.StrictMode>
    <ArbitrageDashboard />
  </React.StrictMode>,
  document.getElementById("root") // Attach to the `div` in index.html
);
