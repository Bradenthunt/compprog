document
  .getElementById("search")
  .addEventListener("change", (event) => getCharacterData(event.target.value));

const getCharacterData = (number) => {
  const charName = document.getElementById("name");
  const height = document.getElementById("height");
  const mass = document.getElementById("mass");
  const hair = document.getElementById("hair");
  const skin = document.getElementById("skin");
  const eye = document.getElementById("eye");
  const birth = document.getElementById("birth");
  const gender = document.getElementById("gender");
  const home = document.getElementById("home");
  const world = document.getElementById("world");

  fetch(`https://swapi.dev/api/people/${number}/`)
    .then((response) => response.json())
    .then((data) => {
      let mainCharacter;
      mainCharacter = data;
      console.log(mainCharacter);
      charName.innerHTML = `Name: <strong>${mainCharacter.name}</strong>`;
      height.innerHTML = `Height: <strong>${mainCharacter.height}cm</strong>`;
      mass.innerHTML = `Weight: <strong>${mainCharacter.mass}kg</strong>`;
      hair.innerHTML = `Hair Color: <strong>${mainCharacter.hair_color}</strong>`;
      skin.innerHTML = `Skin Color: <strong>${mainCharacter.skin_color}</strong>`;
      eye.innerHTML = `Eye Color: <strong>${mainCharacter.eye_color}</strong>`;
      birth.innerHTML = `YOB: <strong>${mainCharacter.birth_year}</strong>`;
      gender.innerHTML = `Gender: <strong>${mainCharacter.gender}</strong>`;

      fetch(`${mainCharacter.homeworld}`)
        .then((response) => response.json())
        .then((data) => {
          let homeWorld;
          homeWorld = data;
          console.log(homeWorld);
          home.innerHTML = `Home World: <strong>${homeWorld.name}</strong>`;
          world.innerHTML = `${homeWorld.name}`;
        })
        .catch((error) => console.log(error));
    })
    .catch((error) => console.log(error));
};
