import ApolloClient from "apollo-boost";

import clientState from "./clientState";

const client = new ApolloClient({
  uri: "http://192.168.99.100:5000/graphql/restaurants", // TODO
  clientState
});

export default client;
