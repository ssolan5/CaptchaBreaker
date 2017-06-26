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
	  		finalTranscription = finalTranscription + getAlphabet(word);
	  });
	  fs.writeFile(fileName, finalTranscription);
	});
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
			else if(element == "one") {returnVal = returnVal + "1"; }
			else if(element == "two" || element == "to") {returnVal = returnVal + "2"; }
			else if(element == "three") {returnVal = returnVal + "3"; }
			else if(element == "four" || element =="for") {returnVal = returnVal + "4"; }
			else if(element == "five") {returnVal = returnVal + "5";}
			else if(element == "six") {returnVal = returnVal + "6";}
			else if(element == "eight") {returnVal = returnVal + "8";}
			else if(element == "nine") {returnVal = returnVal + "9";}
			else if (element == "zero") {returnVal = returnVal + "0";}
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