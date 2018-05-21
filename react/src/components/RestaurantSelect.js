import React from "react";
import PropTypes from "prop-types";
import MenuItem from "@material-ui/core/MenuItem";
import FormHelperText from "@material-ui/core/FormHelperText";
import FormControl from "@material-ui/core/FormControl";
import Select from "@material-ui/core/Select";
import Input from "@material-ui/core/Input";
import { withStyles } from "@material-ui/core/styles";
import { Query } from "react-apollo";
import gql from "graphql-tag";

const styles = {
  root: { margin: "0.25em 1em" }
};

const GET_RESTAURANTS = gql`
  {
    allRestaurants {
      edges {
        node {
          id
          name
        }
      }
    }
  }
`;

const restoList = [
  {
    id: -1,
    name: "Test 1"
  },
  {
    id: -2,
    name: "Test 2"
  }
];

const RestaurantSelect = ({ classes, value, handleChange }) => (
  <Query query={GET_RESTAURANTS}>
    {({ loading, error, data }) => (
      <Select className={classes.root} value={value} onChange={handleChange}>
        <MenuItem value="">
          <em>None</em>
        </MenuItem>
        {loading || error ? (
          <MenuItem value="">{error ? error.message : "Loading"}</MenuItem>
        ) : (
          data.allRestaurants.edges.map(({ node: { id, name } }) => (
            <MenuItem key={id} value={id}>
              {name}
            </MenuItem>
          ))
        )}
      </Select>
    )}
  </Query>
);

export default withStyles(styles)(RestaurantSelect);
