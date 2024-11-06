const image = document.getElementById('clickable-image');
const popup = document.getElementById('popup');
const overlay = document.getElementById('overlay');
const popupText = document.getElementById('popup-text');
const closeButton = document.getElementById('close-btn');
const linesDiv = document.getElementById('lines');

image.addEventListener('click', function(event) {
    const rect = image.getBoundingClientRect();
    const x = event.clientX - rect.left; // Position X relative à l'image
    const y = event.clientY - rect.top;  // Position Y relative à l'image

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
});

// Écouteur pour le bouton de fermeture
closeButton.addEventListener('click', function() {
    popup.classList.remove('show'); // Enlever l'animation
    setTimeout(() => {
        popup.style.display = 'none';
        overlay.style.display = 'none';
        linesDiv.innerHTML = ''; // Réinitialiser le contenu des lignes
    }, 300); // Attendre la fin de l'animation
});

// Écouteur pour fermer le popup en cliquant sur l'overlay
overlay.addEventListener('click', function() {
    popup.classList.remove('show'); // Enlever l'animation
    setTimeout(() => {
        popup.style.display = 'none';
        overlay.style.display = 'none';
        linesDiv.innerHTML = ''; // Réinitialiser le contenu des lignes
    }, 300); // Attendre la fin de l'animation
});
