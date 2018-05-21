import React from "react";
import ReactDOM from "react-dom";
import normalize from "normalize.css";
import { ApolloProvider } from "react-apollo";

import apolloClient from "./apollo/client";
import App from "./components/App";

// In the default template, body is empty. We must
// create a div to mount the app.
if (!document.getElementById("app")) {
  const divElem = document.createElement("div");
  divElem.id = "app";
  document.body.appendChild(divElem);
}

const Root = () => (
  <ApolloProvider client={apolloClient}>
    <App />
  </ApolloProvider>
);
ReactDOM.render(<Root />, document.getElementById("app"));

module.hot.accept();
