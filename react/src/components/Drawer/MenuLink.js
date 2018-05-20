import React from "react";
import PropTypes from "prop-types";
import { Link } from "react-router-dom";
import ListItem from "@material-ui/core/ListItem";

const DrawerMenuLink = ({ to, title }) => (
  <ListItem button component={Link} to={to}>
    {title}
  </ListItem>
);

DrawerMenuLink.propTypes = {
  to: PropTypes.string.isRequired,
  title: PropTypes.string.isRequired
};

export default DrawerMenuLink;
