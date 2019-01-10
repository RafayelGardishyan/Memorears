let player = 0;
opencards = [];
let Mgame;
let gameId;

function checkpin(inputfield) {
    if (inputfield.value.length === 5) {
        getOnce(inputfield.value);
        setTimeout(function () {
            console.log(Mgame);
            if (Mgame !== undefined) {
                gameId = inputfield.value;
                document.getElementById("beforegame").classList.add('hidden');
                document.getElementById("game").classList.remove('hidden');
                Mgame.player_count++;
                player = Mgame.player_count;
                try {
                    Mgame.player_scores[Mgame.player_count - 1] = 0;
                } catch (e) {
                    Mgame.player_scores.push(0);
                }

                writeGameData(gameId, Mgame);
            }
        }, 1000);
    }
}

for (i = 0; i < 4; i++) {
    document.getElementById('buttons').innerHTML += '<tr class="buttonrow" id="row_' + i + '"></tr>';
    for (j = 0; j < 6; j++) {
        id = i * 6 + j;
        document.getElementById('row_' + i).innerHTML += '<th class="buttonhok"><button onclick="send(' + id + ')" id="' + id + '" class="clickablebutton">&nbsp;&nbsp;&nbsp;</button></th>'
    }
}

function send(id) {
    if (opencards.length < 1) {
        opencards.push(id);
        colorinterval()
    } else if (opencards.length < 2) {
        opencards.push(id);
        colorinterval();
        setTimeout(function () {

            colorintervalBack();
            opencards = [];
        }, 1000)
    }
    if (Mgame.openCard1 !== 25) {
        Mgame.openCard1 = id;
    } else if (Mgame.openCard2 !== 25) {
        Mgame.openCard2 = id;
    } else {
        Mgame.openCard1 = 25;
        Mgame.openCard2 = 25;
    }
    writeGameData(gameId, Mgame);
}

function colorinterval() {
    opencards.forEach(function (item) {
        document.getElementById(item).style.backgroundColor = "#fff";
        document.getElementById(item).style.color = "#dd3f5b"
    })
}

function colorintervalBack() {
    opencards.forEach(function (item) {
        document.getElementById(item).style.backgroundColor = "#dd3f5b";
        document.getElementById(item).style.color = "#fff"
    })
}

setCallbackOnRecieve(gameId, function (data) {
    console.log(data);
    Mgame = data;
    let turn = Mgame.turn;
    if (turn.toString() === player) {
        let element = document.getElementById('myturn');
        element.innerHTML = "Mijn beurt";
        element.style.backgroundColor = "rebeccapurple";
        element.style.color = "#ffffff";
    } else {
        let element = document.getElementById('myturn');
        element.innerHTML = "Even wachten ...";
        element.style.backgroundColor = "#444444";
        element.style.color = "black"
    }

});
