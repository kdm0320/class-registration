const btnContentInfo = document.querySelector(".content_index_info");
const btnContentList = document.querySelector(".content_index_list");
const btnContentSchedule = document.querySelector(".content_index_schedule");

const contentBasketInfo = document.querySelector(".content_basket_info");
const contentBaskteList = document.querySelector(".content_basket_list");
const contentBaskteSchedule = document.querySelector(
  ".content_basket_schedule"
);

let isShow = true;

const infoToggle = function () {
  if (contentBasketInfo.style.display === "none") {
    if (isShow === false && contentBasketInfo.style.display === "none")
      isShow = true;
    contentBasketInfo.style.display = isShow ? "block" : "none";
    contentBaskteSchedule.style.display = "none";
    contentBaskteList.style.display = "none";
    isShow = !isShow;
    // 수강신청 안내 페이지가 표시되지 않았을 때 클릭 시 수강신청 안내 페이지를 표시함
  }
};

const listToggle = function () {
  if (
    contentBasketInfo.style.display === "none" &&
    contentBaskteList.style.display === "block"
  ) {
    isShow = true;
    contentBasketInfo.style.display = isShow ? "block" : "none";
    contentBaskteSchedule.style.display = "none";
    contentBaskteList.style.display = "none";
    isShow = !isShow;
    // 장바구니 목록이 보인 상태에서 클릭 시 수강신청 안내창이 보이도록 설정
  } else {
    if (isShow === false && contentBaskteList.style.display === "none")
      isShow = true;
    contentBaskteList.style.display = isShow ? "block" : "none";
    contentBaskteSchedule.style.display = "none";
    contentBasketInfo.style.display = "none";
    isShow = !isShow;
    // 수강신청 및 장바구니 시간표가 보인 상태라면 장바구니 목록을 보이도록 설정
  }
};

const scheduleToggle = function () {
  if (
    contentBasketInfo.style.display === "none" &&
    contentBaskteSchedule.style.display === "block"
  ) {
    isShow = true;
    contentBasketInfo.style.display = isShow ? "block" : "none";
    contentBaskteSchedule.style.display = "none";
    contentBaskteList.style.display = "none";
    isShow = !isShow;
    // 장바구니 시간표가 보인 상태에서 클릭 시 수강신청 안내창이 보이도록 설정
  } else {
    if (isShow === false && contentBaskteSchedule.style.display === "none")
      isShow = true;
    contentBaskteSchedule.style.display = isShow ? "block" : "none";
    contentBaskteList.style.display = "none";
    contentBasketInfo.style.display = "none";
    isShow = !isShow;
    // 수강신청 및 장바구니 목록이 보인 상태라면 시간표를 보이도록 설정.
  }
};

btnContentInfo.onclick = infoToggle;
btnContentList.onclick = listToggle;
btnContentSchedule.onclick = scheduleToggle;
