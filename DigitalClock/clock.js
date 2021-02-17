getTime = document.querySelector("#time");

getDate = document.querySelector("#date");

getTimeZone = document.querySelector('#tzone');


function timer() {
    d = new Date();
    hr = d.getHours();
    min = d.getMinutes();
    sec = d.getSeconds();
    date = d.getDate();
    month = d.getMonth();
    year = d.getFullYear(); 
    if (hr < 10) {
        hr = "0" + hr;
    }
    if (min < 10) {
        min = "0" + min;
    }
    if (sec < 10) {
        sec = "0" + sec;
    }
    if (date < 10) {
        date = "0" + date;
    }
    monthName = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    month = monthName[month]
    getTime.innerHTML = `${hr}:${min}:${sec}`;
    getDate.innerHTML = `${date} ${month} ${year}` 
    
    getTimeZone.innerHTML = "GMT+" + timeZone();

}


setInterval(timer, 1000);

function timeZone() {
    var y = d.getTimezoneOffset();
    var time = Math.floor(y / (-60));
    if (time < 10) {
        time = "0" + time;
    }
    var rem = (y + 60 * time) * (-1);
    return `${time}${rem}`
}




y = timer();








