import React from "react";
import PropTypes from "prop-types";
import { withStyles } from "@material-ui/core/styles";
import { Link } from "react-router-dom";
import List from "@material-ui/core/List";
import ListItem from "@material-ui/core/ListItem";
import Divider from "@material-ui/core/Divider";
import InboxIcon from "@material-ui/icons/Inbox";
import { isFinite } from "lodash";
import RestaurantSelect from "../RestaurantSelect";

import MenuLink from "./MenuLink";

const styles = theme => ({
  toolbar: theme.mixins.toolbar
});

const DrawerMenuContent = ({
  classes,
  restaurantId,
  handleRestaurantChange
}) => (
  <React.Fragment>
    <div className={classes.toolbar} />
    <Divider />
    <List component="nav">
      <MenuLink to="/" title="Home" />
      <MenuLink to="/restaurant-manager" title="Restaurant Manager" />
    </List>
    <Divider />
    <RestaurantSelect
      value={restaurantId}
      handleChange={handleRestaurantChange}
    />
    <Divider />
    {isFinite(restaurantId) && (
      <List component="nav">
        <MenuLink
          to={`/${restaurantId}/restaurant-overview`}
          title="Restaurant Overview"
        />
        <MenuLink
          to={`/${restaurantId}/attendance-manager`}
          title="Attendance Manager"
        />
        <MenuLink
          to={`/${restaurantId}/period-manager`}
          title="Period Manager"
        />
      </List>
    )}
  </React.Fragment>
);

DrawerMenuContent.propTypes = {
  classes: PropTypes.object.isRequired,
  restaurantId: PropTypes.oneOfType([PropTypes.number, PropTypes.oneOf([""])])
    .isRequired,
  handleRestaurantChange: PropTypes.func.isRequired
};

export default withStyles(styles)(DrawerMenuContent);
