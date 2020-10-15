import os
import sys
import subprocess
import csv


if len(sys.argv) < 1:
    print ('Usage: %s <output-file>' % sys.argv[0])
    sys.exit(1)

api_url_first_half = "https://docs.atlas.mongodb.com"

api_url_sec_half = ["/reference/api/alert-configurations-get-matchers-field-names/",
"/reference/api/alert-configurations-get-all-configs/",
"/reference/api/alert-configurations-create-config/",
"/reference/api/alert-configurations-get-config/",
"/reference/api/alert-configurations-update-config/",
"/reference/api/alert-configurations-enable-disable-config/",
"/reference/api/alert-configurations-delete-config/",
"/reference/api/alert-configurations-get-open-alerts/"
]

api_url_list = []

for sec_half in api_url_sec_half:
	api_url_full = api_url_first_half + sec_half
	api_url_list.append(api_url_full)

fields = ["Application","Title","Collection","Filename","Method","Base Url","Resource","Type","Name","Data Type","Necessity","Description","Default"]

with open(sys.argv[1], 'a') as output:
    writer = csv.writer(output)
    writer.writerow(fields)

for url in api_url_list:
	print(['python', sys.argv[0], url, sys.argv[1]])
	output = subprocess.check_output(['python', 'api-extractor.py', sys.argv[1], url])