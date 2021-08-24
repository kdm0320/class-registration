let trRows = document.querySelectorAll(".notice_content_table_row");
const modalOn = document.querySelector(".modal_open_btn");
const modalOff = document.querySelector(".modal_close_btn");

function setTrRow(targetRows) {
  targetRows.forEach((targetRow) => {
    targetRow.addEventListener("click", onLinked);
  });
}

function onLinked() {
  const regData = this.querySelector(".hidden").innerText;
  window.location.replace(`notice.html?regData=${regData}`);
  // 새로 html 파일 만들면 연결 시켜야 함.
}

modalOn.onclick = () => {
  document.querySelector(".modal").style.display = "flex";
};
modalOff.onclick = () => {
  document.querySelector(".modal").style.display = "none";
};

setTrRow(trRows);
