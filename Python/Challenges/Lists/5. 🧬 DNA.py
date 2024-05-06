dna_sequence = [
  'GCT', 'AGC', 'AGG',
  'TAA', 'ACT', 'CAT',
  'TAT', 'CCC', 'ACG',
  'GAA', 'ACC', 'GGA'
  ]

item_to_find = 'CCC'

item_found = False

for item in dna_sequence:
  if item == item_to_find:
    item_found = True
    break

if item_found:    
  print('Item Found!')
else:
  print('Item not found.')