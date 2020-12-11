from flask import Flask,send_file,send_from_directory
from flask_restful import Api,Resource,reqparse
import sounddevice as sd
import librosa
import uuid

app = Flask(__name__)
app.config["AUDIO_DIR"] = "/home/surya/Desktop/flask/"
api = Api(app)
audio_args=reqparse.RequestParser()
train_args=reqparse.RequestParser()
train_args.add_argument("bse_dir",help="The name of audio file",type=str)
play_audio_args=reqparse.RequestParser()
audio_args.add_argument("text",help="Request does not contain text to generate audio",type=str)
audio_args.add_argument("file_name",default="AudioFile",help="The name of audio file",type=str)
play_audio_args.add_argument("text",help="Request does not contain text to generate audio",required=True)
play_audio_args.add_argument("audio_device",help="On which audio device you want to play the audio",default="default")
class TextToSpeech(Resource):

    #Function to generate audio with given text
    def get(self):
        args=audio_args.parse_args()
        sd.default.samplerate=48000
        audio,_=librosa.load("Audio1.wav",48000)
        response = {"given_text":args['text']}
        
        return send_from_directory(app.config["AUDIO_DIR"],filename=file_name                                                                                                                                                                                                                                                                   ,as_attachment=True)

class PlayAudio(Resource):

    def get(self):
        #args=play_audio_args.parse_args()
        sd.default.device=args['audio_device']
        sd.default.samplerate=48000
        audio,_=librosa.load("Audio1.wav",48000)
        sd.play(audio)

class TrainModel(Resource):

    def get(self):
        #args=play_audio_args.parse_args()
        test_Id="00986-ddsds-54223-vdf-232"
        return {"UUID":test_id}
    
    def post(self):
        args=play_audio_args.parse_args()
        UUID = uuid.uuid4().__str__()
        
        return {"UUID":UUID}


api.add_resource(TextToSpeech,"/audio/file")   
api.add_resource(PlayAudio,"/output/audio")
api.add_resource(TrainModel,"/train")
if __name__=="__main__":
    app.run(debug=True)