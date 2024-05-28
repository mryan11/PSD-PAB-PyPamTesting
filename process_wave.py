from pypam import acoustic_file
import pyhydrophone as pyhy

# SoundTrap
model = 'ST600HF'
name = 'SoundTrap'
serial_number = 5459
soundtrap = pyhy.soundtrap.SoundTrap(name=name, model=model, serial_number=serial_number)
print()
acu_file = acoustic_file.AcuFile('/wave_files/5459_20220118_052541.wav', soundtrap, 1)
acu_file.plot_spectrum_per_chunk()

nfft = 8000  # Set to the same as sampling rate (or higher band limit, when downsampling) for 1s time resolution
acu_file.hybrid_millidecade_bands(nfft=nfft, fft_overlap=0.5, binsize=None, bin_overlap=0, db=True, method='density', band=None)