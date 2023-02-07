// function sayHello(){
//     alert("Hello")
// }
// setTimeout(sayHello,2000)//функция через 2 секунды



const ten=setInterval(saySale,1000)
let raz=10
function saySale(){
    const ban=document.createElement("div");
    const content=document.createTextNode(`The sales end in ${raz}sec!`);
    // const content.textContent=`The sales end in ${raz}sec!`
    const body1=document.body;
    ban.appendChild(content);
    body1.appendChild(ban);
    raz--;
    if(raz>0){
    }else{
        clearInterval(ten)
    }

}


// const id=setInterval(sayHello,1000)
//  function sayHello(){
//     console.log("Hello");
//     clearInterval(id)
//  }