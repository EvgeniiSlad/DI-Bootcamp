let downBottles = 0
let bottles = Number(prompt('Number of bottles:'))
function getInput() {
    while (bottles - downBottles > 0) {
        console.log(`${bottles} bottles of beer on the wall\n${bottles} bottles of beer`);
        downBottles++
        bottles -= downBottles
        if (downBottles == 1) {
            console.log(`Take ${downBottles} down, pass it around\n${bottles} bottles of beer on the wall`);
        } else {
            console.log(`Take ${downBottles} down, pass them around\n${bottles} bottles of beer on the wall`);
        }
    }
console.log(`${bottles} bottles of beer on the wall\n${bottles} bottles of beer`);
console.log(`Take ${bottles} down, pass them around\nNo bottle of beer on the wall`);
}
getInput()