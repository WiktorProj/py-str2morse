import array
import math
import time

import pyaudio


morse = ["","",".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
showdebug = str(input("Show debug prints? (Y/N): "))
if showdebug == "Y":
    showdbug = True
else:
    showdbug = False

def Str2Morse(string):
    tablestr = list(string)
    endstrtable = []
    try:
        for i in tablestr:
            if i != " ":
                cletter = int(i, 36) - 8
                if showdbug:
                    print("CHARACTER " + str(cletter - 1) + " (" + i + ") GET")
                endstrtable.append(morse[cletter])
            else:
                if showdbug:
                    print("CHARACTER -1 ( ) GET")
                endstrtable.append("/")
    except ValueError:
        print(f"You inputted a illegal base 36 to base 10 ({i}) character!")
    except:
        print("Plz debug, something is wrong...")
    newstring = " ".join(endstrtable)
    return newstring

while True:
    instring = str(input("Words: "))
    endstr = Str2Morse(instring)
    print(endstr)

    for i in list(endstr):
        p = pyaudio.PyAudio()
        volume = 0.5  # range [0.0, 1.0]
        fs = 44100
        if i == "-":
            duration = 0.5
            if showdbug:
                print("DASH READ")
        elif i == ".":
            duration = 0.2
            if showdbug:
                print("DOT READ")
        else:
            duration = 0
            if showdbug:
                print("NULL READ")
        f = 1000
        num_samples = int(fs * duration)
        samples = [volume * math.sin(2 * math.pi * k * f / fs) for k in range(0, num_samples)]

        output_bytes = array.array('f', samples).tobytes()

        stream = p.open(format=pyaudio.paFloat32,
                        channels=1,
                        rate=fs,
                        output=True)

        start_time = time.time()
        stream.write(output_bytes)

        stream.stop_stream()
        stream.close()

        p.terminate()
    
        
