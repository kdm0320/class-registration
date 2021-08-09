import React, { Component } from "react";

import Registration from "./components/regi.js";
import Login from "./components/login.js";

class App extends Component {
  render() {
    return (
      <div>
        <Login></Login>
        <Registration></Registration>
      </div>
    );
  }
}

export default App;
