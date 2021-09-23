function selectedOption(e) {
  const business = { economics: "경제학과" };
  const engineering = { electronic: "전자공학과" };
  const software = { software: "소프트웨어학과" };
  // 원하는 대학에 따른 학과를 위의 예시처럼 객체로 생성해야함. {서버에 보내질 이름 : 표시될 이름}

  const target = document.getElementById("college");
  let index = 0;
  let opt;
  let loop;

  if (this.value == "business") loop = business;
  else if (this.value == "engineering") loop = engineering;
  else if (this.value == "software") loop = software;

  target.options.length = 1;

  for (index in loop) {
    opt = document.createElement("option");
    opt.value = index;
    opt.innerHTML = loop[index];
    target.appendChild(opt);
  }
}

const subject = document.querySelector("#subject");
subject.onchange = selectedOption;

