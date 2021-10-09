const classData = document.querySelector("#class_datas").textContent;
const dataObj = JSON.parse(classData);
const target = document.querySelector("#target_tbody");
const formAction = [];

const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;

function makeJquery(){
let script = document.createElement('script');
script.src = 'https://code.jquery.com/jquery-3.4.1.min.js';
script.type = 'text/javascript';
document.getElementsByTagName('head')[0].appendChild(script);
}

const dataArray = ['universe','department','grade','check_major','subject_number','subject_name','credit','professor','time','people'];

makeJquery();

for (let clazz in dataObj) {
    let classTr = document.createElement("tr");
    let formTag = document.createElement("form");
    let button = document.createElement("button");
    let buttonName = document.createTextNode("장바구니");
    let datas = dataObj[clazz];
    let arrayIndex = 0;

    button.className = "btnAjax";
    
    button.appendChild(buttonName);
    classTr.appendChild(button)
    for (let data in datas) {
        let targetData = datas[data];
        let classTd = document.createElement("td");
      let tdText = document.createTextNode(targetData);
      switch (data) {
        case 'pk':
          classTd.className = "hidden";
          classTd.appendChild(tdText);
          classTr.appendChild(classTd);
          break;
        case 'subject_name':
          classTd.className = dataArray[arrayIndex];
          classTd.appendChild(tdText);
          classTd.addEventListener('click', e => {
              window.open(`../../static/pdf/lecture${datas['pk']}.pdf`,`${data}`,"width=800, height=700"
              );
          })
          classTr.appendChild(classTd);
          arrayIndex += 1;
          break;
        default:
          classTd.className = dataArray[arrayIndex];
          classTd.appendChild(tdText);
          classTr.appendChild(classTd);
          arrayIndex += 1;
          break;
      }
    }
    classTr.appendChild(formTag)
    target.appendChild(classTr);

  button.addEventListener('click', e => {
        let universe = classTr.querySelector('.universe').innerText;
        let department = classTr.querySelector('.department').innerText;
        let grade = classTr.querySelector('.grade').innerText;
        let check_major = classTr.querySelector('.check_major').innerText;
        let subject_number = classTr.querySelector('.subject_number').innerText;
        let subject_name = classTr.querySelector('.subject_name').innerText;
        let credit = classTr.querySelector('.credit').innerText;
        let professor = classTr.querySelector('.professor').innerText;
        let time = classTr.querySelector('.time').innerText;
        let people = classTr.querySelector('.people').innerText;
        let param = {
          'universe' : universe,
          'department' : department,
          'grade' : grade,
          'check_major' : check_major,
          'subject_number' : subject_number,
          'subject_name' : subject_name,
          'credit' : credit,
            'professor': professor,
            'time': time,
            'people': people,
          }
        //
        //const reqUrl = new Request(
       //     "http://127.0.0.1:8000/class/regi-basket/",
       //     { headers: { 'X-CSRFToken': csrftoken } }
// )
      //  fetch(reqUrl, {
       //     method: "POST",
//body: JSON.stringify(param),
       //     mode: 'same-origin'
        //}).then(function (res) {
         //   return res.text()
        //}, function (error) {
         //   console.log(error)
        //}
        //)
          
          $.ajax({
          url: "http://127.0.0.1:8000/class/regi-basket/",
          type: 'POST',
          headers:{
              'X-CSRFTOKEN' : csrftoken
          },
          data : JSON.stringify(param),
          success: function(data){
              console.log(data)
          },
          error: function(){
              console.log("전송실패")
          }
        });
      });

}