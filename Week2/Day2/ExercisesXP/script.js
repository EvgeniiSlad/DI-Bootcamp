//EX1
let x = 5;
let y = 2;

if(x>y){
    console.log("x is the biggest number");
}else {
    console.log("EROOR");
}

//EX2
let newDog="Chihuahua";
//console.log(newDog.length);
// console.log(newDog.toUpperCase());
// console.log(newDog.toLowerCase());

if(newDog == "Chihuahua"){
    console.log("‘I love Chihuahuas, it’s my favorite dog breed");
}else{
    console.log("I dont care, I prefer cats");
}

//EX3
const chis = prompt("Write a namber")

if(chis%2==0){
    console.log(`${chis} is an even number`);
}else{
    console.log(`${chis} is an odd number`);
}

//EX4
const users = ["Lea123", "Princess45", "cat&doglovers", "helooo@000"];
const userOth=users.length-2;
if(users.length===0){
    console.log("No one is online");
}else if(users.length===1){
    console.log(`${users[0]} is online`);
}else if(users.length===2){
    console.log(`${users[0]} and ${users[1]} is online`);
}else if(users.length>2) {
    console.log(`${users[0]} and ${users[1]} and ${userOth} more are online`);
}