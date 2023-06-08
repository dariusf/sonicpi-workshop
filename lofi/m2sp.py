#!/usr/bin/env python

import music21
import sys
import re

def translate(file):
  for elt in music21.converter.parse(file).recurse():
    if isinstance(elt, music21.chord.Chord):

      name = f':{elt[0].name.lower()}{elt[0].octave}'
      name = re.sub('-', 'b', name)
      name = re.sub('#', 's', name)

      cname = elt.pitchedCommonName
      doubt = False
      if 'minor-ninth' in cname:
        qual = ':m9, '
      elif 'minor seventh' in cname:
        qual = ':m7, '
      elif 'dominant-seventh' in cname:
        qual = ':dom7, '
      elif 'major seventh' in cname:
        qual = '"7", '
      elif 'major-ninth' in cname:
        qual = ':maj9, '
      elif 'minor' in cname:
        qual = ':minor, '
      elif 'major' in cname:
        qual = ''
      else:
        # if in doubt, use m9
        qual = ':m9, '
        doubt = True

      if doubt:
        doubt = ' (?)'
      else:
        doubt = ''

      print(f'# {cname}{doubt}')
      print(f'play (chord {name}, {qual}num_octaves: 2)')
      print('sleep 2')
    else:
      # print(type(elt))
      pass

if __name__ == "__main__":
  d = sys.argv[1]
  print('# LoFi\n')
  print("Try the drum samples above and chord progressions below in your work!\n")
  print('Credit: [chords](https://www.youtube.com/watch?v=S5UsIl2JIhY), [samples](https://www.edmprod.com/lofi-hip-hop/)\n')
  for file in range(1, 21):
    print(f'## Chord progression {file}\n')
    print('```ruby')
    translate(f'{d}/{file}.mid')
    print('```\n')
