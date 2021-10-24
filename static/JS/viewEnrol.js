const regiData = document.querySelector("#regi_data").textContent;
const regiDataObj = JSON.parse(regiData);

const regiTbody = document.querySelector("#target_enrol_table");
const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
const dataArray = ['grade', 'check_major', 'subject_number', 'subject_name', 'credit', 'professor', 'time', 'people'];

//const creditBox = document.querySelector(".button_bottom_left_text_credit");
const countBox = document.querySelector(".button_bottom_left_text_classNum");
let count =0
//let credit =0

/*function loadHead() {
    const tr = document.querySelector("#target_enrol_table").querySelectorAll("tr")
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
    let credit = creBox.innerText.replace(/\s/g, "");
    let parseCredit;
    if (updatedCredit != undefined)
        parseCredit = parseFloat(credit) - parseFloat(updatedCredit);
    else
        parseCredit = parseFloat(credit);

    creBox.innerText = parseCredit.toString();

}

for (let clazz in regiDataObj) {
    let classTr = document.createElement("tr");
    let button = document.createElement("button");
    let buttonName = document.createTextNode("수강취소");
    let datas = regiDataObj[clazz];
    let arrayIndex = 0;
    button.className = "btnAjax";
    
    button.appendChild(buttonName);
    classTr.appendChild(button)
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
            case 'credit':
                classTd.className = dataArray[arrayIndex];
                classTd.appendChild(tdText);
                classTr.appendChild(classTd);
                arrayIndex += 1;
                credit += parseInt(datas[data])
                break;
            default:
                classTd.className = dataArray[arrayIndex];
                classTd.appendChild(tdText);
                classTr.appendChild(classTd);
                arrayIndex += 1;
                break;

        }
    }
    count += 1;


    regiTbody.appendChild(classTr);

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
        
        const reqUrl = new Request("/registration/delete", { headers: { 'X-CSRFToken': csrftoken } })
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
            let message = JSON.parse(data);
            console.log(message);
            //loadCredits(message.credits);
        })
        
        regiTbody.removeChild(classTr);
        
        //loadHead()

    });
    
}
//creditBox.innerText = credit;
countBox.innerText = count;