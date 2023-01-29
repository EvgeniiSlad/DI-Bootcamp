let zvez=""
for (let x = 0; x <=6; x++) {
    zvez += "* ";
    console.log(zvez);
}

//or
let one = '* '
let oth = '';
for (let i = 0; i < 7; i++) {
    for (let k = 0; k < 1; k++) {
       oth += one;
    }
    console.log(oth)
}