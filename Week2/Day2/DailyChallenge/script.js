let sentence = ("This movie is not so bad !");
let wordNot = sentence.search ("not");//or .indexOf
let wordBad = sentence.search ("bad");
// console.log(wordNot);
// console.log(wordBad);
if(wordNot===-1){
    console.log(sentence);
}else  if(wordNot<wordBad){
    const per=sentence.slice(0,wordNot)
    const pos=sentence.slice(wordBad + 3)
    console.log(per+"good"+pos);
}else {
    console.log(sentence);
}