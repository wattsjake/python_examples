import matplotlib.pyplot as plt
import numpy as np
import sounddevice as sd
import time
import keyboard

sps = 44100
duration_s = 2

def plot_graph(x,y):
    plt.plot(x,y)
    plt.xlim(0,10000)
    plt.ylim(-2,2)
    plt.show()
    
def wave_form(freq,atten):
    if freq == 0:
        return 0
    T = freq**-1
    print("Freq: %.3f Period: %.3f" %(freq,T))
    x = np.arange(duration_s*sps)
    waveform = (np.sin(2*np.pi*x*freq/sps)*atten)
    return waveform

wav1 = wave_form(1209, 0.1)
wav2 = wave_form(852, 0.1)
wav3 = wave_form(0,0.1)
wav4 = wave_form(0,0.5)

waveform = wav1 + wav2 + wav3 + wav4
y = np.arange(duration_s*sps)
plot_graph(y, waveform)



# Play the waveform out the speakers
sd.play(waveform, sps, loop=True)
time.sleep(duration_s)
sd.stop()




