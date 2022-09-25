
import AudioFileToText as Audio

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

isSelected = False
isSelected2 = False
print(bcolors.HEADER + "Hello to Voice to Text. \n This script will help you write your documents more efficiently and fast. \n To get started, enter the number of the option you want to use" + bcolors.ENDC)
try:
    while isSelected == False:
        print(bcolors.WARNING + "1 - use Microphone" + bcolors.ENDC)
        print(bcolors.WARNING + "2 - use .wav File" + bcolors.ENDC)
        op = input(bcolors.UNDERLINE + "Option: " + bcolors.ENDC)
        if op == "1":
            isSelected = True
            print(bcolors.OKGREEN + "Start Talking!"  + bcolors.ENDC)
            Audio.UseMicrophone()                
        elif op == "2":                     
            while isSelected2 == False:
                print(bcolors.WARNING + "1 - use Short text" + bcolors.ENDC)
                print(bcolors.WARNING + "2 - use Long Text" + bcolors.ENDC)
                op2 = input(bcolors.UNDERLINE + "Option: " + bcolors.ENDC)
                if op2 == "1":
                    isSelected2 = True
                    audioFile = input(bcolors.UNDERLINE + "Path to the .wav file: " + bcolors.ENDC)
                    ##  Audio Samples/audio1.wav
                    ##Audio.SetAudioFileName(audioFile)
                    Audio.audioFilename = audioFile
                    Audio.StartShortAudioToText()
                elif op2 == "2":
                    isSelected2 = True
                    audioFile = input(bcolors.UNDERLINE + "Path to the .wav file: " + bcolors.ENDC)
                    ##  /Audio Samples/audio1.wav
                    ##Audio.SetAudioFileName(audioFile)
                    Audio.audioFilename = audioFile
                    Audio.StartLongAudioToText()
                else:
                    print(bcolors.FAIL + "Enter only numbers of the menu" + bcolors.ENDC)                      
            isSelected = True                 
        else:
            print(bcolors.FAIL + "Enter only numbers of the menu" + bcolors.ENDC)
            
except Exception as e: 
    print(e)