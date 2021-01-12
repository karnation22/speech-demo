import speech_recognition as sr
import argparse
import os

def main():
    parser = argparse.ArgumentParser(description="Process speech to text..")
    parser.add_argument("wav-file", help="Please input a wavefile.. no default option..")
    args = vars(parser.parse_args())
    if(args['wav-file']==None or args['wav-file'] not in os.listdir() or not(args['wav-file'].endswith(".wav"))):
        print("""Please input an appropriate wavefile 
                (with .wav ending) in the current working directory""")
        return
    else:
        filename = args['wav-file']
        rsr = sr.Recognizer()
        with sr.AudioFile(filename) as source:
            audio = rsr.record(source)
            text = rsr.recognize_google(audio)
            txtfile = filename[:filename.index(".wav")]+".txt"
            with open(txtfile,"w") as f_txt:
                f_txt.write(text)

main()