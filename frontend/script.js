const map = L.map("map").setView([33,44],5); //added leaflet map coordinates for the middle east
L.tileLayer("https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png",{
    attribution: "© OpenStreetMap © CARTO",
}).addTo(map);
const button = document.getElementById("fetchButton");
const input = document.getElementById("yearInput");
const resultsList = document.getElementById("results");
button.addEventListener("click",() =>{
    const year = input.value;
    let url = "http://127.0.0.1:5000/empires";
    if (year) {
        url += `?year=${year}`;
    }
    fetch(url)
    .then(response => response.json())
    .then(data => {resultsList.innerHTML = "";
     if(data.length === 0) {
        resultsList.innerHTML = "<li>Sorry, no Empires found</li>";
        return;
     }
     data.forEach(empire => {
        const li = document.createElement("li");
        li.textContent = `${empire.empire_name} (${empire.start_year_bce}-${empire.end_year_bce} BCE)`;
        resultsList.appendChild(li);

     });
    })
    .catch(error =>{
        console.error("Error fetching data:",error);
    });
});