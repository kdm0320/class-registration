let trRows = document.querySelectorAll(".notice_content_table_row");
const modalOn = document.querySelector(".modal_open_btn");
const modalOff = document.querySelector(".modal_close_btn");
const modals = document.querySelector(".modal");

function setTrRow(targetRows) {
  targetRows.forEach((targetRow) => {
    targetRow.addEventListener("click", onLinked);
  });
}

function onLinked() {
  const regData = this.querySelector(".hidden").innerText;
  // pk 값에 따른 링크 생성을 위해 해당 값을 읽음.
  console.log("클릭하셨습니다.")
  //window.location.replace(`notice.html?regData=${regData}`);
  // 새로 html 파일 만들면 연결 시켜야 함.
}

modalOn.onclick = () => {
  document.querySelector(".modal").style.display = "flex";
};
modalOff.onclick = () => {
  document.querySelector(".modal").style.display = "none";
};

modals.addEventListener("click", event => {
  const evTarget = event.target
  if (evTarget.classList.contains("modal_layer")) {
    modals.style.display = "none";
  }
})
setTrRow(trRows);

