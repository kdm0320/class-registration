const eventButton = document.querySelector("#fixing_button");
const fixedInterface = document.querySelector("#notice_detail_fixed_button_interface");
const cancleFixed = fixedInterface.querySelector("#cancle_button");
const showedMaster = document.querySelector("#only_showed_notice_master");
const detailWriter = document.querySelector("#detail_writer");
const logedinUser = document.querySelector("#target_data");
const mainSection = document.querySelector(".detail_main_content");
const writer = detailWriter.textContent;
const target = logedinUser.textContent;

fixedInterface.style.display = "none";
showedMaster.style.display = "none";

if ( writer == target) {
    showedMaster.style.display = "block";
}


eventButton.addEventListener("click", () => {
    fixedInterface.style.display = "block";
    eventButton.style.display = "none";
    mainSection.style.display = "none";
})

cancleFixed.addEventListener("click", () => {
    fixedInterface.style.display = "none";
    eventButton.style.display = "block";
    mainSection.style.display = "block";

})