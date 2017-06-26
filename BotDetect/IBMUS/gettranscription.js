var fs = require('fs');
var WtoN = require('words-to-num');
var fileName = process.argv[2];
getTranscription();

function getTranscription(){
	console.log(fileName);
	var finalTranscription = "";

	var data = fs.readFileSync(fileName, 'utf8');
		console.log("hey" + data);
		finalTranscription = getAlphaNum(data);
		console.log(finalTranscription);

	fs.writeFile(fileName, finalTranscription);
}

function getAlphaNum(data){
    var finalTranscription = "";
    if(data!=null && data.length>0){
        data = data.trim().toLowerCase();
        var words = new Array();
        words = data.split(" ");
        console.log(words);
        for(var i=0; i<words.length; i++){
            var value = findSimilarWords(words[i]);
            console.log(value);
            if(value.length>0){
                finalTranscription = finalTranscription + value;
            }
        }
    }
    return finalTranscription;
}

function findSimilarWords(word){
    var value = "";
    if(word.charAt(word.length - 1)=='.'){
		word = word.substr(0, word.length - 1);
	}
	if(word=="hey" || word=="hay" || word=="a"){
		value = "a";
	}else if(word=="bee" || word=="be" || word=="b"){
		value = "b";
	}else if(word=="see" || word=="sea" || word=="c"){
		value = "c";
	}else if(word=="the" || word=="d"){
		value = "d";
	}else if(word=="he" || word=="e" || word=="eee"){
		value = "e";
	}else if(word=="f"){
		value = "f";
	}else if(word=="g"){
		value = "g";
	}else if(word=="etch" || word=="each" || word=="h"){
	    value = "h";
	}else if(word=="i" || word=="high" || word=="eye"){
		value = "i";
	}else if(word=="jay" || word=="j"){
		value = "j";
	}else if(word=="okay" || word=="k"){
		value = "k";
	}else if(word=="yell" || word=="hell" || word=="l"){
		value = "l";
	}else if(word=="am" || word=="hem" || word=="m"){
		value = "m";
	}else if(word=="and" || word=="en" || word=="n"){
	    value = "n";
	}else if(word=="o"){
		value = "o";
	}else if(word=="pee" || word=="p"){
		value = "p";
	}else if(word=="queue" || word=="q"){
		value = "q";
	}else if(word=="more" || word=="are" || word=="r"){
		value = "r";
	}else if(word=="yes" || word=="s"){
		value = "s";
	}else if(word=="tea" || word=="t"){
		value = "t";
	}else if(word=="you" || word=="new"|| word=="u"){
		value = "u";
	}else if(word=="we" || word=="v"){
		value = "v";
	}else if(word=="double" || word=="w"){
		value = "w";
	}else if(word=="ex" || word=="x"){
		value = "x";
	}else if(word=="why" || word=="y"){
		value = "y";
	}else if(word=="z"){
		value = "z";
	}else if(word=="won" || word =="wine" || word=="war" || word =="want" || word=="what" || word =="on" || word=="bomb" || word=="one"){
        value = "1";
    }else if (word=="too" || word =="to" || word=="true" || word =="who" || word=="you" || word=="two"){
        value = "2";
    }else if (word=="three" || word =="through" || word=="tree" || word =="free" || word=="he" || word=="very" || word=="green" || word=="three"){
        value = "3";
    }else if (word=="for" || word =="full" || word=="four"){
        value = "4";
    }else if (word=="fine" || word =="hi" || word=="high" || word =="right" || word=="i" || word=="bye" || word=="eye" || word=="five"){
        value = "5";
    }else if (word =="sick" || word=="sex" || word =="ex" || word=="six"){
        value = "6";
    }else if (word=="seven" || word =="several" || word=="then" || word=="seven"){
        value = "7";
    }else if (word=="hey" || word =="ate" || word=="at" || word=="eight"){
        value = "8";
    }else if (word=="not" || word=="right" || word=="now" || word=="none" || word=="nine"){
        value = "9";
    }
    else{
    }
    return value;
}