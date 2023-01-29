//EX1
const favfood="Pizza";
const favmel="lunch";
let pre=`I eat ${favfood} at every ${favmel}`;
console.log(pre);

//ex2
const myWatchedSeries = ["black mirror", "money heist", "the big bang theory"];
const myWatchedSeriesLength=myWatchedSeries.length;
const myWatchedSeriesSentence=myWatchedSeries [0]+ ', ' +myWatchedSeries[1]+ ', and ' +myWatchedSeries[2];
console.log('i watched' + ' ' + myWatchedSeriesLength + ' ' + 'series:' + ' ' + myWatchedSeriesSentence);
myWatchedSeries.splice(2,2,"friends");
myWatchedSeries.push("shamless");
myWatchedSeries.shift();
myWatchedSeries.reverse();
console.log(myWatchedSeries);

//ex3
const cestem=30;
const fartem=cestem/5*9+32;
console.log(`${cestem}°C is ${fartem}°F`);

//ex4
let c;
let a = 34;
let b = 21;

console.log(a+b) //first expression
// Prediction:It will output 25, because 34 and 21 are numbers
// Actual:55

a = 2;

console.log(a+b) //second expression
// Prediction:It will output 23, because "a" now 2 and "b" 21
// Actual:23

// What will be the outcome of a + b in the first expression ? 55
// What will be the outcome of a + b in the second expression ? 23
// What is the value of c? undefined
console.log(3 + 4 + '5');
// Prediction: 75 because 3 and 4 are nubers and we can sum them. but '5' ia a string, so we cant do with it any math manipulation
// Actual: 75

//ex5
console.log(typeof(15));
// Prediction: number. its a number. it hasnt quotes
// Actual: number

console.log(typeof(5.5));
// Prediction: number its still a number. it hasnt quotes
// Actual: number

console.log(typeof(NaN));
// Prediction: number nan = mot a number, but it has type of number
// Actual: number

console.log(typeof("hello"));
// Prediction: string because its in quotes
// Actual:string

console.log(typeof(true));
// Prediction: boolean 
// Actual:boolean

console.log(typeof(1 != 2));
// Prediction: boolean because there is a comparison
// Actual: boolean

console.log("hamburger" + "s");
// Prediction: hamburgers combining two lines 
// Actual: hamburgers

console.log("hamburgers" - "s");
// Prediction: --
// Actual: nan

console.log("1" + "3");
// Prediction: 13  two strings, not numbers
// Actual: 13

console.log("1" - "3");
// Prediction: nan
// Actual: -2   

console.log("johnny" + 5);
// Prediction: johnny5 we cant sum a string a a number
// Actual:nan

console.log("johnny" - 5);
// Prediction: nan we cant subtract a string a a number
// Actual:nan

console.log(99 * "hello");
// Prediction: nan we cant multiply a string a a number
// Actual:nan

console.log(1 != 1);
// Prediction: false because 1 = 1 - its true. and here != that means 1 not equal 1 
// Actual:false

console.log(1 == "1");
// Prediction: true here isnt strictly equal
// Actual:true

console.log(1 === "1");
// Prediction: false strictly equal and here compare string and number
// Actual:false

// EX6
console.log(5 + "34");
// Prediction: 534 not two numbers
// Actual:534

console.log(5 - "4");
// Prediction: 1 we use - only for subtractions, so 4 counts as a number
// Actual:1

console.log(10 % 5);
// Prediction: 0 because 10/5 = 2 without any residues
// Actual:0

console.log(5 % 10);
// Prediction: 5 
// Actual:5

console.log("Java" + "Script");
// Prediction: JavaScript its two strings without space
// Actual:JavaScript

console.log(" " + " ");
// Prediction:'  '. just space without any variables
// Actual:'  '

console.log(" " + 0);
// Prediction:' 0' - space and the number
// Actual:' 0'

console.log(true + true);
// Prediction: 2 true = 1 => 1 + 1 =2
// Actual:2

console.log(true + false);
// Prediction: 1 true=1, false=0
// Actual:1

console.log(false + true);
// Prediction: 1 true=1, false=0
// Actual:1

console.log(false - true);
// Prediction: -1 true=1, false=0
// Actual:-1

console.log(!true);
// Prediction: false ! its a logical negation
// Actual:false 1

console.log(3 - 4);
// Prediction: -1 
// Actual:-1

console.log("Bob" - "bill");
// Prediction:nan its two strings, not numbers
// Actual:nan
