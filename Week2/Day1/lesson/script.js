//ex1
let addressNumber = 41;
let addressStreet = "BenYehuda";
let countr = "Israel";
let globalAddress = `I live in ${addressStreet} ${addressNumber},in ${countr}`;
//console.log(globalAddress);

//ex2
const byear= 1999
const year= 2055
let age=year-byear
//console.log(`I will be ${age} in ${year}`)

//ex3
let pets=['cat','dog','fish','rabbit','cow'];
let dog=pets.slice(1,2);
console.log(dog);
//pets.push("horse");
pets.splice(3,1,"horse")
//delete pets[2,3]
let string=pets.toString();
console.log(string);