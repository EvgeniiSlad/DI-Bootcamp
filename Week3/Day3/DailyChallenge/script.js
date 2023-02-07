let body = document.getElementsByTagName('body')[0]
let inpt = document.createElement('input')
document.body.appendChild(inpt)
inpt.addEventListener('keyup',function(e) {
    this.value = this.value.replace(/[^a-zA-Z]/g,"")
})