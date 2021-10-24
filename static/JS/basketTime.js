const timeDatas = document.querySelector("#basket_datas").textContent;
const timeDatasObj = JSON.parse(timeDatas);
function showRandom() {
    const rand = Math.floor(Math.random() * 10);
    return rand;
}
const color = ['blueviolet','magenta','lime','yellow','teal','orange','cyan','tomato','seagreen','palevioletred']

function getPeriodTd(subjectName,target) {
    let values = Object.values(target);
    let day
    let time
    let table = document.querySelector("#time_table")
    let qdata
    let targetTds
    let backgColor = color[showRandom()]
    for (let i in values) {
        if (values[i] != 'period') {
            day = values[i].lectureDay;
            time = values[i].lectureTime;
            for (let j in time) {
                switch (time[j]) {
                    case '0':
                        
                        qdata = "zero_periods"
                        targetTds = table.querySelectorAll(`.${day}.${qdata}`)
                        for (let k = 0; k < targetTds.length; k++) {
                            let targetTd = targetTds[k]
                            targetTd.style.background = backgColor
                            if (k == 1) {
                                targetTd.innerText = subjectName
                            }
                        }
                        break;
                    case '1':
                        
                        qdata = "first_periods"
                        targetTds = table.querySelectorAll(`.${day}.${qdata}`)
                        for (let k = 0; k < targetTds.length; k++) {
                            let targetTd = targetTds[k]
                            targetTd.style.background = backgColor
                            if (k == 1) {
                                targetTd.innerText = subjectName
                            }
                        }
                        break;
                    case '2':
                        
                        qdata = "second_periods"
                        targetTds = table.querySelectorAll(`.${day}.${qdata}`)
                        for (let k = 0; k < targetTds.length; k++) {
                            let targetTd = targetTds[k]
                           targetTd.style.background = backgColor
                            if (k == 1) {
                                targetTd.innerText = subjectName
                            }
                        }
                        break;
                    case '3':
                        
                        qdata = "third_periods"
                        targetTds = table.querySelectorAll(`.${day}.${qdata}`)
                        for (let k = 0; k < targetTds.length; k++) {
                            let targetTd = targetTds[k]
                           targetTd.style.background = backgColor
                            if (k == 1) {
                                targetTd.innerText = subjectName
                            }
                        }
                        break;
                    case '4':
                        
                        qdata = "fourth_periods"
                        targetTds = table.querySelectorAll(`.${day}.${qdata}`)
                        for (let k = 0; k < targetTds.length; k++) {
                            let targetTd = targetTds[k]
                           targetTd.style.background = backgColor
                            if (k == 1) {
                                targetTd.innerText = subjectName
                            }
                        }
                        break;
                    case '5':
                        
                        qdata = "fifth_periods"
                        targetTds = table.querySelectorAll(`.${day}.${qdata}`)
                        for (let k = 0; k < targetTds.length; k++) {
                            let targetTd = targetTds[k]
                           targetTd.style.background = backgColor
                            if (k == 1) {
                                targetTd.innerText = subjectName
                            }
                        }
                        break;
                    case '6':
                        
                        qdata = "sixth_periods"
                        targetTds = table.querySelectorAll(`.${day}.${qdata}`)
                        for (let k = 0; k < targetTds.length; k++) {
                            let targetTd = targetTds[k]
                           targetTd.style.background = backgColor
                            if (k == 1) {
                                targetTd.innerText = subjectName
                            }
                        }
                        break;
                    case '7':
                        
                        qdata = "seventh_periods"
                        targetTds = table.querySelectorAll(`.${day}.${qdata}`)
                        for (let k = 0; k < targetTds.length; k++) {
                            let targetTd = targetTds[k]
                           targetTd.style.background = backgColor
                            if (k == 1) {
                                targetTd.innerText = subjectName
                            }
                        }
                        break;
                    case '8':
                        
                        qdata = "eight_periods"
                        targetTds = table.querySelectorAll(`.${day}.${qdata}`)
                        for (let k = 0; k < targetTds.length; k++) {
                            let targetTd = targetTds[k]
                           targetTd.style.background = backgColor
                            if (k == 1) {
                                targetTd.innerText = subjectName
                            }
                        }
                        break;
                    case '9':
                        
                        qdata = "ninth_periods"
                        targetTds = table.querySelectorAll(`.${day}.${qdata}`)
                        for (let k = 0; k < targetTds.length; k++) {
                            let targetTd = targetTds[k]
                           targetTd.style.background = backgColor
                            if (k == 1) {
                                targetTd.innerText = subjectName
                            }
                        }
                        break;
                    case '10':
                        
                        qdata = "tenth_periods"
                        targetTds = table.querySelectorAll(`.${day}.${qdata}`)
                        for (let k = 0; k < targetTds.length; k++) {
                            let targetTd = targetTds[k]
                           targetTd.style.background = backgColor
                            if (k == 1) {
                                targetTd.innerText = subjectName
                            }
                        }
                        break;
                    case '11':
                        
                        qdata = "eleventh_periods"
                        targetTds = table.querySelectorAll(`.${day}.${qdata}`)
                        for (let k = 0; k < targetTds.length; k++) {
                            let targetTd = targetTds[k]
                           targetTd.style.background = backgColor
                            if (k == 1) {
                                targetTd.innerText = subjectName
                            }
                        }
                        break;
                    case '12':
                        
                        qdata = "twelfth_periods"
                        targetTds = table.querySelectorAll(`.${day}.${qdata}`)
                        for (let k = 0; k < targetTds.length; k++) {
                            let targetTd = targetTds[k]
                           targetTd.style.background = backgColor
                            if (k == 1) {
                                targetTd.innerText = subjectName
                            }
                        }
                        break;
                    case '13':
                        
                        qdata = "thirteenth_periods"
                        targetTds = table.querySelectorAll(`.${day}.${qdata}`)
                        for (let k = 0; k < targetTds.length; k++) {
                            let targetTd = targetTds[k]
                           targetTd.style.background = backgColor
                            if (k == 1) {
                                targetTd.innerText = subjectName
                            }
                        }
                        break;
                    case '14':
                        
                        qdata = "fourteenth_periods"
                        targetTds = table.querySelectorAll(`.${day}.${qdata}`)
                        for (let k = 0; k < targetTds.length; k++) {
                            let targetTd = targetTds[k]
                           targetTd.style.background = backgColor
                            if (k == 1) {
                                targetTd.innerText = subjectName
                            }
                        }
                        break;
                    case '15':
                        
                        qdata = "fifteenth_periods"
                        targetTds = table.querySelectorAll(`.${day}.${qdata}`)
                        for (let k = 0; k < targetTds.length; k++) {
                            let targetTd = targetTds[k]
                           targetTd.style.background = backgColor
                            if (k == 1) {
                                targetTd.innerText = subjectName
                            }
                        }
                        break;
                    default:
                        break;
                }
            }
        }
    }


}

function getTimeTd(subjectName,target) {
    let values = Object.values(target);
    let day
    let time
    let table = document.querySelector("#time_table")
    let qdata
    let targetTds
    let backgColor = color[showRandom()]
    for (let i in values) {
        if (values[i] != 'time') {
            day = values[i].lectureDay;
            time = values[i].lectureTime;
            switch (time) {
                case '09:00':
                    
                    qdata = "Aline"
                    targetTds = table.querySelectorAll(`.${day}.${qdata}`)
                    for (let k = 0; k < targetTds.length; k++) {
                        let targetTd = targetTds[k]
                       targetTd.style.background = backgColor
                        if (k == 1) {
                            targetTd.innerText = subjectName
                        }
                    }
                    break;
                case '10:30':
                    
                    qdata = "Bline"
                    targetTds = table.querySelectorAll(`.${day}.${qdata}`)
                    for (let k = 0; k < targetTds.length; k++) {
                        let targetTd = targetTds[k]
                       targetTd.style.background = backgColor
                        if (k == 1) {
                            targetTd.innerText = subjectName
                        }
                    }
                    break;
                case '12:00':
                    
                    qdata = "Cline"
                    targetTds = table.querySelectorAll(`.${day}.${qdata}`)
                    for (let k = 0; k < targetTds.length; k++) {
                        let targetTd = targetTds[k]
                       targetTd.style.background = backgColor
                        if (k == 1) {
                            targetTd.innerText = subjectName
                        }
                    }
                    break;
                case '13:30':
                    
                    qdata = "Dline"
                    targetTds = table.querySelectorAll(`.${day}.${qdata}`)
                    for (let k = 0; k < targetTds.length; k++) {
                        let targetTd = targetTds[k]
                       targetTd.style.background = backgColor
                        if (k == 1) {
                            targetTd.innerText = subjectName
                        }
                    }
                    break;
                case '15:00':
                    
                    qdata = "Eline"
                    targetTds = table.querySelectorAll(`.${day}.${qdata}`)
                    for (let k = 0; k < targetTds.length; k++) {
                        let targetTd = targetTds[k]
                       targetTd.style.background = backgColor
                        if (k == 1) {
                            targetTd.innerText = subjectName
                        }
                    }
                    break;
                case '16:30':
                    
                    qdata = "Fline"
                    targetTds = table.querySelectorAll(`.${day}.${qdata}`)
                    for (let k = 0; k < targetTds.length; k++) {
                        let targetTd = targetTds[k]
                       targetTd.style.background = backgColor
                        if (k == 1) {
                            targetTd.innerText = subjectName
                        }
                    }
                break;   
            }       
        }
    }
}

function printSchedule(subjectName,lectures) {
    let type = lectures.lectureTypes;
    switch (type) {
        case "period":
            getPeriodTd(subjectName,lectures);
            break;
        case 'time':
            getTimeTd(subjectName,lectures);
            break;
        default:
            break;
    }
}

function splitGuy(time) {
    let periods = time.split('(')
    let period = periods[1].split(')')
    let asomeGuy = period[0].split('~')
    return asomeGuy
}

function aimSchedule(day, times) {
    let targetDay
    let periods
    switch (day) {
        case '월':
            targetDay = "mon"
            break
        case '화':
            targetDay = "tue"
            break;
        case '수':
            targetDay = "wed"
            break;
        case '목':
            targetDay = "thi"
            break;
        case '금':
            targetDay = "fri"
            break;
        case '토':
            targetDay = "sat"
            break;
        default:
            targetDay = "error"
            break;
    }
    if (times[0] == '(') {
        periods = splitGuy(times)
        periods = periods[0]
    }
    else {
        periods = times.split(',')
    }
    let lectureObj = {
        lectureTime: periods,
        lectureDay: targetDay
    }
    
    return lectureObj
}

function getDate(date) {
    let subDates = date.split(' / ')
    let lectures = {}
    let types
    for (let days in subDates) {
        let subDate = subDates[days];
        let day = subDate.substring(0, 1);
        let lectureTime = subDate.substring(1);
        let lecture = aimSchedule(day, lectureTime);
        if (Array.isArray(lecture.lectureTime)) {
            types = "period"
        }
        else {
            types = "time"
        }
        lectures[`lecture${days}`] = lecture;
        lectures['lectureTypes'] = types
    }
    return lectures
}

for (let timeObj in timeDatasObj){
    let taskObj = timeDatasObj[timeObj];
    let taskTime = taskObj.time;
    let taskSubject = taskObj.subject_name;
    let lectures = getDate(taskTime);
    printSchedule(taskSubject,lectures)
}