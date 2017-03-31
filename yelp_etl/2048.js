var array = [
	[0,0,0,0],
	[0,2,0,0],
	[0,2,0,0],
	[0,0,0,0]
	
];
function drawArray(){
	console.log("Drawing array");
	console.log(array);
	var table = "<table>";
	for( var i in array ){
		table += "<tr>";
		for(var j in array[i]){
			table += "<td>" + array[i][j] + "</td>";
		}
		table += "</tr>";
	}
	table += "</table>";
	$("div#container").html(table);
}
$(document).keydown(function(e) {
	    switch(e.which) {
	        case 37: // left
	        move("left");
		        
	        break;
	        
	        case 38: // up
	        move("up");
		      
	        break;
	        
	        case 39: // right
	        move("right");
	        break;

	        case 40: // down
	        move("down");
	        break;

	        default: return; // exit this handler for other keys
	    }
	    e.preventDefault(); // prevent the default action (scroll / move caret)
});

function putRandomNumber(){
	var blankPos = [];

	for(var i=0; i<4 ;i++){
		for(var j=0; j< 4; j++){
			if(array[i][j] == 0 ){
				console.log(i);
				var a = [i,j];
				blankPos.push(a);
			}
		}
	}
	
	if(blankPos.length == 1){
		var bpos = blankPos[0];
		array[bpos[0]][bpos[1]] = 2;

	}else if(blankPos.length > 1){
		var rpos = Math.floor((Math.random()* blankPos.length)+1);
		var bpos = blankPos[rpos];
		array[bpos[0]][bpos[1]] = 2;

	}
	
}
function move(direction){
	console.log(direction)

	if(direction === "left"){
		// for each row
		for(var i=0; i<4 ;i++){
			for(var j=0; j< 4; j++){
				if(array[i][j] == 0 && j+1 < 4){
					if(array[i][j] == array[i][j+1]){
						array[i][j] = array[i][j] + array[i][j+1];
						
					}else{
						array[i][j] = array[i][j+1]
						
					}
					
				}else if(array[i][j] == array[i][j+1]){
					array[i][j] = array[i][j] + array[i][j+1];
					
					
				}
			}
		}
		
	}
	
	putRandomNumber();
	drawArray();
	
	
}
$(document).ready(function(){
	drawArray();
	
	
});