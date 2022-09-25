
import AudioFileToText as Audio

isSelected = False
isSelected2 = False
print("Hello to Voice to Text. \n This script will help you write your documents more efficiently and fast. \n To get started, enter the number of the option you want to use")
try:
    while isSelected == False:
        print("1 - use Microphone")
        print("2 - use .wav File")
        op = input("option: ")
        if op == "1":
            print("2")
            isSelected = True
                        
        elif op == "2":                     
            while isSelected2 == False:
                print("1 - use Short text")
                print("2 - use Long Text")
                op2 = input("option: ")
                if op2 == "1":
                    isSelected2 = True
                    audioFile = input("Path to the .wav file: ")
                    ##  Audio Samples/audio1.wav
                    ##Audio.SetAudioFileName(audioFile)
                    Audio.audioFilename = audioFile
                    Audio.StartShortAudioToText()
                elif op2 == "2":
                    isSelected2 = True
                    audioFile = input("Path to the .wav file: ")
                    ##  /Audio Samples/audio1.wav
                    ##Audio.SetAudioFileName(audioFile)
                    Audio.audioFilename = audioFile
                    Audio.StartLongAudioToText()
                else:
                    print("Enter only numbers")                      
            isSelected = True                 
        else:
            print("Enter only numbers")
            
except Exception as e: 
    print(e)