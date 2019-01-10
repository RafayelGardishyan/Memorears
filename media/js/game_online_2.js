setCallbackOnRecieve(gameId, function (data) {
    if (data.opencard1 !== null || data.opencard1 !== 25){
        memoryFlipTile(data.opencard1, memory_array[data.opencard1]);
    }
    if (data.opencard2 !== null || data.opencard2 !== 25){
        memoryFlipTile(data.opencard2, memory_array[data.opencard2]);
    }
});

function reset() {
  let game = {
    openCard1: 25,
    openCard2: 25,
    player_count: 0,
    player_scores: [
        0
    ],
    turn: 1,
    locked: false
  };

  writeGameData(gameId, game);
}

function set_score() {
  game.player_scores[game.turn - 1]++;
  writeGameData(gameId, game);
}

function changeTurn() {
  if (game.turn < game.player_count){
      game.turn++;
  } else{
      game.turn = 1;
  }

  document.getElementById("player").innerText = game.turn;

  writeGameData(gameId, game);

}