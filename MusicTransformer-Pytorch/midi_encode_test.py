import third_party.midi_processor.processor as mp
import pretty_midi

def encode_midi(file_path):
    events = []
    notes = []
    mid = pretty_midi.PrettyMIDI(midi_file=file_path)

    for inst in mid.instruments:
        inst_notes = inst.notes
        # ctrl.number is the number of sustain control. If you want to know abour the number type of control,
        # see https://www.midi.org/specifications-old/item/table-3-control-change-messages-data-bytes-2
        ctrls = mp._control_preprocess([ctrl for ctrl in inst.control_changes if ctrl.number == 64])
        #print("notes", ctrls)
        #print("notes", inst_notes)
        notes += mp._note_preprocess(ctrls, inst_notes)

    #print("notes", notes)
    #print("instruments", mid.instruments[0].notes)
    dnotes = mp._divide_note(notes)

    # print(dnotes)
    dnotes.sort(key=lambda x: x.time)
    # print('sorted:')
    # print(dnotes)
    cur_time = 0
    cur_vel = 0
    for snote in dnotes:
        events += mp._make_time_sift_events(prev_time=cur_time, post_time=snote.time)
        events += mp._snote2events(snote=snote, prev_vel=cur_vel)
        # events += _make_time_sift_events(prev_time=cur_time, post_time=snote.time)

        cur_time = snote.time
        cur_vel = snote.velocity

    return [e.to_int() for e in events]

filepath = '../midiFill/data/AceAttorney/471.midi'
# 471 is empty
# 2494 is not empty
encoded = encode_midi(filepath)

decoded = mp.decode_midi(encoded)
decoded.write("471.midi")