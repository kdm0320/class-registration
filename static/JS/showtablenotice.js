function inputData(data, tr, pk) {
    let firstChild = document.createElement("td");
    firstChild.className = 'hidden';
    firstChild.textContent = pk
    tr.appendChild(firstChild);
    const datas = [
        data.type,
        data.title,
        data.department,
        data.writer,
        data.created,
        data.post_hit
    ];
    datas.forEach(function (item) {
        let tableCol = document.createElement("td");
        tableCol.textContent = item;
        tr.appendChild(tableCol);
    })
}
// 여러 게시글이 있다면 해당 json 도 비슷하게 올 것. 이때 어떻게 slpit 하는지 잘 생각해야함.
//let placeData = JSON.parse(document.getElementById('jsonData').textContent).split("[")[1].split("]")[0];
let placeData = JSON.parse(document.getElementById('jsonData').textContent).split("[")[1].split("]")[0].split(",");
//let testData = JSON.parse(document.getElementById('jsonData').textContent)
console.log(placeData)

let count = 0;
let index = placeData.length
const loopNum = (index / 9)+1; // 전체 요소 갯수에 비례한 반복 횟수 결정
let targetArray = [];
for (let i = 1; i < loopNum; i++){
    let tempData = [];
    for (let j = 0; j < 9; j++){
        
        tempData.push(placeData[count]);
        count += 1;
    }
    targetArray.push(tempData)
}

targetArray.forEach(function (item,index) {
    let targetitem = JSON.parse(item);
    let contentData = targetitem.fields;
    let pk = targetitem.pk;
    let tbody = document.querySelector(".target_table_body")
    let tableRow = document.createElement("tr");
    tableRow.className = 'notice_content_table_row';
    inputData(contentData,tableRow,pk);
    tbody.appendChild(tableRow);
})

