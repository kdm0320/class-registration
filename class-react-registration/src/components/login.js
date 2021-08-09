import React, { Component } from "react";

class Login extends Component {
  render() {
    return (
      <main>
        <form
          name="user-data"
          id="login-form"
          action="/registration.html"
          method="GET"
        >
          <div id="login-box">
            <input type="text" name="id" />
            <input type="text" name="password" />
          </div>
          <button>로그인</button>
        </form>
      </main>
    );
  }
}

export default Login;
