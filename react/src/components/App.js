import React from "react";
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";

import Home from "../screens/Home";
import AttendanceManager from "../screens/AttendanceManager";
import RestaurantManager from "../screens/RestaurantManager";
import RestaurantOverview from "../screens/RestaurantOverview";
import PeriodManager from "../screens/PeriodManager";
import NotFound from "../screens/NotFound";

import Layout from "./Layout";

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

      <RouteWithLayout
        path="/:restaurantId/restaurant-overview"
        component={RestaurantOverview}
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
