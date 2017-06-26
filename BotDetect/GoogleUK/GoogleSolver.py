import urllib, urllib.request ,re , csv, sys, contextlib, datetime, pydub, os, argparse, base64, json, httplib2,ssl
from googleapiclient import discovery
from oauth2client.client import GoogleCredentials
from oauth2client.service_account import ServiceAccountCredentials

scopes = ['https://www.googleapis.com/auth/sqlservice.admin']


# [START authenticating]
DISCOVERY_URL = ('https://{api}.googleapis.com/$discovery/rest?'
                 'version={apiVersion}')


# Application default credentials provided by env variable
# GOOGLE_APPLICATION_CREDENTIALS
def get_speech_service():
    
    credentials = GoogleCredentials.get_application_default().create_scoped(
        ['https://www.googleapis.com/auth/cloud-platform'])
    
    
    #credentials = ServiceAccountCredentials.from_json_keyfile_name(
    #'/home/smo/Downloads/My First Project-5b808f67cea3.json', scopes=scopes)
    http = httplib2.Http()
    credentials.authorize(http)

    return discovery.build(
        'speech', 'v1beta1', http=http, discoveryServiceUrl=DISCOVERY_URL)
# [END authenticating]

def replaceAlphaNum(x):
    x = x.lower()
    if x[len(x) - 1] == '.' or x[len(x) - 1] == ',' or x[len(x) - 1] == '?':
        x = x[0:len(x) - 1]
    if x == 'hey' or x == 'hay' or x == 'a':
        return 'a'
    elif x == 'bee' or x == 'be' or x == 'b':
        return 'b'
    elif x == 'see' or x == 'sea' or x == 'c':
        return 'c'
    elif x == 'the' or x == 'd':
        return 'd'
    elif x == 'he' or x == 'e' or x == 'eee':
        return 'e'
    elif x == 'f':
        return 'f'
    elif x == 'g':
        return 'g'
    elif x == 'etch' or x == 'each' or x == 'h':
        return 'h'
    elif x == 'i' or x == 'high' or x == 'eye':
        return 'i'
    elif x == 'jay' or x == 'j':
        return 'j'
    elif x == 'okay' or x == 'k':
        return 'k'
    elif x == 'yell' or x == 'hell' or x == 'l':
        return 'l'
    elif x == 'am' or x == 'hem' or x == 'm':
        return 'm'
    elif x == 'en' or x=='&' or x=='and' or x == 'n':
        return 'n'
    elif x == 'o':
        return 'o'
    elif x == 'pee' or x == 'p':
        return 'p'
    elif x == 'queue' or x == 'q':
        return 'q'
    elif x == 'more' or x=='far' or x == 'or' or x == 'are' or x == 'r':
        return 'r'
    elif x == 'yes' or x == 's':
        return 's'
    elif x == 'teams' or x == 'team' or x == 'tea' or x == 't':
        return 't'
    elif x == 'you' or x == 'new' or x == 'u':
        return 'u'
    elif x == 'we' or x == 'v':
        return 'v'
    elif x == 'double' or x == 'w':
        return 'w'
    elif x == 'ex' or x == 'x':
        return 'x'
    elif x == 'why' or x == 'y':
        return 'y'
    elif x == 'z':
        return 'z'
    elif x=='1' or x == 'one' or x == 'once':
        return 1
    elif x=='2' or x == 'two' or x == 'screw' or x == 'school' or x == 'scoop' or x =='scoops':
        return 2
    elif x=='3' or x == 'three' or x == 'free' or x == 'tree' or x == 'ring':
        return 3
    elif x=='4' or x == 'four' or x == 'for' or x == 'source' or x == 'horse' or x =='store':
        return 4
    elif x=='5' or x=='hi' or x=='bye' or x == 'five' or x == 'by' or x == 'size' or x == 'spice' or x == 'slice' or x == 'side':
        return 5
    elif x=='6' or x=='this' or x == 'six' or x == 'if' or x == 'first' or x == 'books' or x == 'sick' or x =='stilts' or x == 'suits' or x == 'sex' or x == 'stick' or x == 'sticks' or x == 'speak' or x == 'street'  or x == 'streets' or x == 'strip' or x == 'strips' or x == 'step' or x == 'steps':
        return 6
    elif x=='7' or x == 'seven' or x == 'devon' or x == 'star' or x == 'stomach' or x == 'stomachs':
        return 7
    elif x=='8' or x == 'faith' or x == 'fate' or x == 'hate' or x == 'eight':
        return 8
    elif x=='8' or x == 'eight' or x == 'eighth' or x == 'eighths' or x == 'fate' or x == 'hate' or x == 'feet' or x =='store':
        return 8
    elif x=='9' or x == 'nine' or x == 'know' or  x == 'life' or x == 'night' or x == 'site':
        return 9
    else:
        return ''


def hasNumbers(inputString):
      return any(char.isdigit() for char in inputString)

global content

def transcribe(speech_file, samplerate):
    """Transcribe the given audio file.

    Args:
        speech_file: the name of the audio file.
    """
    # [START construct_request]
    with open(speech_file, 'rb') as speech:
        # Base64 encode the binary audio file for inclusion in the JSON
        # request.
        speech_content = base64.b64encode(speech.read())

    service = get_speech_service()
    service_request = service.speech().syncrecognize(
        body={
            'config': {
                # There are a bunch of config options you can specify. See
                # https://goo.gl/KPZn97 for the full list.
                'encoding': 'FLAC',  # raw 16-bit signed LE samples
                'sampleRate': samplerate,  # 16 khz
                # See http://g.co/cloud/speech/docs/languages for a list of
                # supported languages.
                'languageCode': 'en-UK',  # a BCP-47 language tag
                'speechContext': {
                        "phrases": [
                            "one","two","three","four","five","six","seven","eight","nine","ten", "tree","sex","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"
                            "1","2","3","4","5","6","7","8","9"
                        ]

                }
            },
            'audio': {
                'content': speech_content.decode('UTF-8')
            }
        })
    # [END construct_request]
    # [START send_request]
    response = service_request.execute()
    print(json.dumps(response))
    j = json.dumps(response)
    j = json.loads(j)

    resulttext = ""
    if j == {} :
        return resulttext

    for result in j['results']:
        s = result['alternatives'][0]['transcript']

        w = s.split()
        for res in w:
            res = res.strip()
            print(res)
            res = replaceAlphaNum(res)
            res = str(res).lower()
            resulttext += str(res)


    print(resulttext)
    return resulttext
    # [END send_request]