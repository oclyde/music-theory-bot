# assigning notes to mathematical values
# the value is equal to the number of steps above the root, centered on C
note_values = {
    'C': 0.0, 
    'C#': 0.5, 'Db': 0.5, 
    'D': 1.0, 
    'D#': 1.5, 'Eb': 1.5,
    'E': 2.0,
    'F': 2.5,
    'F#': 3.0, 'Gb': 3.0,
    'G': 3.5,
    'G#': 4.0, 'Ab': 4.0,
    'A': 4.5,
    'A#': 5.0, 'Bb': 5.0,
    'B': 5.5
}

# inversely assigning values to note equivalents
value_notes = {
    0.0: ('C',),
    0.5: ('C#','Db'),
    1.0: ('D',),
    1.5: ('D#','Eb'),
    2.0: ('E',),
    2.5: ('F',),
    3.0: ('F#','Gb'),
    3.5: ('G',),
    4.0: ('G#','Ab'),
    4.5: ('A',),
    5.0: ('A#','Bb'),
    5.5: ('B',)
}

# representing keys as arrays of note values
key_degrees = {
    'MAJOR': [0.0, 1.0, 2.0, 2.5, 3.5, 4.5, 5.5],
    'MINOR': [0.0, 1.0, 1.5, 2.5, 3.5, 4.0, 5.0],
}

# representing modes as arrays of note values
mode_degrees = {
    'IONIAN': [0.0, 1.0, 2.0, 2.5, 3.5, 4.5, 5.5],
    'DORIAN': [0.0, 1.0, 1.5, 2.5, 3.5, 4.5, 5.0],
    'PHRYGIAN': [0.0, 0.5, 1.5, 2.5, 3.5, 4.0, 5.0],
    'LYDIAN': [0.0, 1.0, 2.0, 3.0, 3.5, 4.5, 5.5],
    'MIXOLYDIAN': [0.0, 1.0, 2.0, 2.5, 3.5, 4.5, 5.0],
    'AEOLIAN': [0.0, 1.0, 1.5, 2.5, 3.5, 4.0, 5.0],
    'LOCRIAN': [0.0, 0.5, 1.5, 2.5, 3.0, 4.0, 5.0]
}

# using the circle of fifths to mark major/augmented roots as either sharp (0) or flat (1) keys
major_accidentals = {
    'C': 0,
    'G': 0,
    'D': 0,
    'A': 0,
    'E': 0,
    'B': 0,
    'F#': 0,
    'C#': 0,
    'G#': 0,
    'D#': 0,
    'A#': 0,
    'F': 1,
    'Bb': 1,
    'Eb': 1,
    'Ab': 1,
    'Db': 1,
    'Gb': 1
}

# using the circle of fifths to mark minor/diminished roots as either sharp (0) or flat (1) keys
minor_accidentals = {
    'E': 0,
    'B': 0,
    'F#': 0,
    'C#': 0,
    'G#': 0,
    'D#': 0,
    'A#': 0,
    'A': 1,
    'D': 1,
    'G': 1,
    'C': 1,
    'F': 1,
    'Bb': 1,
    'Eb': 1,
    'Ab': 1,
    'Db': 1,
    'Gb': 1
}

# creating a class to work with keys
class Key:
    # initializing the key with a root and quality
    def __init__(self, root, quality):
        self.root = root
        self.quality = quality

    # returning the modes in the key
    def get_modes(self):
        # calculating the interval between the root and C
        interval = note_values[self.root]
        # creating an array of values representing the notes in the key
        values = [degree + interval if degree + interval <= 5.5 else degree + interval - 6 for degree in key_degrees[self.quality]]
        # translating the values into the notes associated with the key
        key_notes = []
        for value in values:
            for note_value in value_notes:
                if note_value == value:
                    # appends the equivalent note if there are no accidentals
                    if len(value_notes[note_value]) == 1:
                        key_notes.append(value_notes[note_value][0])
                    # appends the equivalent note with an accidental based on quality and key
                    elif len(value_notes[note_value]) == 2 and (self.quality == 'MAJOR'):
                        key_notes.append(value_notes[note_value][major_accidentals[self.root]])
                    elif len(value_notes[note_value]) == 2 and (self.quality == 'MINOR'):
                        key_notes.append(value_notes[note_value][minor_accidentals[self.root]])
        # creating an array of notes assigned to modes as strings
        degree_modes = []
        mode_list = list(mode_degrees.keys())
        for i in range(7):
            if self.quality == 'MAJOR':
                degree_modes.append(f'{key_notes[i]} {mode_list[i].lower().capitalize()}')
            if self.quality == 'MINOR':
                degree_modes.append(f'{key_notes[i]} {mode_list[i-2].lower().capitalize()}')
        # creating an array of the scales associated with each mode
        mode_notes = []
        mode_scale = key_notes
        for i in range(7):
            mode_scale_string = ' '.join(mode_scale)
            mode_notes.append(mode_scale_string)
            mode_scale.append(mode_scale.pop(0))
        # combining the two arrays
        modes = list(zip(degree_modes,mode_notes))
        return modes

# runs indefinitely until requested to stop
active = True
while active:
    # getting key root note with error-checking
    root = input("Root: ").lower().capitalize()
    while root not in note_values:
        root = input("Invalid response. Root: ").lower().capitalize()
    # getting key quality with error-checking
    quality = input("Quality: ").upper()
    while quality not in key_degrees:
        quality = input("Invalid response. Quality: ").upper()
    # using an instance of the Key class to print the modes
    key = Key(root, quality)
    modes = key.get_modes()
    for tuple in modes:
        print(f'{tuple[0]}:\t{tuple[1]}')
    # checking if the user wants to enter another chord
    activity = input("Would you like to enter another key? (Y/N) ").upper()
    while activity != 'Y' and activity != 'N':
        activity = input("Invalid response. Would you like to enter another key? (Y/N) ").upper()
    if activity == 'N':
        active = False
