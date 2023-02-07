// //Ex1
// const hone=document.body.firstElementChild.children[0]
// // console.log(hone.textContent);

// const udl=document.body.firstElementChild.children[6]
// udl.parentElement.removeChild(udl)

// const htre=document.body.firstElementChild.children[2]
// htre.addEventListener("click",klik)
// function klik() {
//     document.body.firstElementChild.children[2].style.display='none'
// }

// const btn=document.createElement("button")
// const content=document.createTextNode(`Click here`)
// const art1=document.body.firstElementChild
// btn.appendChild(content)
// art1.appendChild(btn)
// btn.addEventListener("click",klik1)
// function klik1() {
//     document.body.style.fontWeight='bold'
// }

//EX2
// let form = document.forms[0]
// let form1 = document.getElementsByTagName('form')[0]
// console.log(form1);

// let fname = document.getElementById('fname')
// console.log(fname);
// let lname = document.getElementById('lname')
// console.log(lname);
// let submit = document.getElementById('submit')
// console.log(submit);

// let name1 = document.getElementsByName('fname')
// let name2 = document.getElementsByName('lname')

// let ul = document.getElementsByClassName('usersAnswer')[0]
// console.log(ul);
// let formF = document.getElementsByTagName('form')[0]
// formF.addEventListener('click',fun1 )
// function fun1(event){
//     event.preventDefault()
//     let inpt1 = document.getElementsByTagName('input')[0].value
//     let inpt2 = document.getElementsByTagName('input')[1].value
//     if (inpt1.length > 0  && inpt2.length > 0) {
//     console.log(inpt1 + ' ' + inpt2);
//     let li1 = document.createElement('li')
//     let li2 = document.createElement('li')
//     li1.innerText = inpt1
//     li2.innerText = inpt2
//      ul.appendChild(li1)
//      ul.appendChild(li2)
//     }
// }

//EX3
// var allBoldItems = ' '

// function getBold_items(){
//     for (let i = 0; i < 6; i++) {
//         let strng = document.getElementsByTagName('strong')[i].innerText
//         allBoldItems += strng + ' '
//     }
//     console.log(allBoldItems);
// }
// getBold_items()

// function highlight() {
//     for (let i = 0; i < 6; i++) {
//         let strng1 = document.getElementsByTagName('strong')[i].innerText
//         document.getElementsByTagName('strong')[i].style.color = 'blue'
//     }
// }
// highlight()

// function return_normal() {
//     for (let i = 0; i < 6; i++) {
//         let strng2 = document.getElementsByTagName('strong')[i].innerText
//         document.getElementsByTagName('strong')[i].style.color = 'black'
//     }
// }

// return_normal()

// function ex5() {
//     let pr = document.getElementsByTagName('p')[0].addEventListener('mouseover', highlight)
//     function highlight() {
//         for (let i = 0; i < 6; i++) {
//             let strng1 = document.getElementsByTagName('strong')[i].innerText
//             document.getElementsByTagName('strong')[i].style.color = 'blue'
//         }
//     }
    
//     pr = document.getElementsByTagName('p')[0].addEventListener('mouseout', return_normal)
//     function return_normal() {
//         for (let i = 0; i < 6; i++) {
//             let strng2 = document.getElementsByTagName('strong')[i].innerText
//             document.getElementsByTagName('strong')[i].style.color = 'black'
//         }
//     }
    
// }
// ex5()

//EX4
// Write a JavaScript program to calculate the volume of a sphere. Use the code below as a base:
let form = document.forms[0]
form.addEventListener('submit',calc )
function calc(evt) {
    evt.preventDefault()
    const inpRad=evt.target.radius.value
    const volRes=(((inpRad**3)*4*Math.PI)/3).toFixed(2)
    const inptVol=evt.target.volume
    console.log(volRes);
    inptVol.value=volRes
}

// //EX5
// let prgrph = document.getElementsByTagName('p')[0].addEventListener('click', clickPrgrph)
// function clickPrgrph() {
//     document.getElementsByTagName('p')[0].style.fontSize = '60px'
// }
//  prgrph = document.getElementsByTagName('p')[0].addEventListener('mouseover', mouseoverPrgrph)
//  function mouseoverPrgrph() {
//     document.getElementsByTagName('p')[0].style.color = 'lightblue'

// }
//  prgrph = document.getElementsByTagName('p')[0].addEventListener('mouseout', mouseoutPrgrph)
//  function mouseoutPrgrph() {
//     document.getElementsByTagName('p')[0].style.color = 'black'
// }
//  prgrph = document.getElementsByTagName('p')[0].addEventListener('dblclick', dblclickPrgrph)
//  function dblclickPrgrph() {
//     document.getElementsByTagName('p')[0].style.display = 'none'
//}
