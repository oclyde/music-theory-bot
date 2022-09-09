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

# representing chord qualities as arrays of note values
chord_degrees = {
    'MAJOR': [0.0, 2.0, 3.5, 5.5],
    'MINOR': [0.0, 1.5, 3.5, 5.0],
    'DIMINISHED': [0.0, 1.5, 3.0, 4.5],
    'AUGMENTED': [0.0, 2.0, 4.0, 5.0]
}

# using the circle of fifths to mark major/augmented roots as either sharp (0) or flat (1) keys
major_augmented_accidentals = {
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
minor_diminished_accidentals = {
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

# creating a class to work with chords
class Chord:
    # initializing the chord with a root and quality
    def __init__(self, root, quality):
        self.root = root
        self.quality = quality
    
    # returning the notes in the chord
    def get_notes(self):
        # calculating the interval between the root and C
        interval = note_values[self.root]
        # creating an array of values representing the notes in the chord
        values = [degree + interval if degree + interval <= 5.5 else degree + interval - 6 for degree in chord_degrees[self.quality]]
        # creating an array of notes corresponding to the array of values
        notes = []
        for value in values:
            for note_value in value_notes:
                if value == note_value:
                    # appends the equivalent note if there are no accidentals
                    if len(value_notes[note_value]) == 1:
                        notes.append(value_notes[note_value][0])
                    # appends the equivalent note with an accidental based on quality and key
                    elif len(value_notes[note_value]) == 2 and (self.quality == 'MAJOR' or self.quality == 'AUGMENTED'):
                        notes.append(value_notes[note_value][major_augmented_accidentals[self.root]])
                    elif len(value_notes[note_value]) == 2 and (self.quality == 'MINOR' or self.quality == 'DIMINISHED'):
                        notes.append(value_notes[note_value][minor_diminished_accidentals[self.root]])
        return notes

# runs indefinitely until requested to stop
active = True
while active:
    # getting root note with error-checking
    root = input("Root: ").lower().capitalize()
    while root not in note_values:
        root = input("Invalid response. Root: ").lower().capitalize()
    # getting chord quality with error-checking
    quality = input("Quality: ").upper()
    while quality not in chord_degrees:
        quality = input("Invalid response. Quality: ").upper()
    # using an instance of the Chord class to print the notes
    chord = Chord(root, quality)
    notes = chord.get_notes()
    print(notes[0], notes[1], notes[2], notes[3])
    # checking if the user wants to enter another chord
    activity = input("Would you like to enter another chord? (Y/N) ").upper()
    while activity != 'Y' and activity != 'N':
        activity = input("Invalid response. Would you like to enter another chord? (Y/N) ").upper()
    if activity == 'N':
        active = False
