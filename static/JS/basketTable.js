const basketData = document.querySelector("#basket_datas").textContent;
const basketDataObj = JSON.parse(basketData);

const basketTbody = document.querySelector("#target_basket_table");
const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
const dataArray = ['grade','check_major','subject_number','subject_name','credit','professor','time','people'];
const tr = basketTbody.getElementsByTagName("tr")


/*function loadHead() {
    const tr = document.querySelector("#target_basket_table").querySelectorAll("tr")
    const creBox = document.querySelector(".button_bottom_left_text_credit");
    const couBox = document.querySelector(".button_bottom_left_text_classNum");
    const countCredit = document.querySelectorAll(".credit");
    let cre = 0
    for (let i=0; i < countCredit.length; i++) {
        let temp = countCredit[i].innerText;
        cre += parseInt(temp)
    }
    let count = tr.length;
    couBox.innerText = count;
    creBox.innerText = cre;
}*/

function loadCredits(updatedCredit) {
    const creBox = document.querySelector(".button_bottom_left_text_credit");
    let parseCredit = parseFloat(updatedCredit);
    console.log(parseCredit.toString())
    creBox.innerText = parseCredit.toString();
    console.log(tr)
    count = tr.length;
    couBox.innerText = count;
}



for (let clazz in basketDataObj) {
    let classTr = document.createElement("tr");
    let button = document.createElement("button");
    let buttonName = document.createTextNode("수강신청");
    let deleteButtonText = document.createTextNode("삭제");
    let deleteButton = document.createElement("button");
    let datas = basketDataObj[clazz];
    let arrayIndex = 0;

    button.className = "btnAjax";
    deleteButton.appendChild(deleteButtonText);
    button.appendChild(buttonName);
    classTr.appendChild(button)
    classTr.appendChild(deleteButton);
    for (let data in datas) {
        let targetData = datas[data];
        let classTd = document.createElement("td");
        let tdText = document.createTextNode(targetData);
        switch (data) {
            case 'id':
                classTd.className = "hidden";
                classTd.appendChild(tdText);
                classTr.appendChild(classTd);
                break;
            case 'universe':
                break;
            case 'department':
                break;
            /*case 'subject_name':
                classTd.className = dataArray[arrayIndex];
                classTd.appendChild(tdText);
                classTd.addEventListener('click', e => {
                    window.open(`../static/pdf/lecture${datas['id']}.pdf`,`${data}`,"width=800, height=700"
                    );
                })
                classTr.appendChild(classTd);
                arrayIndex += 1;
                break;*/
            default:
                classTd.className = dataArray[arrayIndex];
                classTd.appendChild(tdText);
                classTr.appendChild(classTd);
                arrayIndex += 1;
                break;

        }
    }
    basketTbody.appendChild(classTr);

    deleteButton.addEventListener('click', e => {
        const reqUrl = new Request("/basket/delete", { headers: { 'X-CSRFToken': csrftoken } })
        let id = classTr.querySelector('.hidden').innerText;
        let grade = classTr.querySelector('.grade').innerText;
        let check_major = classTr.querySelector('.check_major').innerText;
        let subject_number = classTr.querySelector('.subject_number').innerText;
        let subject_name = classTr.querySelector('.subject_name').innerText;
        let credit = classTr.querySelector('.credit').innerText;
        let time = classTr.querySelector('.time').innerText
        let professor = classTr.querySelector('.professor').innerText;
        let people = classTr.querySelector('.people').innerText;
        let param = {
            'id': id,
            'grade': grade,
            'check_major': check_major,
            'subject_number': subject_number,
            'subject_name': subject_name,
            'credit': credit,
            'professor': professor,
            'time': time,
            'people': people,
        }
        
        fetch(reqUrl, {
            body: JSON.stringify(param),
            method: "POST",
            mode: 'same-origin'
        }
        ).then(function (res) {
            return res.text();
        }, function (error) {
            console.log(error);
        }).then(function (data) {
            let message = JSON.parse(data)  
            loadCredits(message.credit)
            //basketTbody.removeChild(classTr);
            
        });
        basketTbody.removeChild(classTr);
    }
  
    );

    button.addEventListener('click', e => {
        let id = classTr.querySelector('.hidden').innerText;
        let grade = classTr.querySelector('.grade').innerText;
        let check_major = classTr.querySelector('.check_major').innerText;
        let subject_number = classTr.querySelector('.subject_number').innerText;
        let subject_name = classTr.querySelector('.subject_name').innerText;
        let credit = classTr.querySelector('.credit').innerText;
        let time = classTr.querySelector('.time').innerText
        let professor = classTr.querySelector('.professor').innerText;
        let people = classTr.querySelector('.people').innerText;
        let param = {
            'id': id,
            'grade': grade,
            'check_major': check_major,
            'subject_number': subject_number,
            'subject_name': subject_name,
            'credit': credit,
            'professor': professor,
            'time': time,
            'people': people,
        }

        
        const reqUrl = new Request("/basket/registration", { headers: { 'X-CSRFToken': csrftoken } })
        fetch(reqUrl, {
            method: "POST",
            body: JSON.stringify(param),
            mode: 'same-origin'
        }
        ).then(function (res) {
            return res.text()
        }, function (error) {
            console.log(error)
        }
        ).then(data => {
            let message = JSON.parse(data)
            if (message.messages != "nothing") {
                alert(message.messages)
            }
            else {
                basketTbody.removeChild(classTr);
                loadCredits(message.credits)
            }
        }, function (error) {
            console.log(error)
        })
    });
}
const couBox = document.querySelector(".button_bottom_left_text_classNum");
let count = tr.length;
couBox.innerText = count;
