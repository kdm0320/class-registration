const regiData = document.querySelector("#regi_data").textContent;
const regiDataObj = JSON.parse(regiData);

const regiTbody = document.querySelector("#target_enrol_table");
const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
const dataArray = ['grade', 'check_major', 'subject_number', 'subject_name', 'credit', 'professor', 'time', 'people'];

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
            default:
                classTd.className = dataArray[arrayIndex];
                classTd.appendChild(tdText);
                classTr.appendChild(classTd);
                arrayIndex += 1;
                break;

        }
    }
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
        )
        
        regiTbody.removeChild(classTr);
    });
}