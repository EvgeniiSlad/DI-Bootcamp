let bar=document.getElementById("navBar")
bar.id="socialNetworkNavigation"
// console.log(bar);
const il1=document.createElement("il")
const uli=document.body.firstElementChild.children[0]
const textNode = document.createTextNode("Logout");
il1.append(textNode);
uli.appendChild(il1)
console.log(il1);

