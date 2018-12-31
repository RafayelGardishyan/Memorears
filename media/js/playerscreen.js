let player = 0;
opencards = [];
function checkpin(inputfield) {
  if (inputfield.value.length === 5){
      let xhttp = new XMLHttpRequest();
      xhttp.onreadystatechange = function() {
          if (this.readyState === 4 && this.status === 200) {
            document.getElementById("beforegame").classList.add('hidden');
            document.getElementById("game").classList.remove('hidden');
          }
      };
    xhttp.open("GET", "/getgame/"+inputfield.value, true);
    xhttp.send();
    }
    xhttp = new XMLHttpRequest();
      xhttp.onreadystatechange = function() {
          if (this.readyState === 4 && this.status === 200) {
              if (JSON.parse(this.responseText)[0] === false){
                  window.location.href = "/player?l=true";
              }
              player = this.responseText[1];
      }
    };
    xhttp.open("GET", "/setonline/"+inputfield.value, true);
    xhttp.send();
    }

for (i = 0; i < 4; i++){
    document.getElementById('buttons').innerHTML += '<tr class="buttonrow" id="row_' + i + '"></tr>';
  for(j = 0; j < 6; j++){
    id = i * 6 + j;
    document.getElementById('row_' + i).innerHTML += '<th class="buttonhok"><button onclick="send(' + id + ')" id="' + id + '" class="clickablebutton">&nbsp;&nbsp;&nbsp;</button></th>'
  }
}

function send(id) {
    if (opencards.length < 1){
        opencards.push(id);
        colorinterval()
    }else if (opencards.length < 2){
        opencards.push(id);
        colorinterval();
        setTimeout(function() {

        colorintervalBack();
        opencards = [];
        }, 1000)
    }
    let xhttp = new XMLHttpRequest();
    xhttp.open("GET", "/set/opencard/"+id+"/"+player, true);
    xhttp.send();
    }

function colorinterval() {
  opencards.forEach(function(item) {
    document.getElementById(item).style.backgroundColor = "#fff";
      document.getElementById(item).style.color = "#3b094e"
  })
}
function colorintervalBack() {
  opencards.forEach(function(item) {
      document.getElementById(item).style.backgroundColor = "#3b094e";
    document.getElementById(item).style.color = "#fff"
  })
}
let ajaxinterval = setInterval(function() {
        let xhttp = new XMLHttpRequest();
        xhttp.onreadystatechange = function() {
            if (this.readyState === 4 && this.status === 200) {
                let response = JSON.parse(this.responseText);
                document.getElementById('score').innerHTML = JSON.parse(response.player_score)[player - 1];
                let turn = response.turn;
                if (turn.toString() === player){
                    let element = document.getElementById('myturn');
                    element.innerHTML = "Mijn beurt";
                    element.style.backgroundColor = "rebeccapurple";
                    element.style.color = "#ffffff";
                }else{
                    let element = document.getElementById('myturn');
                    element.innerHTML = "Even wachten ...";
                    element.style.backgroundColor = "#444444";
                    element.style.color = "black"
                }
        }
      };
      xhttp.open("GET", "/getgame", true);
      xhttp.send();
}, 1000);

function getUrlVars() {
    let vars = {};
    let parts = window.location.href.replace(/[?&]+([^=&]+)=([^&]*)/gi, function (m, key, value) {
        vars[key] = value;
    });
    return vars;
}
