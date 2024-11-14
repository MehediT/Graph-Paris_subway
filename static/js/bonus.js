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

const acpmButton = document.getElementById('acpm-btn');


const container = document.getElementById('imageContainer');
const reset = document.getElementById('reset-btn');
const canvas = document.getElementById("graphCanvas");
const canvas2 = document.getElementById("canvas");
const ctx = canvas.getContext("2d");

function drawEdges(aretes) {
    aretes.forEach(arete => {
        const start = numeroToPos[arete.source];
        const end = numeroToPos[arete.target];

        if (start && end) {
            ctx.beginPath();
            ctx.moveTo(start.x, start.y);
            ctx.lineTo(end.x, end.y);
            ctx.strokeStyle = arete.couleur;
            ctx.lineWidth = 2;
            ctx.stroke();


            const midX = (start.x + end.x) / 2;
            const midY = (start.y + end.y) / 2;
            ctx.fillStyle = "black";
            ctx.font = "12px Arial";
            ctx.fillText(arete.distance, midX, midY);
        }
    });
}

function drawNodes(sommets) {
    sommets.forEach(sommet => {
        const x = sommet.posx ;
        const y = sommet.posy;


        ctx.beginPath();
        ctx.arc(x, y, 4, 0, Math.PI * 2);
        ctx.fillStyle = "lightgray";
        ctx.fill();
        ctx.strokeStyle = "gray";
        ctx.stroke();


        ctx.fillStyle = "black";
        ctx.font = "8px Arial";
        ctx.fillText(sommet.name, x - 20 - sommet.name.length, y - 10);
    });
}

function drawGraph(graphData) {
    drawEdges(graphData.aretes);
    drawNodes(graphData.sommets);
}

canvas.addEventListener('click', function (event) {
    get_information_event(event);
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
        fetch(`/pcc2?station1=${selectedStation1}&station2=${selectedStation2}`)
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

acpmButton.addEventListener('click', () => {
    fetch(`/acpm`)
        .then(response => response.json())
        .then(data => {
            console.log(data);
            pcc_des.textContent = ``
            pcc.textContent = `Arbres couvrants de poids minimum`;
            pcc_chemin.innerHTML = '';

            // data.chemin.forEach(line => {
            //     const p = document.createElement('li');
            //     p.textContent = line;
            //     pcc_chemin.appendChild(p);
            // });

            canvas.style.filter = 'grayscale(100%)';
            canvas2.width = canvas.width;
            canvas2.height = canvas.height;

            canvas2.style.top = canvas.offsetTop + 'px';
            canvas2.style.left = canvas.offsetLeft + 'px';

            const ctx = canvas2.getContext("2d");
            ctx.clearRect(0, 0, canvas2.width, canvas2.height);
            aretes = data.aretes;
            
            aretes.forEach(arete => {
                const start = numeroToPos[arete.source];
                const end = numeroToPos[arete.target];
        
                if (start && end) {
                    ctx.beginPath();
                    ctx.moveTo(start.x, start.y);
                    ctx.lineTo(end.x, end.y);
                    ctx.strokeStyle = arete.couleur;
                    ctx.lineWidth = 2;
                    ctx.stroke();
        
        
                    const midX = (start.x + end.x) / 2;
                    const midY = (start.y + end.y) / 2;
                    ctx.fillStyle = "black";
                    ctx.font = "10px Arial";
                    ctx.fillText(arete.distance, midX, midY);
                }
            });
        })
        .catch(error => {
            console.error('Erreur lors du chargement des positions :', error);
        });
});

closeButton.addEventListener('click', function () {
    popup.classList.remove('show');
    setTimeout(() => {
        popup.style.display = 'none';
        overlay.style.display = 'none';
        linesDiv.innerHTML = '';
    }, 300);
});

overlay.addEventListener('click', function () {
    popup.classList.remove('show');
    setTimeout(() => {
        popup.style.display = 'none';
        overlay.style.display = 'none';
        linesDiv.innerHTML = '';
    }, 300);
});

reset.addEventListener('click', () => {
    pcc_des.textContent = ''
    pcc.textContent = '';
    pcc_chemin.innerHTML = '';
    
    canvas.width = image.width;
    canvas.height = image.height;
    canvas.style.filter = 'grayscale(0%)';

    const ctx = canvas.getContext('2d');
    ctx.clearRect(0, 0, canvas.width, canvas.height); // Effacer le canvas
});

function callAnimerTracerLignes(points) {

    canvas.style.filter = 'grayscale(100%)';
    canvas2.width = canvas.width;
    canvas2.height = canvas.height;

    canvas2.style.top = canvas.offsetTop + 'px';
    canvas2.style.left = canvas.offsetLeft + 'px';

    dessinerPoint(points[0].x, points[0].y, 'red');
    dessinerPoint(points[points.length - 1].x, points[points.length - 1].y, 'blue');

    animerTracageLigne(points);
};

function dessinerPoint(x, y, color) {
    const ctx = canvas2.getContext('2d');

    ctx.beginPath();
    ctx.arc(x, y, 4, 0, Math.PI * 2);
    ctx.fillStyle = color;
    ctx.fill();
    ctx.strokeStyle = "gray";
    ctx.stroke();


    // ctx.fillStyle = color;
    // ctx.font = "8px Arial";
    // ctx.fillText(sommet.name, x - 20 - sommet.name.length, y - 10);
}

function animerTracageLigne(points, segmentIndex = 0, progress = 0) {
    const ctx = canvas2.getContext('2d');
    ctx.clearRect(0, 0, canvas2.width, canvas2.height);

    for (let i = 0; i < segmentIndex; i++) {
        ctx.beginPath();
        ctx.moveTo(points[i].x, points[i].y);
        ctx.lineTo(points[i + 1].x, points[i + 1].y);
        ctx.strokeStyle = 'purple';
        ctx.lineWidth = 2;
        ctx.stroke();
    }


    if (segmentIndex < points.length - 1) {
        const start = points[segmentIndex];
        const end = points[segmentIndex + 1];


        const currentX = start.x + progress * (end.x - start.x);
        const currentY = start.y + progress * (end.y - start.y);

        ctx.beginPath();
        ctx.moveTo(start.x, start.y);
        ctx.lineTo(currentX, currentY);
        ctx.strokeStyle = 'red';
        ctx.lineWidth = 2;
        ctx.stroke();


        progress += 0.02;


        if (progress >= 1) {
            progress = 0;
            segmentIndex++;
        }


        requestAnimationFrame(() => animerTracageLigne(points, segmentIndex, progress));
    }

};

function get_information_event(event) {
    const rect = canvas.getBoundingClientRect();
    const x = event.clientX - rect.left;
    const y = event.clientY - rect.top;
    console.log(`X: ${x}, Y: ${y}`);

    fetch(`/get_zone?x=${x}&y=${y}`)
        .then(response => response.json())
        .then(data => {

            popupText.innerText = `Station : ${data.name}`;
            linesDiv.innerHTML = '';


            if (data.lines && data.lines.length > 0) {
                data.lines.forEach(line => {
                    const p = document.createElement('p');
                    p.textContent = line;
                    linesDiv.appendChild(p);
                });
            } else {
                linesDiv.innerHTML = 'Aucune ligne disponible pour cette zone.';
            }


            popup.style.display = 'block';
            overlay.style.display = 'block';

            setTimeout(() => {
                popup.classList.add('show');
            }, 10);
        });
};

function loadPositions() {
    fetch('/get_stations')
        .then(response => response.json())
        .then(data => {
            positionSelect1.innerHTML = '';
            let option = document.createElement('option');
            option.selected = true;
            option.value = '';
            option.textContent = 'Aucune station sélectionnée';
            positionSelect1.appendChild(option);

            positionSelect2.innerHTML = '';
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
const numeroToPos = {};

function loadGraph() {
    fetch('/get_graph')
        .then(response => response.json())
        .then(data => {
            data.sommets.forEach(sommet => {
                sommet.numeros.forEach(numero => {
                    numeroToPos[numero] = { x: sommet.posx, y: sommet.posy };
                });
            });
            drawGraph(data);
        })
        .catch(error => console.error('Erreur lors du chargement du graphe :', error));
}

loadPositions();
loadGraph();
