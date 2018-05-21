import ApolloClient from "apollo-boost";
import gql from "graphql-tag";

export const resolvers = {
  Mutation: {
    setCurrentRestaurantId: (_, variables, { cache, getCacheKey }) => {
      cache.writeData({ data: { currentRestaurantId: variables.id } });
      return variables.id;
    }
  }
};

const typeDefs = `
  type Mutation {
    setCurrentRestaurantId(id: ID): ID
  }

  type Query {
    currentRestaurantId: ID
  }
`;

const defaults = {
  currentRestaurantId: ""
};

const client = new ApolloClient({
  uri: "http://192.168.99.100:5000/graphql/restaurants", // TODO
  clientState: {
    defaults,
    resolvers,
    typeDefs
  }
});

export default client;
