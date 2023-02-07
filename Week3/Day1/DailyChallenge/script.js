let solarSistem = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
let sec = document.getElementsByTagName('section')
function divFun() {
let x = 1
    for (let i = 0; i < solarSistem.length; i++) {
        var divs = document.createElement('div');
        document.body.appendChild(divs);
        divs.className = 'planet'
        divs.setAttribute('id', x)
        x++
    }
    let mercury = document.getElementById(1).style.background = 'red';
    let venus = document.getElementById(2).style.background = 'orange';
    let earth = document.getElementById(3).style.background = 'yellow';
    let mars = document.getElementById(4).style.background = 'green';
    let jupiter = document.getElementById(5).style.background = 'lightblue';
    let saturn = document.getElementById(6).style.background = 'blue';
    let uranus = document.getElementById(7).style.background = 'purple';
    let neptune = document.getElementById(8).style.background = 'white';
}
console.log(divFun());