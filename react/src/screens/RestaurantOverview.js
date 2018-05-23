import React from "react";
import { Link } from "react-router-dom";
import { Query } from "react-apollo";
import gql from "graphql-tag";

const GET_RESTAURANT = gql`
  query restaurant($id: ID!) {
    restaurant(id: $id) {
      id
      name
      email
      address
    }
  }
`;

const RestaurantOverview = ({
  match: {
    params: { restaurantId }
  }
}) => (
  <Query query={GET_RESTAURANT} variables={{ id: restaurantId }}>
    {({ loading, error, data: { restaurant } }) => {
      if (error) return error.name;
      if (loading) return "loading";
      return (
        <div>
          <h3>This is RestaurantOverview of restaurant #{restaurant.id}</h3>
          <span>name: {restaurant.name}</span>
          <br />
          <span>email: {restaurant.email}</span>
          <br />
          <span>address: {restaurant.address}</span>
          <br />
          <Link
            to={{
              pathname: `/${restaurant.id}/edit`,
              state: { restaurant }
            }}
          >
            Edit
          </Link>
        </div>
      );
    }}
  </Query>
);

export default RestaurantOverview;
