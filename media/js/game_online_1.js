
let plus = 0;
let doo = 0;
function set_score() {
  let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState === 4 && this.status === 200) {
          plus = 0;
          console.log(this.responseText);
    }
  };
  xhttp.open("GET", "/set/score/" + turn.toString() + "/" + plus, true);
  xhttp.send();
}
let memory_values = [];
let memory_tile_ids = [];
let tiles_flipped = 0;
Array.prototype.memory_tile_shuffle = function(){
    let i = this.length, j, temp;
    while(--i > 0){
        j = Math.floor(Math.random() * (i+1));
        temp = this[j];
        this[j] = this[i];
        this[i] = temp;
    }
}
function newBoard(){
	tiles_flipped = 0;
	let output = '';
    memory_array.memory_tile_shuffle();
	for(let i = 0; i < memory_array.length; i++){
		output += '<div id="tile_'+i+'" onclick="memoryFlipTile(' + i + ',\''+memory_array[i]+'\')"></div>';
	}
	document.getElementById('memory_board').innerHTML = output;
}
function memoryFlipTile(tileid, val){
    if (tileid === 25 || tileid === null){
        return false;
    }
    tile = document.getElementById("tile_" + tileid);
	if(tile.innerHTML === "" && memory_values.length < 2){
		tile.style.backgroundSize = '0px 0px;';
		tile.innerHTML = '<img class="image" src="' + val + '" height="113" width="113">';
		if(memory_values.length === 0){
			memory_values.push(val);
			memory_tile_ids.push(tile.id);
		} else if(memory_values.length === 1){
			memory_values.push(val);
			memory_tile_ids.push(tile.id);
			if(memory_values[0] === memory_values[1]){
			    console.log("Change Score");
			    plus = 1;
//			    plus = 1;
//			    set_score();
//			    plus = 1;
//			    set_score();
				tiles_flipped += 2;
				// Clear both arrays
				memory_values = [];
            	memory_tile_ids = [];
				// Check to see if the whole board is cleared
				if(tiles_flipped === memory_array.length){
//					modal.style.display = "block";
					document.getElementById('memory_board').innerHTML = "";
					resetscore();
					window.location.reload();
				}
			} else {
				function flip2Back(){
				    doo = 1;
				    // Flip the 2 tiles back over
				    let tile_1 = document.getElementById(memory_tile_ids[0]);
				    let tile_2 = document.getElementById(memory_tile_ids[1]);
				    tile_1.style.backgroundSize = '116px 116px;';
            	    tile_1.innerHTML = "";
				    tile_2.style.backgroundSize = '116px 116px;';
            	    tile_2.innerHTML = "";
				    // Clear both arrays
				    memory_values = [];
            	    memory_tile_ids = [];
//                    reset();
				}
				setTimeout(flip2Back, 3500);
			}
			reset();
		}
	}
}