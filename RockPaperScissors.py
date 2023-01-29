import random

h=input('chose [r]ock , [p]aper, [s]cissors: ')
c=random.choice(['r','p','s'])

if h not in ['r','p','s']:
    raise SystemExit('invalid input, try again')
print(f'computer choose: {c}')
if h=='r' and c=='s' or h=='s' and c=='p' or h=='p' and c=='r': print('you win')
elif h==c: print('draw')
else: print('you lose')