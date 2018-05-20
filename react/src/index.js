import React from "react";
import ReactDOM from "react-dom";
import normalize from "normalize.css";

import App from "./components/App";

// In the default template, body is empty. We must
// create a div to mount the app.
if (!document.getElementById("app")) {
  const divElem = document.createElement("div");
  divElem.id = "app";
  document.body.appendChild(divElem);
}

ReactDOM.render(<App />, document.getElementById("app"));

module.hot.accept();
