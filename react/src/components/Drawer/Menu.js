import React from "react";
import PropTypes from "prop-types";
import { withStyles } from "@material-ui/core/styles";
import Drawer from "@material-ui/core/Drawer";
import Hidden from "@material-ui/core/Hidden";
import MenuIcon from "@material-ui/icons/Menu";
import { withRouter } from "react-router";
import { isFinite } from "lodash";

import DrawerMenuContent from "./MenuContent";

export const drawerWidth = 240;

const styles = theme => ({
  drawerPaper: {
    width: drawerWidth,
    [theme.breakpoints.up("md")]: {
      position: "relative"
    }
  }
});

class DrawerMenu extends React.Component {
  constructor(props) {
    super(props);
    this.state = DrawerMenu.getDerivedStateFromProps(props); // initialised with getDerivedStateFromProps
  }

  static getDerivedStateFromProps(nextProps, prevState) {
    if (
      !prevState ||
      (nextProps.match.restaurantId &&
        nextProps.match.restaurantId !== prevState.restaurantId)
    )
      return {
        restaurantId: parseInt(nextProps.match.params.restaurantId) || ""
      };
    else return prevState;
  }

  handleRestaurantChange = event => {
    const restaurantId = event.target.value;
    if (isFinite(restaurantId)) {
      this.setState({ restaurantId });
      if (parseInt(this.props.match.params.restaurantId)) {
        this.props.history.push(
          this.props.match.path.replace(":restaurantId", restaurantId)
        );
      }
    } else {
      this.setState({ restaurantId: "" });
      if (parseInt(this.props.match.params.restaurantId)) {
        this.props.history.push("/");
      }
    }
  };

  render() {
    const { mobileOpen, classes, theme, handleDrawerToggle } = this.props;
    return (
      <React.Fragment>
        <Hidden mdUp>
          <Drawer
            variant="temporary"
            anchor={theme.direction === "rtl" ? "right" : "left"}
            open={mobileOpen}
            onClose={handleDrawerToggle}
            classes={{
              paper: classes.drawerPaper
            }}
            ModalProps={{
              keepMounted: true // Better open performance on mobile.
            }}
          >
            <DrawerMenuContent
              restaurantId={this.state.restaurantId}
              handleRestaurantChange={this.handleRestaurantChange}
            />
          </Drawer>
        </Hidden>
        <Hidden smDown implementation="css">
          <Drawer
            variant="permanent"
            open
            classes={{
              paper: classes.drawerPaper
            }}
          >
            <DrawerMenuContent
              restaurantId={this.state.restaurantId}
              handleRestaurantChange={this.handleRestaurantChange}
            />
          </Drawer>
        </Hidden>
      </React.Fragment>
    );
  }
}

DrawerMenu.propTypes = {
  classes: PropTypes.object.isRequired,
  theme: PropTypes.object.isRequired,
  mobileOpen: PropTypes.bool.isRequired,
  handleDrawerToggle: PropTypes.func.isRequired
};

export default withRouter(withStyles(styles, { withTheme: true })(DrawerMenu));
