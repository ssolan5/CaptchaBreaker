var fs = require('fs');
var value = "";
var fileName = process.argv[2];

parseJSONInFile();

function parseJSONInFile(){
	//console.log(fileName);
	finalTranscription = "";
	fs.readFile(fileName, 'utf-8', function (err, data) {
	  words = data.split(" "); 
	  words.forEach(function(word){
	  	if(isNatoWord(word)){
	  		finalTranscription = finalTranscription + word.charAt(0);
	  	}else{
	  		word = getTranslation(word);
	  		finalTranscription = finalTranscription + word.charAt(0);
	  	}
	  });
	  fs.writeFile(fileName, finalTranscription);
	});
}

function isNatoWord(){
	var arg = (Array.prototype.slice.call(arguments, 0))[0];
	var natoWords = new Array()
	natoWords = ["alfa", "alpha", "bravo", "charlie", "delta", "echo", "foxtrot", "golf", "hotel", "india", "juliett", "juliet" , "kilo", "lima", "mike", "november", "oscar","oskar", "papa", "quebec", "romeo", "sierra", "tango", "uniform", "new form",  "victor", "whiskey","x-ray", "yankee", "zulu"];
	if(arg.length>0){	
		for (var j=0; j<natoWords.length; j++) {
	        if (arg.toLowerCase().indexOf(natoWords[j]) > -1) {
	        	return true;
	        }
	    }
	}
    return false;
}
function getTranslation(val){
	val = val.toLowerCase();
	if(val=="elsa" || val=="thank"){
		return "alpha";
	}
	else if(val=="brothel" || val=="bridal"){
		return "bravo";
	}
	else if(val=="sorry" || val=="lee" || val=="sharaley" ||val=="sharley" || val=="charley" || val=="jolly" || val=="sharply" || val=="surely"){
		return "charlie";
	}
	else if(val=="ultra"){
		return "delta";
	}
	else if(val=="eco"){
		return "echo";
	}
	else if(val=="gulf"){
		return "golf";
	}
	else if(val=="tell"){
		return "hotel";
	}
	else if(val=="usually"){
		return "juliet";
	}
	else if(val=="gill" || val=="kill" || val=="jill" || val=="hello" || val=="hero" || val=="deal" || val=="low"){
		return "kilo";
	}
	else if(val=="simon" || val=="i'm" || val=="climate"){
		return "lima";
	}
	else if(val=="my" || val=="micheal"){
		return "mike";
	}
	else if(val=="oskar"){
		return "oscar";
	}
	else if(val=="popular" || val=="poplar" || val=="pop"){
		return "papa";
	}
	else if(val=="callback" || val=="compared" || val=="kebab"){
		return "quebec";
	}
	else if(val=="go"){
		return "tango";
	}
	else if(val=="reform" || val=="forum" || val=="form"){
		return "uniform";
	}
	else if(val=="see"){
		return "sierra";
	}
	else if(val=="nicola" || val=="vector" || val=="director" || val=="miller" || val=="require"){
		return "victor";
	}
	else if(val=="risky" || val=="which"){
		return "whiskey";
	}
	else if(val=="secretary" || val=="explain" || val=="ray" || val=="right"){
		return "x.ray";
	}
	else if(val=="key"){
		return "yankee";
	}
	else if(val=="school" || val=="lou" || val=="loo" ||val=="lu" || val=="loop" || val=="looe" || val=="due"){
		return "zulu";
	}
	else{
		return "";
	}
}