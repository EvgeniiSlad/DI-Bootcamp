// let butn1=document.querySelector("#btn1");
// let butn2=document.querySelector("#btn2");
// function color(e) {
//     document.body.style.backgroundColor = e.target.textContent.toLowerCase()
// }
// butn1.addEventListener("click",color);
// butn2.addEventListener("click",color);

const colors = ["blue", "yellow", "green", "pink"];

function createBut() {
    const divCont=document.body.firstElementChild
    // divb.appendChild(nbtn)
    for (let color of colors) {
        const nbtn=document.createElement("button")
        const content=document.createTextNode(`Click here`)
        nbtn.setAttribute("value",color)
        nbtn.appendChild(content)
        divCont.appendChild(nbtn)
        nbtn.addEventListener("click",colorf)
    }

}
createBut()
function colorf(e) {
        document.body.style.backgroundColor = e.target.value.toLowerCase()
    }