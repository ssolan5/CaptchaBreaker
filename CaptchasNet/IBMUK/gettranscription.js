var fs = require('fs');
var fileName = process.argv[2];
getTranscription();

function getTranscription(){
	console.log(fileName);
	var finalTranscription = "";

	var data = fs.readFileSync(fileName, 'utf8');
		console.log("hey"+data);
		data = eliminateNonNatoWords(data);
		console.log("Final:" + data);
		finalTranscription = getFirstAlphabets(data);

	//fileName = fileName.substr(0, fileName.lastIndexOf('_')) + '.txt';
	fs.writeFile(fileName, finalTranscription);
}

function getFirstAlphabets(value){
	var returnValue = "";
	if(value.length>0){
		var words = value.split(" ");
		for(var i=0; i<words.length; i++){
			returnValue = returnValue + words[i].charAt(0);
		}
	}
	return returnValue;
}

function eliminateNonNatoWords(value){
	var words = new Array();
	words = value.split(" ");
	var result = "";
	if(words.length>0){
		for(var i=0; i<words.length; i++){
			if(isNatoWord(words[i])){
				result = result + " " + words[i];
				result = result.toLowerCase().trim();
			}else{
				result = result + " " + getTranslation(words[i]);
				result = result.toLowerCase().trim();
			}
			//console.log("a:" + result);
		}
		result = result.trim();
		return result;
	}
	return value;
}
function isNatoWord(){
	var arg = (Array.prototype.slice.call(arguments, 0))[0];
	arg = arg.trim().toLowerCase();
	if(arg!=null && arg!=undefined){
		var natoWords = new Array();
		natoWords = ["alfa", "alpha", "bravo", "charlie", "delta", "echo", "foxtrot", "golf", "hotel", "india", "juliett", "juliet" , "kilo", "lima", "mike", "november", "oscar","oskar", "papa", "quebec", "romeo", "sierra", "tango", "uniform", "new form",  "victor", "whiskey","x-ray", "yankee", "zulu"];
		if(arg.length>0){	
			for (var j=0; j<natoWords.length; j++) {
		        if (arg.toLowerCase().indexOf(natoWords[j]) > -1) {
		        	return true;		        }
		    } 
		}
	}
    return false;
}
function getTranslation(val){
	console.log("Finding similar sounding words for: " + val);
	val = val.trim().toLowerCase();
	if(val=="elsa" || val=="thank"){
		return "alpha";
	}
	else if(val=="brothel" || val=="bridal" || val=="bramhall"){
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
	else if(val=="see" || val=="yeah"){
		return "Sierra";
	}
	else if(val=="nicola" || val=="vector" || val=="director" || val=="miller" || val=="require"){
		return "victor";
	}
	else if(val=="risky"){
		return "whiskey";
	}
	else if(val=="secretary" || val=="explain"){
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