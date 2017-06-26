var watson = require('watson-developer-cloud');
var fs = require('fs');

convertSpeechToText();

function convertSpeechToText(){
	var speech_to_text = watson.speech_to_text({
	  username: 'afc7c517-af64-482c-9118-60b67d525a60',
	  password: '3iisOz7I60DY',
	  version: 'v1',
	});

	var params = {
	  content_type: 'audio/wav',
	  continuous: true,
	  interim_results: true,
	  model: 'en-UK_NarrowbandModel',
	  max_alternatives: 5
	};

	// Create the stream.
	var recognizeStream = speech_to_text.createRecognizeStream(params);

	// Pipe in the audio.
	fs.createReadStream(process.argv[2]).pipe(recognizeStream);

	filename = (process.argv[2]).substr(0, process.argv[2].indexOf('.'));
	// Pipe out the transcription to a file.
	recognizeStream.pipe(fs.createWriteStream(filename + '.txt'), { 'flags' : 'w'});

	// Get strings instead of buffers from 'data' events.
	recognizeStream.setEncoding('utf8');

	count = 1;
	fs.appendFile(filename + '_alt.txt', '[');

	// Listen for events.
	//recognizeStream.on('data', function(event) { onEvent('Data:', event); });
	recognizeStream.on('results', function(event) { onEvent('Results:', event); });
	recognizeStream.on('error', function(event) { onEvent('Error:', event); });
	recognizeStream.on('close-connection', function(event) { onEvent('Close:', event); });
}
// Writes events to file.
function onEvent(name, event) {
	fs.appendFile(filename + '_alt.txt','\r\n');
	fs.appendFile(filename + '_alt.txt', JSON.stringify(event, null, 2) + ",", function (err) {

	});
	count++;
}  