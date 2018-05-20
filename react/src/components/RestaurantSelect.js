import React from "react";
import PropTypes from "prop-types";
import MenuItem from "@material-ui/core/MenuItem";
import FormHelperText from "@material-ui/core/FormHelperText";
import FormControl from "@material-ui/core/FormControl";
import Select from "@material-ui/core/Select";
import Input from "@material-ui/core/Input";
import { withStyles } from "@material-ui/core/styles";

const styles = {
  root: { margin: "0.25em 1em" }
};

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
  <Select className={classes.root} value={value} onChange={handleChange}>
    <MenuItem value="">
      <em>None</em>
    </MenuItem>
    {restoList.map(({ id, name }) => (
      <MenuItem key={id} value={id}>
        {name}
      </MenuItem>
    ))}
  </Select>
);

export default withStyles(styles)(RestaurantSelect);
