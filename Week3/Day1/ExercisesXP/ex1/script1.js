let div1= document.body.firstElementChild;
console.log(div1);
let ul1= document.body.children[1];
let npete=ul1.children[1];
npete.textContent="Richard";
let mname =document.querySelector(".list");
let mname1=mname.firstElementChild;
mname1.textContent="Zhenia";
let myname =document.body.children[2];
console.log(myname);
let myname1=myname.firstElementChild;
myname1.textContent="Zhenia";
let secondUlList = document.getElementsByTagName('ul')[1]
let sarah = secondUlList.getElementsByTagName('li')[1].remove()

