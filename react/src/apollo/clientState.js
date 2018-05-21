import gql from "graphql-tag";
import { matchPath } from "react-router";

import { pathsWithRestaurantId } from "../components/App";

const resolvers = {
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

// Initialise currentRestaurantId with route
const match = matchPath(window.location.pathname, {
  path: pathsWithRestaurantId
});
const currentRestaurantId = (match && match.params.restaurantId) || "";

const defaults = {
  currentRestaurantId
};

const clientState = {
  resolvers,
  typeDefs,
  defaults
};

export default clientState;
