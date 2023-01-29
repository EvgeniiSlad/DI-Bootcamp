//EX1.1
const people = ["Greg", "Mary", "Devon", "James"];
people.shift("Greg")
people.splice(2,3,"Jason")
people.push("Zhenya")
console.log(people.indexOf("Mary"));
console.log(people);
console.log(people.indexOf('Foo')); // it will return -1 because Foo does not exist in array people
let last = people[people.length-1];
console.log(last);
//EX1.2
for (let i = 0; i < people.length; i++) {
    console.log(people[i]);
}
for (let i = 0; i < people.length; i++) {
    if (people[i] == 'Jason') {
        break;
    }
    console.log(people[i]);
}

//EX2
const colors=["Black","White","Orange","Pink","Grey"]
num=0
for(let x=0;x<colors.length;x++){
    num++;
    console.log(`My #${num} choise is ${colors[x]} `);
}

//EX3
// const answ=Number(prompt("Enter a number"))
// while (answ<10) {
//     answ=Number(prompt("Enter a number"))
// }

//EX4
const building = {
    numberOfFloors: 4,
    numberOfAptByFloor: {
        firstFloor: 3,
        secondFloor: 4,
        thirdFloor: 9,
        fourthFloor: 2,
    },
    nameOfTenants: ["Sarah", "Dan", "David"],
    numberOfRoomsAndRent:  {
        sarah: [3, 990],
        dan:  [4, 1000],
        david: [1, 500],
    },
}
console.log(building.numberOfFloors);
console.log(building.numberOfAptByFloor.firstFloor+building.numberOfAptByFloor.thirdFloor);
console.log(building.nameOfTenants[1] +" is has "+building.numberOfRoomsAndRent.dan[0]+" rooms");
if(building.numberOfRoomsAndRent.david[1]+building.numberOfRoomsAndRent.sarah[1]>building.numberOfRoomsAndRent.dan[1]){
    building.numberOfRoomsAndRent.dan.splice(1,1,1200)
}
// console.log(building.numberOfRoomsAndRent.dan);

//EX5
let family={
    pairs: "Mom",
    pairs: "Dad",
    pairs: "Me"
}
for (const k in family) {
    console.log(k);
    console.log(family[k]);
}
//EX6
let details = {
    my: 'name',
    is: 'Rudolf',
    the: 'raindeer'
  }
let str = ''
for (let key in details){
str += key + ' ' + details[key] + ' ';
// console.log(details[key]);
// console.log(key);
}
console.log(str);
