// function sum(num1,num2) {
//     console.log(num1*num2);
// }   
// sum(10,20)
// sum(13,1234)

function age(myAge) {
    const mage=myAge*2;
    const dage=mage*1.2;
    console.log(`Age of my Mum ${mage} and my Dad ${dage}`);
}
 age(20)

 function checkQuantityOrder(boxes) {
    if(10>=boxes && boxes>5){
        console.log("Dear client, you won a bouquet of flowers");
    }else if(20>=boxes && boxes>10){
        console.log("Dear client, you won a bottle of wine");
    }else if(boxes>20){
        console.log("Dear client, you won a trip to Paris");
    }else{}
 }
 checkQuantityOrder(8);
 checkQuantityOrder(15);
 checkQuantityOrder(30);

 function checkQuantityOrder1(boxes,name='client') {
    if(10>=boxes && boxes>5){
        console.log(`Dear ${name}, you won a bouquet of flowers`);
    }else if(20>=boxes && boxes>10){
        console.log(`Dear ${name}, you won a bottle of wine`);
    }else if(boxes>20){
        console.log(`Dear ${name}, you won a trip to Paris`);
    }
 }
checkQuantityOrder1(8, "John");
checkQuantityOrder1(15);
checkQuantityOrder1(30, "David");
//EX2
function age(myAge) {
    const mage=myAge*2;
    return mage;
}

 const mumage=age(23)
 console.log(mumage);