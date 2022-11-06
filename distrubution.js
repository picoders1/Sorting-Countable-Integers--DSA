//arr=[1,2,3,4,5,1,5,4,3,2,1,4,5,2,1,3,2,1,4,5,2,1,3];
arr = [];
var n = prompt("Enter the Size of the  Array");
var table1 = "<table>";
for (i = 0; i < n; i++) {
  var e = prompt("Enter the " + (i + 1) + " Elements");
  arr.push(e);
  table1 += "<tr><td>A[" + i + "]</td><td>" + e + "</td><tr>";
}
beforeSort(arr);
table1 += "<table>";
document.getElementById("be").innerHTML = table1;
var min = arr[0],
  max = arr[0];
for (item of arr) {
  // find minimum value
  if (item < min) min = item;

  // find maximum value
  if (item > max) max = item;
}
var b = [];
var d = [];
for (i = 0; i < n; i++) {
  b.push(0);
}
for (i = 0; i < max - min + 1; i++) {
  d.push(0);
}
console.log("min = ", min);
console.log("max= ", max);
var j = 0;
var table2 = "<h1> Array Frequency </h1> <br><table> <tr>";
for (i = 0; i < n; i++) {
  j = arr[i] - min;
  d[j] = d[j] + 1;
}
z = d.length;
for (i = 0; i < z; i++) {
  w = parseInt(min) + parseInt(i);
  table2 += "<td>" + w + "</td>";
}
table2 += "</tr><tr>";
for (i = 0; i < z; i++) {
  table2 += "<td>" + d[i] + "</td>";
}
table2 += "</tr></table>";
for (i = 1; i < max - min + 1; i++) {
  d[i] = d[i] + d[i - 1];
}
table3 = "<h3> accumlated frequence </h3> <br> <table><tr>";
for (i = 0; i < z; i++) {
  table3 += "<td>" + i + "</td>";
}

table3 += "<br/> <h3>Distributio</h3>";
table3 += "</tr><tr>";
for (i = 0; i < z; i++) {
  table3 += "<td>" + d[i] + "</td>";
}
table3 += "</tr></table>";
console.log(d);

document.getElementById("be").innerHTML += table2 + table3;
bs = b.length;
table4 = "<h1> Step 2 </h1> <table> <tr>";
table5 = "<table><tr>";
for (i = n - 1; i >= 0; i--) {
  j = arr[i] - min;
  //console.log(j)
  d[j] = d[j] - 1;
  for (k = 0; k < d.length; k++) {
    table5 += "<td>" + d[k] + "</td>";
  }
  table5 += "</tr> <tr>";
  //console.log(d[j])
  b[d[j]] = arr[i];
  for (k = 0; k < n; k++) {
    if (k == d[j]) {
      table4 += "<td>" + b[k] + "</td>";
    } else {
      table4 += "<td>&nbsp</td>";
    }
  }
  table4 += "</tr><tr>";
}

for (i = 0; i < n; i++) {
  table4 += "<td>" + b[i] + "</td>";
}
table5 += "</tr>";
table5 += "</>";
// for (i = 0; i < n; i++) {
//   table5 += "<td>" + d[i] + "</td>";
// }
afterSort(b);

table4 += "</tr></table>";
table5 += "</tr></table>";
console.log(table4);
document.getElementById("be").innerHTML += table5 + table4;
console.log(b);

function beforeSort(elements) {
  let beforeElements = [];
  for (let i = 0; i < elements.length; i++) {
    const div = document.createElement("div");
    div.className = "before";
    div.innerText = elements[i];
    div.style.animationDelay = `${i / 2}s`;
    beforeElements.push(
      document.querySelector(".main-before").appendChild(div)
    );
  }
  // console.log(beforeElements);
}
function afterSort(elements) {
  for (let i = 0; i < elements.length; i++) {
    const div = document.createElement("div");
    div.className = "after";
    div.innerText = elements[i];
    div.style.animationDelay = `${i / 2}s`;
    document.querySelector(".main-after").appendChild(div);
  }
}
