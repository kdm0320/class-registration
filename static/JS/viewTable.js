const classData = document.querySelector("#class_datas").textContent;
const dataObj = JSON.parse(classData);
const target = document.querySelector("#target_tbody");
const formAction = [];

for (let clazz in dataObj) {
    let classTr = document.createElement("tr");
    let formTag = document.createElement("form");
    let button = document.createElement("button");
    let buttonName = document.createTextNode("장바구니");
    let formText = document.createTextNode("{% csrf_token %}");
    formTag.appendChild(formText);
    let datas = dataObj[clazz];
    formTag.action = "#"
    formTag.method = "POST";

    button.appendChild(buttonName);
    classTr.appendChild(button)
    for (let data in datas) {
        let targetData = datas[data];
        let classTd = document.createElement("td");
        let tdText = document.createTextNode(targetData);
        if (data == "pk") {
            classTd.className = "hidden";
        }
        else{
        classTd.appendChild(tdText);
        classTr.appendChild(classTd);
        }
    }
    //formTag.appendChild(classTr)
    classTr.appendChild(formTag)
    target.appendChild(classTr);
    //target.appendChild(formTag)
}