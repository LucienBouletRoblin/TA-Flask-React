import React from "react";
import { Link } from "react-router-dom";

const RestaurantManager = () => (
  <div>
    <h3>This is RestaurantManager</h3>
    <Link to="/new-restaurant">New restaurant</Link>
  </div>
);

export default RestaurantManager;
