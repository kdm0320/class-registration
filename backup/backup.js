


let btnAjax = document.querySelector('.btnAjax');
btnAjax.addEventListener('click', e => {
  let universe = document.querySelector('.universe').innerText;
  let department = document.querySelector('.department').innerText;
  let grade = document.querySelector('.grade').innerText;
  let check_major = document.querySelector('.check_major').innerText;
  let subject_number = document.querySelector('.subject_number').innerText;
  let subject_name = document.querySelector('.subject_name').innerText;
  let credit = document.querySelector('.credit').innerText;
  let professor = document.querySelector('.professor').innerText;
  let time = document.querySelector('.time').innerText;
  let param = {
    'universe' : universe,
    'department' : department,
    'grade' : grade,
    'check_major' : check_major,
    'subject_number' : subject_number,
    'subject_name' : subject_name,
    'credit' : credit,
    'professor' : professor,
    'time' : time,
    }
    
    $.ajax({
    url: "{% url 'classes:basket' %}",
    type: 'POST',
    headers:{
        'X-CSRFTOKEN' : '{{csrf_token}}'
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
