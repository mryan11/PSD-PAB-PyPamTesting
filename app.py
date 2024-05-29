import pyhydrophone as pyhy

# SoundTrap
model = 'SoundTrap 300 STD'
name = 'SoundTrap'
serial_number = 67416073
soundtrap = pyhy.soundtrap.SoundTrap(name=name, model=model, serial_number=serial_number)

print("Hello World! I am a SoundTrap hydrophone.")