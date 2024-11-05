const image = document.getElementById('clickable-image');
const popup = document.getElementById('popup');
const overlay = document.getElementById('overlay');
const popupText = document.getElementById('popup-text');
const closeButton = document.getElementById('close-btn');
const viewLinesButton = document.getElementById('view-lines');
const linesDiv = document.getElementById('lines');

image.addEventListener('click', function(event) {
    const rect = image.getBoundingClientRect();
    const x = event.clientX - rect.left; // Position X relative à l'image
    const y = event.clientY - rect.top;  // Position Y relative à l'image

    // Appel AJAX pour obtenir le nom de la zone cliquée
    fetch(`/get_zone?x=${x}&y=${y}`)
        .then(response => response.json())
        .then(data => {
            // Afficher le popup
            popupText.innerText = `Vous avez cliqué dans : ${data.name}`;
            popup.style.display = 'block';
            overlay.style.display = 'block';
        });
});

closeButton.addEventListener('click', function() {
    popup.style.display = 'none';
    overlay.style.display = 'none';
    linesDiv.innerHTML = ''; // Réinitialiser le contenu des lignes
});

viewLinesButton.addEventListener('click', function() {
    fetch('/get_lines')
        .then(response => response.json())
        .then(data => {
            linesDiv.innerHTML = ''; // Réinitialiser le contenu des lignes
            data.forEach(line => {
                const p = document.createElement('p');
                p.textContent = line;
                linesDiv.appendChild(p);
            });
        });
});

overlay.addEventListener('click', function() {
    popup.style.display = 'none';
    overlay.style.display = 'none';
    linesDiv.innerHTML = ''; // Réinitialiser le contenu des lignes
});
