let btn = document.body.firstElementChild.children[0]
// console.log(btn);
btn.addEventListener("click", myMove)
function myMove() {
    let position = 0 
    let animateDiv = document.getElementById('animate')
    let interval = setInterval (zuz,10)
    function zuz() {
        if (position == 350){
            clearInterval(interval)
        } else {
            position++
            animateDiv.style.left = position + 'px'
        }
    }
}
