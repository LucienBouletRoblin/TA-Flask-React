import React from "react";
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";

import AttendanceManager from "../screens/AttendanceManager";
import Home from "../screens/Home";
import NotFound from "../screens/NotFound";
import PeriodManager from "../screens/PeriodManager";
import RestaurantForm from "../screens/RestaurantForm";
import RestaurantManager from "../screens/RestaurantManager";
import RestaurantOverview from "../screens/RestaurantOverview";

import Layout from "./Layout";

// To initialise the currentRestaurantId in apollo clientState from window.location.pathname
export const pathsWithRestaurantId =
  "/:restaurantId/(edit|restaurant-overview|attendance-manager|period-manager)";

const RouteWithLayout = ({ component: Component, ...rest }) => (
  <Route
    {...rest}
    render={matchProps => (
      <Layout>
        <Component {...matchProps} />
      </Layout>
    )}
  />
);
const App = () => (
  <Router>
    <Switch>
      <RouteWithLayout path="/" exact component={Home} />

      <RouteWithLayout
        path="/restaurant-manager"
        component={RestaurantManager}
      />

      <RouteWithLayout path="/new-restaurant" component={RestaurantForm} />

      <RouteWithLayout
        path="/:restaurantId/restaurant-overview"
        exact
        component={RestaurantOverview}
      />
      <RouteWithLayout
        path="/:restaurantId/edit"
        exact
        component={RestaurantForm}
      />

      <RouteWithLayout
        path="/:restaurantId/attendance-manager"
        component={AttendanceManager}
      />
      <RouteWithLayout
        path="/:restaurantId/period-manager"
        component={PeriodManager}
      />

      <RouteWithLayout path="*" component={NotFound} />
    </Switch>
  </Router>
);

export default App;
