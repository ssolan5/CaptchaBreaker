var fs = require('fs');
var value = "";
var fileName = process.argv[2];
//var fileName = "C:/CAPTCHA_SAVED_secureimage/captcha20161127-141351_alt.txt";
var imprecise = 0;

parseJSONInFile();

function parseJSONInFile(){
	fs.readFile(fileName, 'utf-8', function (err, data) {
	  //console.log(data);
	  data = data.substr(0, data.lastIndexOf(","));
	  data = data + ']';
	  transcription = JSON.parse(data);
	  var finalTranscription = "";
	  var wordArray = new Array();
	  var confidence = 0;
	  transcription.forEach(function(value){
			wordArray[0] = ((value.results[0].keywords_result!=undefined)?  Object.keys(value.results[0].keywords_result)[0] : ((value.results[0].alternatives[0]!=null)? JSON.stringify(value.results[0].alternatives[0].transcript) : null));
	  		wordArray[0] = (wordArray[0]==null) ? null : ((wordArray[0].replace(/\"/g, "")).trim());
	  		confidence = (wordArray[0]==null) ? 0 : value.results[0].alternatives[0].confidence;
	  		wordArray[1] = (value.results[0].alternatives[1]!=null)? JSON.stringify(value.results[0].alternatives[1].transcript) : null;
	  		wordArray[1] = (wordArray[1]==null) ? null : ((wordArray[1].replace(/\"/g, "")).trim());
	  		wordArray[2] = (value.results[0].alternatives[2]!=null)? JSON.stringify(value.results[0].alternatives[2].transcript) : null;
	  		wordArray[2] = (wordArray[2]==null) ? null : ((wordArray[2].replace(/\"/g, "")).trim());
	  		wordArray[3] = (value.results[0].alternatives[3]!=null)? JSON.stringify(value.results[0].alternatives[3].transcript) : null;
	  		wordArray[3] = (wordArray[3]==null) ? null : ((wordArray[3].replace(/\"/g, "")).trim());
	  		wordArray[4] = (value.results[0].alternatives[4]!=null)? JSON.stringify(value.results[0].alternatives[4].transcript) : null;
	  		wordArray[4] = (wordArray[4]==null) ? null : ((wordArray[4].replace(/\"/g, "")).trim());
	  		console.log(wordArray);
	  		i = 0;
	  		selected = false;
		  	while(!(isAlphabet(wordArray[i])) && i<wordArray.length-1){
		  		i++;
		  	}
		  	if(i==wordArray.length-1 && selected==false){
		  		
		  	}else{
		  		console.log("word selected" + wordArray[i]);
		  		finalTranscription = finalTranscription + getAlphabet(wordArray[i]);
		  	}
	  });
	  fileName = fileName.substr(0, fileName.lastIndexOf('_')) + '.txt';
	  console.log(finalTranscription);
	  fs.writeFile(fileName, finalTranscription);
	});
}

function isAlphabet(){
	var arg = (Array.prototype.slice.call(arguments, 0))[0];
	if(arg!=null && arg.split(" ").length<3){
		arg = arg.split(" ")[0];
		arg = (arg.charAt(arg.length - 1)=='.') ? arg.substr(0, arg.length - 1) : arg;
		var alphabets = new Array();
		alphabets = ["zero", "row", "one","won" ,"two", "to", "three", "tree", "four", "for", "five", "six", "seven", "eight", "nine" , "a", "bee", "be",  "see", "sea", "de", "e",  "f", "g", "etch", "h", "i", "eye", "jay", "j", "k", "l" ,"am", "m", "n", "o", "pee", "p", "queue", "q", "are", "our", "r", "yes", "s", "tea", "t", "u", "you","ew", "we", "v", "double", "w", "ex", "x", "why", "y", "z"];
		if(arg.length>0){	
			for (var j=0; j<alphabets.length; j++) {
		        if (arg.toLowerCase()==alphabets[j]) {
		        	selected = true;
		        	return true;
		        }
		    }
		}
	}
    return false;
}

function getAlphabet(word){
	returnVal = "";
	if(word!=null){
		word = word.toLowerCase();
		words = word.split(" ");
		words.forEach(function(element){
			if(element.charAt(element.length - 1)=='.'){
				element = element.substr(0, element.length - 1);
			}
			if(element=="hey" || element=="hay" || element=="a"){
				returnVal = returnVal + "a";
			}
			else if(element=="bee" || element=="be" || element=="b"){
				returnVal = returnVal + "b";
			}
			else if(element=="see" || element=="sea" || element=="c"){
				returnVal = returnVal + "c";
			}
			else if(element=="the" || element=="d"){
				returnVal = returnVal + "d";
			}
			else if(element=="he" || element=="e" || element=="eee"){
				returnVal = returnVal + "e";
			}
			else if(element=="f"){
				returnVal = returnVal + "f";
			}
			else if(element=="g"){
				returnVal = returnVal + "g";
			}
			else if(element=="etch" || element=="each" || element=="h"){
				returnVal = returnVal + "h";
			}
			else if(element=="i" || element=="high" || element=="eye"){
				returnVal = returnVal + "i";
			}
			else if(element=="jay" || element=="j"){
				returnVal = returnVal + "j";
			}
			else if(element=="okay" || element=="k"){
				returnVal = returnVal + "k";
			}
			else if(element=="yell" || element=="hell" || element=="l"){
				returnVal = returnVal + "l";
			}
			else if(element=="am" || element=="hem" || element=="m"){
				returnVal = returnVal + "m";
			}
			else if(element=="and" || element=="en" || element=="n"){
				returnVal = returnVal + "n";
			}
			else if(element=="o"){
				returnVal = returnVal + "o";
			}
			else if(element=="pee" || element=="p"){
				returnVal = returnVal + "p";
			}
			else if(element=="queue" || element=="q"){
				returnVal = returnVal + "q";
			}
			else if(element=="are" || element=="r"){
				returnVal = returnVal + "r";
			}
			else if(element=="yes" || element=="s"){
				returnVal = returnVal + "s";
			}
			else if(element=="tea" || element=="t"){
				returnVal = returnVal + "t";
			}
			else if(element=="you" || element=="new"|| element=="u"){
				returnVal = returnVal + "u";
			}
			else if(element=="we" || element=="v"){
				returnVal = returnVal + "v";
			}
			else if(element=="double" || element=="w"){
				returnVal = returnVal + "w";
			}
			else if(element=="ex" || element=="x"){
				returnVal = returnVal + "x";
			}
			else if(element=="why" || element=="y"){
				returnVal = returnVal + "y";
			}
			else if(element=="z"){
				returnVal = returnVal + "z";
			}
			else if(element == "one" || element == "won") {returnVal = returnVal + "1"; }
			else if(element == "two" || element == "to") {returnVal = returnVal + "2"; }
			else if(element == "three" || element == "green" || element == "tree") {returnVal = returnVal + "3"; }
			else if(element == "four" || element =="for") {returnVal = returnVal + "4"; }
			else if(element == "five" || element == "by") {returnVal = returnVal + "5";}
			else if(element == "six") {returnVal = returnVal + "6";}
			else if(element == "seven") {returnVal = returnVal + "7";}
			else if(element == "eight") {returnVal = returnVal + "8";}
			else if(element == "nine") {returnVal = returnVal + "9";}
			else if (element == "zero" || element == "hero" || element == "row") {returnVal = returnVal + "0";}
			else{
				returnVal = returnVal + "z";
			}
		});	
		if(returnVal == "im"){
			returnVal = "m";
		}
	}
	return returnVal;
}