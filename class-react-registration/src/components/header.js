import React, { Component } from "react";

class header extends Component {
  render() {
    <div id="main-header">
      <div></div>
      <div></div>
      <div>
        <span>{/**학기정보 **/}</span>
      </div>
      <div>
        {/** 사용자 정보 **/}
        <span></span>
        <span></span>
        <span></span>
        <div></div>
      </div>
      <div>
        <div> {/** 시계 아이콘 **/}</div>
        <span> {/** 30분 타이머 **/}</span>
      </div>
      <div>
        <button>연장하기</button>
      </div>
      <div>
        <button>로그아웃</button>
      </div>
    </div>;
  }
}

export default header;
