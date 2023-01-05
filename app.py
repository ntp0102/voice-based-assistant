from flask import Flask, render_template, request, redirect, url_for, session
import json
from gtts import gTTS
import playsound
# from nltk_utils import bag_of_words, tokenize
from chat import chat_bot
import os
from random import randint
import string
from responses import response


global output, input_text, link_extend, bot_audio, thu_tuc
output = ""
input_text = ""
link_extend = [["", ""]]
bot_audio = ""
thu_tuc = [""]

# check file .mp3 in previous execution errors
dir_path = os.path.dirname(os.path.realpath(__file__))
for root, dirs, files in os.walk(dir_path):
    for file in files:
        if file.endswith('.mp3'):
            os.remove(root+'/'+str(file))


def text_to_speech(text):
    output = gTTS(text, lang="vi", slow=False)
    filename = str(randint(0, 10000))+"output"+str(randint(0, 10000))+".mp3"
    output.save(filename)
    playsound.playsound(filename, True)
    os.remove(filename)


app = Flask(__name__)
logic = 0


@app.route('/', methods=['POST', 'GET'])
def index():
    global logic
    logic += 1
    print(output)
    print(input_text)
    print('Nhay qua ham Index')

    return render_template('index.html', logic=logic, output=output, input_text=input_text,
                           bot_audio=bot_audio, thu_tuc=thu_tuc, link_extend=link_extend)


@app.route('/text', methods=['POST'])
def send_text():
    global output, input_text, bot_audio, thu_tuc, link_extend
    input_text = request.get_json()
    input_text.rstrip(string.punctuation)
    print(input_text)
    if len(input_text) == 2:
        print("Input text error", input_text)
        bot_audio = "Tôi chưa nghe rõ. Mời bạn nói lại."
        print("bot_audio ", bot_audio)
        text_to_speech(bot_audio)
        bot_audio = ""
    else:
        print("Input text ", input_text)
        print("Type input_text ", type(input_text))
        print(len(input_text))
        output = chat_bot(input_text)
        if output == "not understand":
            text_to_speech("Vấn đề này tôi chưa rõ lắm")
            bot_audio = ""
            thu_tuc = [""]
            link_extend = [["", ""]]

        else:
            bot_audio, thu_tuc, link_extend = response(output)
            print("bot_audio ", bot_audio)
            text_to_speech(bot_audio)
    return redirect(url_for('index'))

@app.route('/search_tag', methods=['POST'])
def search_tag():
    global output, input_text, bot_audio, thu_tuc, link_extend
    input_text = request.get_json()
    input_text.rstrip(string.punctuation)
    print(input_text)
    # if len(input_text) == 2:
    #     print("Input text error", input_text)
    #     bot_audio = "Tôi chưa nghe rõ. Mời bạn nói lại."
    #     print("bot_audio ", bot_audio)
    #     text_to_speech(bot_audio)
    #     bot_audio = ""
    # else:
    print("Input text ", input_text)
    print("Type input_text ", type(input_text))
    print(len(input_text))
    output = chat_bot(input_text)
    if output == "not understand":
        text_to_speech("Vấn đề này tôi chưa rõ lắm")
        bot_audio = ""
        thu_tuc = [""]
        link_extend = [["", ""]]

    else:
        bot_audio, thu_tuc, link_extend = response(output)
        print("bot_audio ", bot_audio)
        text_to_speech(bot_audio)
    return redirect(url_for('index'))

@app.route('/bieumau')
def bieumau():
    return render_template('bieumau.html')


if __name__ == "__main__":
    app.jinja_env.auto_reload = True
    app.config["TEMPLATES_AUTO_RELOAD"] = True
    app.run(debug=True, threaded=True)
