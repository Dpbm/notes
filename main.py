notes = ["Do", "Do#", "Re", "Re#", "Mi", "Fa", "Fa#", "Sol", "Sol#", "La", "La#", "Si"]
guitar_notes_sequence = ["Mi", "Si", "Sol", "Re", "La", "Mi"]

frackles = 19

for note in guitar_notes_sequence:
    result = (f'{note}').ljust(3, ' ') + '|'

    actual_note = notes.index(note) + 1

    for frackle in range(frackles):
   
        if(actual_note >= len(notes)): actual_note = 0
        
        ajusted_note = (f' {notes[actual_note]} ').ljust(6, ' ') + (' . ' if frackle < frackles-1 else '')

        result += ajusted_note
        actual_note += 1

    print(result)
