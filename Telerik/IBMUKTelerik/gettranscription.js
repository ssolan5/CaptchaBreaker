var fs = require('fs');
var natural = require('natural');
var metaphone = natural.Metaphone;
var value = "";
var fileName = process.argv[2];
var imprecise = 0;

parseJSONInFile();

function parseJSONInFile(){
	//console.log(fileName);
	fs.readFile(fileName, 'utf-8', function (err, data) {
	  data = data.substr(0, data.lastIndexOf(","));
	  data = data +   ']';
	  //console.log(data);
	  transcription = JSON.parse(data);
	  var finalTranscription = "";
	  transcription.forEach(function(value){
	  		currentWord = (value.results[0].alternatives[0]!=null)? JSON.stringify(value.results[0].alternatives[0].transcript) : null;
	  		currentWord = (currentWord==null) ? null : ((currentWord.replace(/\"/g, "")).trim());
	  		currentWord = currentWord.toLowerCase();
	  		console.log(currentWord);
	  		currentWord = (isNumber(currentWord))? getTextForNumber(currentWord) : getNatoCharacter(value.results[0]);
	  		console.log(currentWord);
	  		finalTranscription = finalTranscription + currentWord;
	  });
	  fileName = fileName.substr(0, fileName.lastIndexOf('_')) + '.txt';
	  //console.log(fileName);
	  fs.writeFile(fileName, finalTranscription);
	});
}

function isNumber(mynumber){
	if(mynumber!=null){
		var numbers = new Array();
		numbers = ["zero", "hero", "row", "so", "sierra", "seirra", "row", "so", "o", "one", "won", "wine", "want", "on", "two", "too", "true", "who", "to", "you","three", "tree", "through", "green", "four", "for", "five", "fine", "eye", "hi", "by", "six", "so", "thank", "see", "seven", "and", "it", "hey", "eight", "at", "yeah", "a", "nine", "right", "now"];
		for (var j=0; j<numbers.length; j++) {
		    if (mynumber == numbers[j]) {
		        return true;
		    }
		}
	}
    return false;
}

function getTextForNumber(number){
	switch(number){
		case "one": return 1;
		case "won": return 1;
		case "wine": return 1;
		case "want": return 1;
		case "on": return 1;
		case "two": return 2;
		case "too": return 2;
		case "true": return 2;
		case "to": return 2;
		case "who": return 2;
		case "three": return 3;
		case "through": return 3;
		case "tree": return 3;
		case "green": return 3;
		case "four": return 4;
		case "for": return 4;
		case "five": return 5;
		case "fine": return 5;
		case "by": return 5;
		case "eye" : return 5;
		case "hi": return 5;
		case "i": return 5;
		case "six": return 6;
		case "sick": return 6;
		case "thank": return 6;
		case "so": return 6;
		case "see": return 6;
		case "seven": return 7;
		case "eight": return 8;
		case "hey": return 8;
		case "it": return 8;
		case "ate": return 8;
		case "at": return 8;
		case "and": return 8;
		case "yeah": return 8;
		case "a": return 8;
		case "nine": return 9;
		case "right": return 9;
		case "now": return 9;
		case "zero": return 0;
		case "hero": return 0;
		case "row": return 0;
		case "so": return 0;
		default: return null;
	}
}

function getNatoCharacter(result){
	var i=0;
	//console.log("I'm here");
	while(result.alternatives[i]!=null && JSON.stringify(result.alternatives[i].transcript)!=null){
		var transcript = JSON.stringify(result.alternatives[i].transcript);
		//console.log(transcript);
		var natoWord = getNatoWord(transcript.replace(/\"/g, "").trim());
		if(natoWord.length>0){
			return natoWord.charAt(0);
		}
		i++;
	}
	return JSON.stringify(result.alternatives[0].transcript).charAt(1);
}
function getNatoWord(myWord){
	console.log(myWord);
	var natoWords = new Array();
	natoWords = ["alfa", "alpha", "bravo", "charlie", "delta", "echo", "foxtrot", "golf", "hotel", "india", "juliette", "juliett", "juliet" , "kilo", "lima", "lyma", "mike", "november", "oscar","oskar", "papa", "quebec", "romeo", "sierra", "tango", "uniform", "new form",  "victor", "whiskey","x.ray", "x", "yankee", "zulu"];
	for (var j=0; j<natoWords.length; j++) {
		//console.log("Sounds like "+ natoWords[j] + " ? : "+metaphone.compare(myWord, natoWords[j]));
		if (myWord.toLowerCase().indexOf(natoWords[j]) > -1){// || metaphone.compare(myWord, natoWords[j])) {
			return natoWords[j];
	    }
	}
	var myWords = myWord.split(" ");
	for(var index in myWords){
		console.log(myWords[index]);
		var result = getSimilarSounds(myWords[index]);
		console.log("found:" + result);
		if(result.length>0){
			return result;
		}
	}
    return "";
}
function getSimilarSounds(val){
	val = val.trim().toLowerCase();
	console.log("Finding similar sounding words for: " + val);
	if(val=="elsa" || val=="okay"){
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
	else if(val=="usually" || val=="you'll" || val=="really"){
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
	else if(val=="popular" || val=="poplar" || val=="pop" || val=="top" || val=="hopper" || val=="post"){
		return "papa";
	}
	else if(val=="callback" || val=="compared" || val=="kebab" || val=="quick"){
		return "quebec";
	}
	else if(val=="o'neil"){
		return "romeo";
	}
	else if(val=="see"){
		return "Sierra";
	}
	else if(val=="go"){
		return "tango";
	}
	else if(val=="reform" || val=="forum" || val=="form"){
		return "uniform";
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
	else if(val=="school" || val=="lou" || val=="loo" ||val=="lu" || val=="loop" || val=="looe" || val=="due" || val=="do" || val=="little"){
		return "zulu";
	}
	else{
		return "";
	}
}