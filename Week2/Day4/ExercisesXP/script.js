//EX1
function infoAboutMe() {
    const info="Zhenia 23 nope"
    console.log(info);
}
// infoAboutMe()

function infoAboutPerson(personName, personAge, personFavoriteColor) {
    console.log(`You name is ${personName}, you are ${personAge} years old, your favorite color is ${personFavoriteColor}`);
}
// infoAboutPerson("David", 45, "blue")
// infoAboutPerson("Josh", 12, "yellow")

//EX2
function calculateTip() {
    let bill = Number(prompt("What is the amount of the bill"))
    if (bill<50) {
        let tip=bill*0.2
        console.log(bill+tip);
    }else if(bill>=50 && bill<=200){
        let tip=bill*0.15
        console.log(bill+tip);
    } else if(bill>200){
        let tip=bill*0.10
        console.log(bill+tip);
    }
}      
// calculateTip()

//EX3
let sum=0
function isDivisible(dil=23) {
    for (let i = 0; i < 500; i++) {
        if(i%dil===0){
            sum+=i;
            console.log(i);
        }
    }
    console.log(sum);
}
// isDivisible()

//EX4
const stock = { 
    "banana": 6, 
    "apple": 0,
    "pear": 12,
    "orange": 32,
    "blueberry":1
}  

const prices = {    
    "banana": 4, 
    "apple": 2, 
    "pear": 1,
    "orange": 1.5,
    "blueberry":10
} 
const shoppingList=["banana","orange","aplle"]
let sum1= 0; 
 function myBill() {
   for (let i = 0; i < shoppingList.length; i++) {
      let a = shoppingList[i];
      if (a in stock && stock[a] > 0){
          sum += prices[a];
          stock[a] -= 1;
      }
   }
   console.log(sum);
   console.log(stock)
 }
//  myBill();

//EX5
function changeEnough(itemPrice, amountOfChange) {
    let money = [0.25, 0.1, 0.05, 0.01];
    let sum = 0;
       for (let i = 0; i < amountOfChange.length; i++) {
          sum += amountOfChange[i]*money[i];
       }
       if(sum >= itemPrice ){
          console.log(true);
       } else { 
          console.log(false);
       }
    
    }
// changeEnough(0.75, [0,0,20,5])
// changeEnough(14.11, [2,100,0,0])

//EX6
function hotelCost() {
    let numberOfNights = 0;
    do{
       numberOfNights = prompt('Enter the number of nights you would like to stay in the hotel');
    } while(isNaN(numberOfNights) || numberOfNights == 0);
    let price = 140 * numberOfNights;
    console.log(price);
 }
 hotelCost()
 
 function planeRideCost(){
     let destination;
     let price1;
     do {
        destination = prompt('Enter your destination')
     } while(!isNaN(destination) || destination == 0);
     
     if (destination == "London"){
        price1 = 183;
     } else if (destination == "Paris"){
        price1 = 220;
     } else {
        price1 = 300;
     }
     console.log(price1);
  }
  planeRideCost()
 