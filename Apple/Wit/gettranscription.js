var fs = require('fs');
var WtoN = require('words-to-num');
var value = "";
var fileName = process.argv[2];

parseJSONInFile();

function parseJSONInFile(){
	//console.log(fileName);
	finalTranscription = "";
	fs.readFile(fileName, 'utf-8', function (err, data) {
	  finalTranscription = getDigits(data);
	  fs.writeFile(fileName, finalTranscription);
	});
}

function getDigits(data){
    var finalTranscription = "";
    if(data!=null && data.length>0){
        data = data.trim().toLowerCase();
        var words = new Array();
        words = data.split(" ");
        for(var i=0; i<words.length; i++){
            if(words[i]=="ten" || words[i]=="eleven" || words[i]=="twelve" || words[i]=="thirteen" || words[i]=="fourteen" || words[i]=="fifteen" || words[i]=="sixteen" || words[i]=="seventeen" || words[i]=="eighteen" || words[i]=="nineteen"){
                finalTranscription += WtoN.convert(words[i])
            }else if(words[i]=="twenty" || words[i]=="thirty" || words[i]=="forty" || words[i]=="fifty" || words[i]=="sixty" || words[i]=="seventy" || words[i]=="eighty" || words[i]=="ninety"){
                if(findSimilarWords(words[i+1]).length> 0 || words[i+1]=="one" || words[i+1]=="two" || words[i+1]=="three" || words[i+1]=="four" || words[i+1]=="five" || words[i+1]=="six" || words[i+1]=="seven" || words[i+1]=="eight" || words[i+1]=="nine"){
                    finalTranscription += WtoN.convert(words[i] + " " + words[i+1]);
                    i = i+1;
                }else{
                    finalTranscription += WtoN.convert(words[i]);
                }
            }else if(words[i]=="one" || words[i] == "two" || words[i]=="three" || words[i] == "four" || words[i]=="five" || words[i] == "six" || words[i]=="seven" || words[i] == "eight" || words[i]=="nine"){
                finalTranscription +=WtoN.convert(words[i]);
            }
            else{
                var similar = findSimilarWords(words[i]);
                finalTranscription += (similar.length>0)? WtoN.convert(similar) : "";
            }
        }
    }
    return finalTranscription;
}

function findSimilarWords(word){
    var value = "";
    if(word=="won" || word =="wine" || word=="war" || word =="want" || word=="what" || word =="on" || word=="bomb"){
        value = "one";
    }else if (word=="too" || word =="to" || word=="true" || word =="who" || word=="you"){
        value = "two";
    }else if (word=="three" || word =="through" || word=="tree" || word =="free" || word=="he" || word=="very" || word=="green"){
        value = "three";
    }else if (word=="for" || word =="full"){
        value = "four";
    }else if (word=="fine" || word =="hi" || word=="high" || word =="right" || word=="i" || word=="bye" || word=="eye"){
        value = "five";
    }else if (word =="sick" || word=="sex" || word =="ex"){
        value = "six";
    }else if (word=="seven" || word =="several" || word=="then"){
        value = "seven";
    }else if (word=="hey" || word =="ate" || word=="at"){
        value = "eight";
    }else if (word=="not" || word=="right" || word=="now" || word=="none"){
        value = "nine";
    }else if(word=="well"){
        value = "twelve";
    }
    else{}
    return value;
}