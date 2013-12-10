import pyaudio
import wave
import struct
import numpy as np
import array
import pyaudio

CHUNK = 8820

wf = wave.open('song_files/test.wav', 'rb')
data = wf.readframes(2)
frames = []
while data != '': 
	frames.append(data)
	data = wf.readframes(2)

f = ''.join(frames)
nums = array.array('h', f)
nums = nums[:len(nums)-len(nums)%(2*CHUNK)]
chnks = np.array(nums).reshape(len(nums)/CHUNK,CHUNK)

ft = [np.abs(np.fft.fft(chnk)) for chnk in chnks]
freqs = [44100 * np.argmax(samp[:2000]) / CHUNK for samp in ft]
notes = [freq2note(f) for f in freqs]

def note2freq(n): return 2 ** (float(i-49)/12) * 440
def freq2note(f): return int(np.log2(float(f) / 440) * 12 + 49)

notes = [freq2note(f) for f in freqs]

p = pyaudio.PyAudio()
# open stream (2)
stream = p.open(format=8,
                channels=1,
                rate=44100,
                output=True)



'''	
for chnk in chnks:
	x = ''.join([struct.pack('h',n) for n in chnk])
	stream.write(x)

def phase_align(clip,pad):
	def align_front(clip):
		first0 = np.min(np.nonzero(np.abs(clip[:pad]) < 50)[0])
		clip[:pad] = np.interp(np.linspace(0, pad-first0, num=pad), np.arange(pad-first0),clip[first0:pad])
		return clip
	clip = align_front(clip)
	return align_front(clip[::-1])[::-1]
	
'''	
	






	
	
'''