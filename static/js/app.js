const image = document.getElementById('clickable-image');
const popup = document.getElementById('popup');
const overlay = document.getElementById('overlay');
const popupText = document.getElementById('popup-text');
const closeButton = document.getElementById('close-btn');
const linesDiv = document.getElementById('lines');
const positionSelect1 = document.getElementById('position-select1');
const positionSelect2 = document.getElementById('position-select2');

const pcc = document.getElementById('pcc-text');
const pcc_des = document.getElementById('pcc-des');
const pcc_chemin = document.getElementById('pcc-chemin');
const pccButton = document.getElementById('pcc-btn');
const canvas = document.getElementById('canvas');
const container = document.getElementById('imageContainer');
const reset = document.getElementById('reset-btn');

image.addEventListener('click', function (event) {
    get_information_event(event); // Appelle la fonction pour obtenir les informations de la zone
});

pccButton.addEventListener('click', () => {
    const selectedStation1 = positionSelect1.value;
    const selectedStation2 = positionSelect2.value;
    if (selectedStation1 === selectedStation2) {
        pcc.style.color = 'red';
        pcc.textContent = 'Veuillez sélectionner deux stations différentes';
    }
    else if (selectedStation1 == '' && selectedStation2 == '') {
        pcc.style.color = 'red';
        pcc.textContent = 'Veuillez sélectionner deux stations';
    }
    else {
        pcc.style.color = 'black';
        fetch(`/pcc?station1=${selectedStation1}&station2=${selectedStation2}`)
            .then(response => response.json())
            .then(data => {
                console.log(data);
                pcc_des.textContent = `La temps totale est de : ${data.time}`
                pcc.textContent = `le chemin le plus court entre ${data.st_station} et ${data.end_station}`;
                pcc_chemin.innerHTML = '';
                
                data.chemin.forEach(line => {
                    const p = document.createElement('li');
                    p.textContent = line;
                    pcc_chemin.appendChild(p);
                });

                callAnimerTracerLignes(data.points)
            }
            )
            .catch(error => {
                console.error(`/pcc?station1=${selectedStation1}&station2=${selectedStation2}`);
                console.error('Erreur lors du chargement des positions :', error);
            });
    }
    
});

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

// Écouteur pour le bouton de réinitialisation
reset.addEventListener('click', () => {
    pcc_des.textContent = ''
    pcc.textContent = '';
    pcc_chemin.innerHTML = '';
    
    canvas.width = image.width;
    canvas.height = image.height;
    image.style.filter = 'grayscale(0%)';

    const ctx = canvas.getContext('2d');
    ctx.clearRect(0, 0, canvas.width, canvas.height); // Effacer le canvas
});

function callAnimerTracerLignes(points) {
    // Ajuster la taille du canvas à celle de l'image
    image.style.filter = 'grayscale(100%)';
    canvas.width = image.width;
    canvas.height = image.height;

    canvas.style.top = image.offsetTop + 'px';
    canvas.style.left = image.offsetLeft + 'px';

    dessinerPoint(points[0].x, points[0].y, 'red', 5);
    dessinerPoint(points[points.length - 1].x, points[points.length - 1].y, 'blue', 5);
    // Démarrer l'animation
    animerTracageLigne(points);
};

function dessinerPoint(x, y, couleur = 'red', taille = 3) {
    const ctx = canvas.getContext('2d');

    ctx.beginPath();
    ctx.arc(x, y, taille, 0, 2 * Math.PI); // Créer un cercle pour le point
    ctx.fillStyle = couleur;
    ctx.fill();
}

function animerTracageLigne(points, segmentIndex = 0, progress = 0) {
    const ctx = canvas.getContext('2d');
    ctx.clearRect(0, 0, canvas.width, canvas.height); // Effacer le canvas

    // Parcourir tous les segments déjà tracés et les dessiner en entier
    for (let i = 0; i < segmentIndex; i++) {
        ctx.beginPath();
        ctx.moveTo(points[i].x, points[i].y);
        ctx.lineTo(points[i + 1].x, points[i + 1].y);
        ctx.strokeStyle = 'purple';
        ctx.lineWidth = 6;
        ctx.stroke();
    }

    // Tracer le segment en cours avec animation
    if (segmentIndex < points.length - 1) {
        const start = points[segmentIndex];
        const end = points[segmentIndex + 1];

        // Calcul de la position intermédiaire
        const currentX = start.x + progress * (end.x - start.x);
        const currentY = start.y + progress * (end.y - start.y);

        ctx.beginPath();
        ctx.moveTo(start.x, start.y);
        ctx.lineTo(currentX, currentY);
        ctx.strokeStyle = 'red';
        ctx.lineWidth = 6;
        ctx.stroke();

        // Incrémenter la progression
        progress += 0.02;

        // Si le segment est entièrement tracé, passer au segment suivant
        if (progress >= 1) {
            progress = 0; // Réinitialiser la progression pour le prochain segment
            segmentIndex++;
        }

        // Continuer l'animation
        requestAnimationFrame(() => animerTracageLigne(points, segmentIndex, progress));
    }

};

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
            popupText.innerText = `Station : ${data.name}`;
            linesDiv.innerHTML = ''; // Réinitialiser le contenu des lignes

            // Afficher les lignes associées à la zone cliquée directement
            if (data.lines && data.lines.length > 0) {
                data.lines.forEach(line => {
                    const p = document.createElement('p');
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
};

// Fonction pour charger les positions dynamiques
function loadPositions() {
    fetch('/get_stations')
        .then(response => response.json())
        .then(data => {
            positionSelect1.innerHTML = ''; // Vide les options existantes
            let option = document.createElement('option');
            option.selected = true;
            option.value = '';
            option.textContent = 'Aucune station sélectionnée';
            positionSelect1.appendChild(option);

            positionSelect2.innerHTML = ''; // Vide les options existantes
            option = document.createElement('option');
            option.selected = true;
            option.value = '';
            option.textContent = 'Aucune station sélectionnée';
            positionSelect2.appendChild(option);

            data.forEach(station => {
                const option = document.createElement('option');
                option.value = `${station.num}`;
                option.textContent = `${station.libelle}`;
                positionSelect1.appendChild(option);

                const option2 = document.createElement('option');
                option2.value = `${station.num}`;
                option2.textContent = `${station.libelle}`;
                positionSelect2.appendChild(option2);
            });
        })
        .catch(error => console.error('Erreur lors du chargement des positions :', error));
};

loadPositions(); // Charger les positions dynamiques au chargement de la page
