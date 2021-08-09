import React, { Component } from "react";

class Registration extends Component {
  render() {
    return (
      <div>
        <nav>
          <ul>
            <div>
              <a href="/">수강신청</a>
            </div>
            <div>
              <a href="/">장바구니</a>
            </div>
            <div>
              <a href="/">시간표 조회</a>
            </div>
            <div>
              <a href="/">개인 시간표</a>
            </div>
            <div>
              <a href="/">게시판</a>
            </div>
          </ul>
        </nav>
        <main>
          <header></header>
          <div id="content"></div>
        </main>
      </div>
    );
  }
}

export default Registration;
