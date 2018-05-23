import React from "react";
import { Form, Field } from "react-final-form";
import Button from "@material-ui/core/Button";
import TextField from "../components/formComponents/TextInput";
import gql from "graphql-tag";
import { Mutation } from "react-apollo";

const validate = values => {
  if (!values.name) return { name: "Required !" };
};

const CREATE_RESTAURANT = gql`
  mutation createRestaurant(
    $name: String!
    $address: String
    $email: String
    $userId: ID!
  ) {
    createRestaurant(
      name: $name
      address: $address
      email: $email
      userId: $userId
    ) {
      restaurant {
        id
      }
      ok
    }
  }
`;

/*
ça marche pas car le submitting reste toujours true
onSubmit={(values, form, callback) => new Promise(resolve => {
                    createRestaurant({ variables: { ...values, userId: 1 } })
                        .then(({ ...args }) => {
                            console.log('resole', args)
                            resolve(values)
                        })
                })}
*/
//TODO design
//TODO update cache
const RestaurantForm = ({ location: { state: { restaurant } = {} } }) => (
  <Mutation mutation={CREATE_RESTAURANT}>
    {(createRestaurant, { loading }) => (
      <Form
        onSubmit={(values, form, callback) => {
          createRestaurant({ variables: { ...values, userId: 1 } }).then(
            ({ ...args }) => {
              console.log("submitted !", args);
            }
          );
        }}
        initialValues={restaurant}
        validate={validate}
        render={({ handleSubmit, reset, submitting, pristine, values }) => (
          <form onSubmit={handleSubmit}>
            <h3>
              {restaurant && restaurant.id
                ? `Edit restaurant ${restaurant.id}`
                : "Create new restaurant"}
            </h3>
            <div style={{ marginBottom: "1em" }}>
              <Field
                name="name"
                component={TextField}
                type="text"
                label="Name"
                required
              />
              <Field
                name="email"
                component={TextField}
                type="email"
                label="Email"
              />
              <Field
                name="address"
                component={TextField}
                type="text"
                label="Address"
              />
            </div>
            <Button
              type="submit"
              variant="raised"
              color="primary"
              disabled={loading}
            >
              {loading ? "Saving..." : "Save"}
            </Button>
          </form>
        )}
      />
    )}
  </Mutation>
);

export default RestaurantForm;
