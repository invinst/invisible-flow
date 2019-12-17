import os
import json

credfile = open('googleCred.json', 'w')
creds = str(os.environ.get('TEMP'))
json.dump(json.loads(creds), credfile)
credfile.close()
