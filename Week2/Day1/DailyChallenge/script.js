//EX1
const fruits = ["Banana", "Apples", "Oranges", "Blueberries"];
fruits.shift();
fruits.sort();
fruits.push("Kiwi")
fruits.reverse();
fruits.pop();
console.log(fruits)

//EX2
const moreFruits = ["Banana", ["Apples", ["Oranges"], "Blueberries"]];
let or = moreFruits[1][1][0];
console.log(or);

