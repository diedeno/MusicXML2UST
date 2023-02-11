from MusicXMLPaser.MusicXMLPaser import MusicXMLDocument
from USTPaser.USTPaser import USTPaser

import argparse


def main(path):
    tempos = 120
    score_parser = MusicXMLDocument(path)
    for tempo in score_parser.get_tempos():
        tempos = tempo.qpm

    xml_data = []
    i = 1
    for part in score_parser.parts:
        for measure in part.measures:
            for note in measure.notes:
                xml_data.insert(i, note.get_note())
                i += i

    return USTPaser(xml_data, tempos).get_ust()


if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print('MusicXML To UST Ver 0.2'
              '\nLicensed under the Apache License, Version 2.0 (the "License");'
              '\nyou may not use this file except in compliance with the License.'
              '\nYou may obtain a copy of the License at'
              '\nhttp://www.apache.org/licenses/LICENSE-2.0'
              '\nusage: main [-h] [-i INPUT]')
    else:
        parser = argparse.ArgumentParser()
        parser.add_argument('-i', '--input', default=None, type=str, help='path to MusicXML (default: None)')
        # TODO: Convert all files in a folder
        # parser.add_argument('-d', '--dir', default=None, type=str, help='path to MusicXML directory (default: None)')

        args = parser.parse_args()
        with open(args.input[0: len(args.input) - 3] + 'ust', mode='w') as f:
            f.write(main(args.input))

        print('Conversion Complete, File: ' + args.input)
