const modalOn = document.querySelector(".modal_open_btn");
const modalOff = document.querySelector(".modal_close_btn");
const modals = document.querySelector(".modal");


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


