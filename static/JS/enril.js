const btnEnrolContentInfo = document.querySelector(".content_index_info");
const btnEnrolContentCancleList = document.querySelector(
  ".content_index_info_cancle_list"
);

const contentEnrolInfo = document.querySelector(".content_enrol_info");
const conentEnrolCancleList = document.querySelector(
  ".content_enrol_cancleList"
);

let isEnrolShow = true;

const enrolInfoToggle = function () {
  if (contentEnrolInfo.style.display === "none") {
    if (isEnrolShow === false && contentEnrolInfo.style.display === "none")
      isEnrolShow = true;
    contentEnrolInfo.style.display = isEnrolShow ? "block" : "none";
    conentEnrolCancleList.style.display = "none";
    isEnrolShow = !isEnrolShow;
    // 수강신청 안내 페이지가 표시되지 않았을 때 클릭 시 수강신청 안내 페이지를 표시함
  }
};

const enrolCancleListToggle = function () {
  if (
    contentEnrolInfo.style.display === "none" &&
    conentEnrolCancleList.style.display === "block"
  ) {
    isEnrolShow = true;
    contentEnrolInfo.style.display = isEnrolShow ? "block" : "none";
    conentEnrolCancleList.style.display = "none";
    isEnrolShow = !isEnrolShow;
    // 장바구니 목록이 보인 상태에서 클릭 시 수강신청 안내창이 보이도록 설정
  } else {
    if (isEnrolShow === false && conentEnrolCancleList.style.display === "none")
      isEnrolShow = true;
    conentEnrolCancleList.style.display = isEnrolShow ? "block" : "none";
    contentEnrolInfo.style.display = "none";
    isEnrolShow = !isEnrolShow;
    // 수강신청 및 장바구니 시간표가 보인 상태라면 장바구니 목록을 보이도록 설정
  }
};

btnEnrolContentInfo.onclick = enrolInfoToggle;
btnEnrolContentCancleList.onclick = enrolCancleListToggle;
