var currentDateTime = new Date();
var year = currentDateTime.getFullYear();
var month = (currentDateTime.getMonth() + 1);
var date = (currentDateTime.getDate() + 1);

if(date < 10) {
  date = '0' + date;
}
if(month < 10) {
  month = '0' + month;
}

var dateTomorrow = year + "-" + month + "-" + date;
var flyoutElem = document.querySelector("#flyout-date");
var flyinElem = document.querySelector("#flyin-date");

flyoutElem.setAttribute("min", dateTomorrow);

flyoutElem.onchange = function () {
    flyinElem.setAttribute("min", this.value);
}