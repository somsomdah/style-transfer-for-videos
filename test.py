


import sys

print('Number of arguments: {}'.format(len(sys.argv)))
print('Argument(s) passed: {}'.format(str(sys.argv)))


import os
for file in os.listdir(os.path.join(os.path.dirname(__file__),"./samples")):
     print(file)
