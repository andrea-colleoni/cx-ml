import pyaudio
import numpy as np
import wave
import struct
import matplotlib.pyplot as plt

CHUNK = 4096 # number of data points to read at a time
RATE = 44100 # time resolution of the recording device (Hz)

p=pyaudio.PyAudio() # start the PyAudio class
stream=p.open(format=pyaudio.paInt16,channels=1,rate=RATE,input=True,
              frames_per_buffer=CHUNK) #uses default input device

# create a numpy array holding a single read of audio data
frame=[]; sample=[]; frame2=[];
for i in range(30): #(int(5*RATE/CHUNK)): #do it a few seconds
	data = stream.read(CHUNK)
	data_int=np.fromstring(data, dtype=np.int16)
	data_noise=data_int + np.random.randn(CHUNK)*1000
	sample=np.concatenate([sample, data_noise])
	frame.append(data)
	start_back=''
 	for element in data_noise:
        	start_back += struct.pack('h', element)
	frame2.append(start_back) 
#t=np.linspace(0, CHUNK*25, CHUNK*25)
plt.plot(sample)

#    print(data)

# close the stream gracefully
stream.stop_stream()
stream.close()
p.terminate()

 
waveFile = wave.open("file.wav", 'wb')
waveFile.setnchannels(1)
waveFile.setsampwidth(p.get_sample_size(pyaudio.paInt16))
waveFile.setframerate(RATE)
waveFile.writeframes(b''.join(frame))
waveFile.close()


p=pyaudio.PyAudio() # start the PyAudio class
stream=p.open(format=pyaudio.paInt16,channels=1,rate=RATE,output=True) 
for i in range(30): #(int(5*RATE/CHUNK)): #do it a few seconds
	stream.write(frame2[i])
for i in range(30): #(int(5*RATE/CHUNK)): #do it a few seconds
	stream.write(frame[i])
stream.stop_stream()
stream.close()
p.terminate()

plt.show()