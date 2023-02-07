// setTimeout(sayHi,2000)
// function sayHi(){
//     alert("Hello World")
// }

// setTimeout(newP,2000)
// function newP(){
//     const para=document.createElement("p");
//     const text=document.createTextNode("Hello World");
//     const div1=document.body.querySelector("#container");
//     para.appendChild(text);
//     div1.appendChild(para);
// }

const int=setInterval(newP1,2000)
let raz=5
function newP1(){
    const para=document.createElement("p");
    const text=document.createTextNode("Hello World");
    const div1=document.body.querySelector("#container");
    para.appendChild(text);
    div1.appendChild(para);
    raz--
    if(raz>0){
    }else{
        clearInterval(int)
    }
}

const btn=document.querySelector("#clear")
btn.addEventListener("click",end)
function end(){
    clearInterval(int)
}