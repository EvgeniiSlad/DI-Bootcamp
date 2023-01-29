// //object
const trip={
    city : "Paris",
    date : "June",
    time : 12,
}
//text
const senTrip= `In ${trip["date"]}, I go to ${trip["city"]}`;
console.log(senTrip);

//change key
trip["time"]=2;
//console.log(trip);

//add key
trip["airlines"]="ELAL";
//trip["airlines"]=["ELAL","USAirline"]
//console.log(trip);


//ex1
const userCart = {
	username : "John",
	password: 1234,
	isUserSignedIn : true,
	cart : {
		apple : 2,
		banana : 1,
		pear : 5,
	},
	prices : {
		apple : 0.5,
		banana : 0.8646466363,
		pear : 0.2
	}
};

// 1. Add the lastname Smith to the object
// 2. Change the price of the pear, so it will include the Taxes. (17% is 0.17)
// 3. Ask the user for the fruit he wants between Apple, Banana and Pear. Make sure that your code accept all type of strings, for example "Banana" or "banana" or "BaNaNA"
// 4. Console.log the price for the specific fruit the user wants
//1
userCart["lastname"]="Smith";

//2
userCart["username"]="Tom"

//2
userCart["prices"]["pear"]*=1.17;

//3
const chois = prompt("What fruit to you want").toLowerCase();
//console.log(userChoice);

//4
const value=userCart["prices"][chois];
console.log(`Price is ${value}`);