import argparse
import os
import tempfile
import json

parser = argparse.ArgumentParser()
parser.add_argument("--key")
parser.add_argument("--val")
args = parser.parse_args()

#storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
storage_path = "dict.txt"

if args.val != None: # input data to file
    with open(storage_path, 'a') as f:
    	data = {'key': args.key, 'val': args.val}
        f.write(json.dumps(data) + '\n')

else: # output data
    if not os.path.isfile(storage_path): # create file
        f = open(storage_path, 'w')
        f.close()
    answer = []
    with open(storage_path, 'r') as f:
        for line in f:
            from_json_line = json.loads(line.strip())
            if from_json_line['key'] == args.key:
                answer.append(from_json_line['val'])

    print(', '.join(answer))