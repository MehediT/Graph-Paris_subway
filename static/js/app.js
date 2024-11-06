const image = document.getElementById('clickable-image');
const popup = document.getElementById('popup');
const overlay = document.getElementById('overlay');
const popupText = document.getElementById('popup-text');
const closeButton = document.getElementById('close-btn');
const linesDiv = document.getElementById('lines');
const coordinatesParagraph1 = document.getElementById('coordinates1');
const coordinatesParagraph2 = document.getElementById('coordinates2');

let isPosition1Active = false; // Indicateur pour Position 1
let isPosition2Active = false; // Indicateur pour Position 2

// Écoute le clic sur le bouton Position 1
document.getElementById('position1-btn').addEventListener('click', () => {
    isPosition1Active = true; // Active le mode Position 1
    isPosition2Active = false; // Désactive le mode Position 2
    coordinatesParagraph1.textContent = "Cliquez sur l'image pour obtenir les coordonnées.";
});

// Écoute le clic sur le bouton Position 2
document.getElementById('position2-btn').addEventListener('click', () => {
    isPosition2Active = true; // Active le mode Position 2
    isPosition1Active = false; // Désactive le mode Position 1
    coordinatesParagraph2.textContent = "Cliquez sur l'image pour obtenir les coordonnées.";
});

image.addEventListener('click', function (event) {
    if (isPosition1Active) {
        position1(event); // Appelle la fonction Position 1
    }
    else if (isPosition2Active) {
        position2(event); // Appelle la fonction Position 2
    }
    else {
        get_information_event(event); // Appelle la fonction pour obtenir les informations de la zone
    }
});

function position1(event) {
    const rect = image.getBoundingClientRect();
    const x = event.clientX - rect.left; // Position X relative à l'image
    const y = event.clientY - rect.top; // Position Y relative à l'image

    // Met à jour le paragraphe avec les coordonnées
    coordinatesParagraph1.textContent = `Coordonnées : X: ${x}, Y: ${y}`;

    // Optionnel : Désactiver le mode Position 1 après le clic
    isPosition1Active = false;
}
function position2(event) {
    const rect = image.getBoundingClientRect();
    const x = event.clientX - rect.left; // Position X relative à l'image
    const y = event.clientY - rect.top; // Position Y relative à l'image

    // Met à jour le paragraphe avec les coordonnées
    coordinatesParagraph2.textContent = `Coordonnées : X: ${x}, Y: ${y}`;

    // Optionnel : Désactiver le mode Position 1 après le clic
    isPosition2Active = false;
}

function get_information_event(event) {
    const rect = image.getBoundingClientRect();
    const x = event.clientX - rect.left; // Position X relative à l'image
    const y = event.clientY - rect.top;  // Position Y relative à l'image
    console.log(`X: ${x}, Y: ${y}`);
    // Appel AJAX pour obtenir le nom de la zone cliquée et les lignes associées
    fetch(`/get_zone?x=${x}&y=${y}`)
        .then(response => response.json())
        .then(data => {
            // Afficher le nom de la zone dans le popup
            popupText.innerText = `Station: ${data.name}`;
            linesDiv.innerHTML = ''; // Réinitialiser le contenu des lignes

            // Afficher les lignes associées à la zone cliquée directement
            if (data.lines && data.lines.length > 0) {
                data.lines.forEach(line => {
                    const p = document.createElement('li');
                    p.textContent = line;
                    linesDiv.appendChild(p);
                });
            } else {
                linesDiv.innerHTML = 'Aucune ligne disponible pour cette zone.';
            }

            // Afficher le popup et l'overlay avec animation
            popup.style.display = 'block';
            overlay.style.display = 'block';

            // Ajouter la classe "show" pour l'animation
            setTimeout(() => {
                popup.classList.add('show');
            }, 10);
        });
}

// Écouteur pour le bouton de fermeture
closeButton.addEventListener('click', function () {
    popup.classList.remove('show'); // Enlever l'animation
    setTimeout(() => {
        popup.style.display = 'none';
        overlay.style.display = 'none';
        linesDiv.innerHTML = ''; // Réinitialiser le contenu des lignes
    }, 300); // Attendre la fin de l'animation
});

// Écouteur pour fermer le popup en cliquant sur l'overlay
overlay.addEventListener('click', function () {
    popup.classList.remove('show'); // Enlever l'animation
    setTimeout(() => {
        popup.style.display = 'none';
        overlay.style.display = 'none';
        linesDiv.innerHTML = ''; // Réinitialiser le contenu des lignes
    }, 300); // Attendre la fin de l'animation
});
