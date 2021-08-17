//const contentInfo = document.querySelector("content_index_info");
const btnContentList = document.querySelector(".content_index_list");
const btnContentSchedule = document.querySelector(".content_index_schedule");

const contentBaskteList = document.querySelector(".content_basket_list");
const contentBaskteSchedule = document.querySelector(
  ".content_basket_schedule"
);

const listToggle = (function () {
  let isShow = false;

  return function () {
    contentBaskteList.style.display = isShow ? "block" : "none";
    isShow = !isShow;
  };
})();

const scheduleToggle = (function () {
  let isShow = false;

  return function () {
    contentBaskteSchedule.style.display = isShow ? "block" : "none";
    isShow = !isShow;
  };
})();

btnContentList.onclick = listToggle;
btnContentSchedule.onclick = scheduleToggle;
