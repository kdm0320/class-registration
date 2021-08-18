const btnBasketContentInfo = document.querySelector(".content_index_info");
const btnBasketContentList = document.querySelector(".content_index_list");
const btnBasketContentSchedule = document.querySelector(
  ".content_index_schedule"
);

const contentBasketInfo = document.querySelector(".content_basket_info");
const contentBaskteList = document.querySelector(".content_basket_list");
const contentBaskteSchedule = document.querySelector(
  ".content_basket_schedule"
);

let isBasketShow = true;

const basketInfoToggle = function () {
  if (contentBasketInfo.style.display === "none") {
    if (isBasketShow === false && contentBasketInfo.style.display === "none")
      isBasketShow = true;
    contentBasketInfo.style.display = isBasketShow ? "block" : "none";
    contentBaskteSchedule.style.display = "none";
    contentBaskteList.style.display = "none";
    isBasketShow = !isBasketShow;
    // 수강신청 안내 페이지가 표시되지 않았을 때 클릭 시 수강신청 안내 페이지를 표시함
  }
};

const basketlistToggle = function () {
  if (
    contentBasketInfo.style.display === "none" &&
    contentBaskteList.style.display === "block"
  ) {
    isBasketShow = true;
    contentBasketInfo.style.display = isBasketShow ? "block" : "none";
    contentBaskteSchedule.style.display = "none";
    contentBaskteList.style.display = "none";
    isBasketShow = !isBasketShow;
    // 장바구니 목록이 보인 상태에서 클릭 시 수강신청 안내창이 보이도록 설정
  } else {
    if (isBasketShow === false && contentBaskteList.style.display === "none")
      isBasketShow = true;
    contentBaskteList.style.display = isBasketShow ? "block" : "none";
    contentBaskteSchedule.style.display = "none";
    contentBasketInfo.style.display = "none";
    isBasketShow = !isBasketShow;
    // 수강신청 및 장바구니 시간표가 보인 상태라면 장바구니 목록을 보이도록 설정
  }
};

const basketScheduleToggle = function () {
  if (
    contentBasketInfo.style.display === "none" &&
    contentBaskteSchedule.style.display === "block"
  ) {
    isBasketShow = true;
    contentBasketInfo.style.display = isBasketShow ? "block" : "none";
    contentBaskteSchedule.style.display = "none";
    contentBaskteList.style.display = "none";
    isBasketShow = !isBasketShow;
    // 장바구니 시간표가 보인 상태에서 클릭 시 수강신청 안내창이 보이도록 설정
  } else {
    if (
      isBasketShow === false &&
      contentBaskteSchedule.style.display === "none"
    )
      isBasketShow = true;
    contentBaskteSchedule.style.display = isBasketShow ? "block" : "none";
    contentBaskteList.style.display = "none";
    contentBasketInfo.style.display = "none";
    isBasketShow = !isBasketShow;
    // 수강신청 및 장바구니 목록이 보인 상태라면 시간표를 보이도록 설정.
  }
};

btnBasketContentInfo.onclick = basketInfoToggle;
btnBasketContentList.onclick = basketlistToggle;
btnBasketContentSchedule.onclick = basketScheduleToggle;
