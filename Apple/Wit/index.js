var witai_speech = require('witai-speech');
var fs = require('fs');
var filename = process.argv[2];
var results_filename = (filename.substr(0, process.argv[2].indexOf('.'))) + '.txt';


var ACCESS_TOKEN = "NB6G6M5TIHFFJT5R5BQC5K73FK5RNXLQ";

witai_speech.ASR({
  file: filename, 
  developer_key: ACCESS_TOKEN
  }, function (err, res) {
    var towrite = res._text;
    console.log(res._text);
    fs.appendFile(results_filename , towrite, { flag: 'w' }, function(err) {
        if(err) {
            return console.log(err);
        }
        console.log("The file was saved!");
    }); 
});
