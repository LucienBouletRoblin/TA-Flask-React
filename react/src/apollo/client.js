import ApolloClient from "apollo-boost";

import clientState from "./clientState";

// Get graphqlEndpoint URI
let remoteEndpoint = process.env.ENDPOINT_URL;
if (!remoteEndpoint) {
  throw new Error(
    "You should override `.env.sample` in a `.env` file with appropriates value !"
  );
}
remoteEndpoint = remoteEndpoint.endsWith("/")
  ? remoteEndpoint
  : `${remoteEndpoint}/`;
const graphqlEndpoint = `${remoteEndpoint}graphql`;

const client = new ApolloClient({
  uri: graphqlEndpoint,
  clientState
});

export default client;
