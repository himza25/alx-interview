#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

// Function to fetch character data
function fetchCharacter (characterUrl, callback) {
  request(characterUrl, (error, response, body) => {
    if (error) {
      callback(error);
      return;
    }
    const characterData = JSON.parse(body);
    callback(null, characterData.name);
  });
}

// Fetch movie data
request(url, (error, response, body) => {
  if (error) {
    console.error('Error fetching movie data:', error);
    return;
  }
  const filmData = JSON.parse(body);
  const characters = filmData.characters;

  // Fetch character names in order
  const fetchCharacterNames = characters.map(characterUrl => {
    return new Promise((resolve, reject) => {
      fetchCharacter(characterUrl, (error, name) => {
        if (error) {
          reject(error);
        } else {
          resolve(name);
        }
      });
    });
  });

  // Resolve all promises and print character names
  Promise.all(fetchCharacterNames)
    .then(names => {
      names.forEach(name => console.log(name));
    })
    .catch(error => {
      console.error('Error fetching character names:', error);
    });
});
