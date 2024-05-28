import pathlib

import pyhydrophone as pyhy
import pypam

# Acoustic Data
summary_path = pathlib.Path('./data_summary_example.csv')
include_dirs = False

# Output folder
output_folder = summary_path.parent.joinpath('data_exploration')

# Hydrophone Setup
# If Vpp is 2.0 then it means the wav is -1 to 1 directly related to V
model = 'ST600HF'  #TODO
#model = 'SoundTrap 600'  #TODO
#model = 'SoundTrap600'  #TODO


name = 'SoundTrap' #TODO
serial_number = 0000000X # First element in the wav file name. Most are four digits some 6-7
soundtrap = pyhy.soundtrap.SoundTrap(name=name, model=model, serial_number=serial_number)


#instruments = {'SoundTrap': soundtrap, 'uPam': upam, 'B&K': bk}
instruments = {'SoundTrap': soundtrap}


# SURVEY PARAMETERS
nfft = 4096 # Number of samples?
fft_overlap = 0.5 # How far does windows slide for overlaps. Like a ven diagram.
binsize = 60.0 # Lets assume time in seconds.
bin_overlap = 0.0 # 
# overlap = 0.5 #TODO
dc_subtract = False #TODO
band_lf = [10, 24000] #TODO
band_list = [band_lf] #TODO
temporal_features = ['rms', 'sel', 'aci'] #TODO
frequency_features = ['third_octaves_levels'] #TODO

# Create the dataset object
ds = pypam.dataset.DataSet(summary_path, output_folder, instruments, temporal_features=temporal_features,
                           frequency_features=frequency_features, bands_list=band_list, binsize=binsize,
                           bin_overlap=bin_overlap, nfft=nfft, fft_overlap=fft_overlap, dc_subtract=dc_subtract)

# Call the dataset creation. Will create the files in the corresponding folder
ds()