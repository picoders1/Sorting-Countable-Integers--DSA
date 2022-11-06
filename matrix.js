let elements = [];
let table = `<table>`;
heading = `<tr>`;
let c = [];
let b = [];
let d = [];
let e = [];
let arr = [];
let num = parseInt(prompt("Enter the no. of Array size"));
for (let i = 0; i < num; i++) {
  let val = parseInt(prompt(`Enter ${i + 1}th term`));
  arr.push(val);
}
// for (let i = 0; i < 10; i++) {
//   heading += `<th>${i}</th>`;
//   let val = Math.floor(Math.random() * 1000);
//   arr.push(val);
// }
// console.log(arr.length);
function getTable() {
  heading += `</tr>`;
  table += heading;
  for (let i = 0; i <= arr.length - 1; i++) {
    c[i] = 0;
    b[i] = 0;
  }
  for (let i = 0; i < arr.length - 1; i++) {
    let data = `<tr>`;
    for (let j = i + 1; j < arr.length; j++) {
      if (arr[i] < arr[j]) {
        c[j] = c[j] + 1;
      } else {
        c[i] = c[i] + 1;
      }
    }
    for (let p = 0; p < i; p++) {
      data += `<td></td>`;
    }
    for (let k = i; k < arr.length; k++) {
      data += `<td style="background-color: black !important">${c[k]}</td>`;
    }
    data += `</tr>`;
    table += data;
    data = "";
  }
  let data = `<tr>`;
  for (let i = 0; i < c.length; i++) {
    data += `<td>${c[i]}</td>`;
  }
  data += `</tr>`;
  table += data;
  table += `</table>`;
  // console.log(table);
  return table;
  // document.write(table);
}
const tt = getTable();
// document.getElementById("main").innerHTML = table;
// document.body.innerHTML = table;

// console.log(elements);
beforeSort(arr);
for (let i = 0; i <= arr.length - 1; i++) {
  d[i] = 0;
  e[i] = 0;
}
for (let i = 0; i < arr.length - 1; i++) {
  for (let j = i + 1; j < arr.length; j++) {
    if (arr[i] < arr[j]) {
      d[j] += 1;
    } else {
      d[i] += 1;
    }
  }
}
// console.log(d);
for (let i = 0; i < arr.length; i++) {
  e[d[i]] = arr[i];
}
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

document.write(tt);

afterSort(e);
