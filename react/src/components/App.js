import React from "react";
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";

import Home from "../screens/Home";
import AttendanceManager from "../screens/AttendanceManager";
import RestaurantManager from "../screens/RestaurantManager";
import RestaurantOverview from "../screens/RestaurantOverview";
import PeriodManager from "../screens/PeriodManager";
import NotFound from "../screens/NotFound";

import Layout from "./Layout";

const App = () => (
  <Router>
    <Layout>
      <Switch>
        <Route path="/" exact component={Home} />
        <Route path="/restaurant-manager" component={RestaurantManager} />

        <Route
          path="/:restaurantId/restaurant-overview"
          component={RestaurantOverview}
        />
        <Route
          path="/:restaurantId/attendance-manager"
          component={AttendanceManager}
        />
        <Route path="/:restaurantId/period-manager" component={PeriodManager} />

        <Route path="*" component={NotFound} />
      </Switch>
    </Layout>
  </Router>
);

export default App;
