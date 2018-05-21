import React from "react";
import PropTypes from "prop-types";
import { withStyles } from "@material-ui/core/styles";
import Drawer from "@material-ui/core/Drawer";
import Hidden from "@material-ui/core/Hidden";
import MenuIcon from "@material-ui/icons/Menu";
import { withRouter } from "react-router";
import { ApolloConsumer, Mutation } from "react-apollo";
import DrawerMenuContent from "./MenuContent";
import gql from "graphql-tag";

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
        restaurantId: nextProps.match.params.restaurantId || ""
      };

    return prevState;
  }

  handleRestaurantChange = event => {
    const restaurantId = event.target.value;
    // To test mutation and cache direct write, only one is necessary
    this.setState({ restaurantId });
    /*this.props.apolloCache.writeData({
      data: { currentRestaurantId: restaurantId }
    });*/
    this.props.setCurrentRestaurantId({ variables: { id: restaurantId } });
    if (this.props.match.params.restaurantId) {
      if (restaurantId) {
        this.props.history.push(
          this.props.match.path.replace(":restaurantId", restaurantId)
        );
      } else {
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

const SET_CURRENT_RESTAURANT_ID = gql`
  mutation SetCurrentRestaurantId($id: String) {
    setCurrentRestaurantId(id: $id) @client
  }
`;

// To test mutation and cache direct write, only one is necessary
const withApolloCache = Component => props => (
  <ApolloConsumer>
    {cache => (
      <Mutation mutation={SET_CURRENT_RESTAURANT_ID}>
        {setCurrentRestaurantId => (
          <Component
            {...props}
            apolloCache={cache}
            setCurrentRestaurantId={setCurrentRestaurantId}
          />
        )}
      </Mutation>
    )}
  </ApolloConsumer>
);
export default withRouter(
  withApolloCache(withStyles(styles, { withTheme: true })(DrawerMenu))
);
