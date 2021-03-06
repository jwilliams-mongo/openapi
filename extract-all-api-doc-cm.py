import os
from glob import glob
import sys
import getpass
import subprocess
import csv
from pathlib import Path 

if len(sys.argv) < 1:
    print ('Usage: %s <output-file>' % sys.argv[0])
    sys.exit(1)

username = getpass.getuser()
home = str(Path.home())

api_url_first_half = 'https://docs-cloudmanager-staging.mongodb.com/' + username + '/master/reference/api'

# update to match absolute path to cloud manager api files in your mms-docs build directory
path = home + '/projects/mms-docs/build/master/html-cloud/reference/api'

api_file_list = [y for x in os.walk(path) for y in glob(os.path.join(x[0], '*.html'))]

api_url_sec_half = []
for fn in api_file_list:
  api_url = fn[len(path):]
  # adding case for abandoned(?) ssh-keys page
  if api_url != '/ssh-keys.html':
    api_url_sec_half.append(api_url)

api_url_list = []

for sec_half in api_url_sec_half:
 	api_url_full = api_url_first_half + sec_half
 	api_url_list.append(api_url_full)

api_url_list.sort()

fields = ["Application","Title","Collection","Filename","Method","Base Url","Resource","Type","Name","Data Type","Necessity","Description","Default"]

with open(sys.argv[1], 'a') as output:
    writer = csv.writer(output)
    writer.writerow(fields)

for url in api_url_list:
	print(['python', sys.argv[0], url, sys.argv[1]])
	output = subprocess.check_output(['python', 'api-extractor.py', sys.argv[1], url])
