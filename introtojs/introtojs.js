const myName = "Mr Hunt";

let favColor = "Blue";

favColor = "Red";

console.log(favColor);

let age = 30;

mainPerson = {
  name: "Jason",
  age: 300,
  favColor: "Blue",
  favFoods: ["steak", "ice cream", "potatoes"],
};

favThings = [2, "movies"];

let isLoggedIn = false;

// function describePerson(person) {
//   //   console.log("MISSING PERSON ALERT: " + person.name);
//   alert(
//     `MISSING PERSON ALERT: ${person.name} missing since 2022, wearing tattered overalls.`
//   );
// }

// describePerson(mainPerson);

if (isLoggedIn) {
  document.getElementById("title").innerHTML = `Hello ${myName}`;
} else {
  document.getElementById("title").innerHTML = "Hello Guest";
}

const para = document.createElement("p");
para.innerHTML = "I'm the paragraph you just created.";
document.getElementById("div1").appendChild(para);
