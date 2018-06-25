
function Predictor(id_input, id_canvas){
	//Connection
	var url_api = '/api';

	//Object vars
	var input = document.getElementById(id_input);
	//App status
	var canvas = document.getElementById(id_canvas);  // Where to draw
	var ctx = canvas.getContext("2d");



	function load_img(callback) {
		console.log("show preview");
		if (input.files && input.files[0]) {
			var reader = new FileReader();
			reader.onload = function(e) {
				console.log("ready");
				var img = new Image();
				img.onload = function(){
					callback(img);
				};
				img.src = e.target.result;
			};
			reader.readAsDataURL(input.files[0]);
		}
	}

	function canvas_draw_img(img){
		// Background
		canvas.width = img.width;
		canvas.height = img.height;
		ctx.drawImage(img, 0, 0);
	}


	function canvas_draw_damages(tiles){
		/*
		tiles: {
		  x: horizontal index for the tile
			y: vertical index for the tile
			damage: float(0.0 - 1.0) how damaged the tile is
	  }
		*/

		/*TODO
			n_x
			n_y
			and draw
		*/
		// Tiles
		console.log(tiles);
		// for (tile of tiles) {
		// 	ctx.beginPath();
		// 	ctx.lineWidth="2";
		// 	ctx.strokeStyle="magenta";
		// 	ctx.rect(tile.x, tile.y, tile.width, tile.height);
		// 	ctx.stroke();
		// }
	}





	//
	// AJAX CALLS: RPC, IMGS
	//

	function rpc_predict(img_b64, callback){
		axios.post(url_api, {
			jsonrpc: '2.0',
			method: 'PREDICTOR.predict',
			params: {
				img_b64: img_b64
			},
			id: 1
	  })
	  .then(function (response) {
	    console.log(response);
			callback(response);
	  })
	  .catch(function (error) {
	    console.log(error);
	  });

	}



	//
	// BUTTONS
	//

	function predict(){
		console.log("FUNCTION: predict");
		rpc_predict(canvas.toDataURL(), function(tiles){
			canvas_draw_damages(tiles);
		});
	}


	//Initialize object
	input.addEventListener("change", function(){
		load_img(canvas_draw_img);
	});

	return {
		predict: predict,
	}
}
