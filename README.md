# MongoDB Cloud API Docs Extractor

The MongoDB API Docs Extractor uses Beautiful Soup to crawl the MongoDB
Cloud REST API documentation and extract details about each public API
endpoint's fields in `csv` format.

This is an evolution of the original extractor implementation, located
[here](https://github.com/tahiyachowdhury/openapi).

This repository contains three product-specific scripts:

- `extract-all-api-doc-atlas.py` for Atlas
- `extract-all-api-doc-om.py` for Ops Manager
- `extract-all-api-doc-cm.py` for Cloud Manager

Each of these scripts searches a local build of that MongoDB docs for
that product to determine which API endpoints the documentation
contains. For each endpoint the product-specific script finds, it
invokes the core extractor, `api-extractor.py`.

For each endpoint, the core extractor:

1. Writes the raw details for an endpoint into a temporary csv
   file,`temp.csv`.
2. Appends details for the endpoint to the output `csv` file.
3. Removes the `temp.csv` file.

## Prerequisites

1. The product-specific scripts assume that you have cloned the MongoDB
   Cloud Docs repositories to a `projects` directory in your home
   directory:

   ```
   ~/projects/cloud-docs
   ~/projects/mms-docs
   ```

   If you have cloned the MongoDB Cloud Docs repositories to different
   directories, modify the `path` variable in each product-specific script,
   as appropriate:

   ```
   # update to match absolute path to api files in your cloud-docs build directory
   path = home + '/path/to/repos/cloud-docs/build/master/html/reference/api'
   ```

2. Run the `setup.py` script:

   ```
   python3 setup.py
   ```

   This script uses `pip3` to install the Python modules that the MongoDB API Docs Extractor requires.

## Run the Scripts

1. For the product whose API docs you want to extract, check out the
`master` branch and pull down the latest from upstream.

   ```
   $ git checkout master
   $ git pull --rebase upstream master
   ```

2. **For Atlas docs only**: Configure your local repository to use the
legacy build tools. 

   In `worker.sh`, Comment out `"build-and-stage-next-gen"`, then save the file.

   ```
   #"build-and-stage-next-gen"
   ```

3. Build and stage the docs:

   ```
   $ make html && make stage
   ```

4. Run the extraction script for the product whose API docs you want to extract:

   **IMPORTANT**: Don't name the output file `test.csv`.

   For Atlas:

   ```
   $ python extract-all-api-doc-atlas.py <output-file-name>.csv
   ```

   For Ops Manager:

   ```
   $ python extract-all-api-doc-om.py <output-file-name>.csv
   ```

   For Cloud Manager:

   ```
   $ python extract-all-api-doc-cm.py <output-file-name>.csv
   ```

   The script's output is written to the terminal. It should take 10-20
   minutes to complete.

5. **For Atlas docs only**: In `worker.sh`, uncomment
   `"build-and-stage-next-gen"` to re-enable the NextGen build, then
   save the file.

   ```
   "build-and-stage-next-gen"
   ```

## Sample Output

   ```
   $ cat om.csv

   Application,Title,Collection,Filename,Method,Base Url,Resource,Type,Name,Data Type,Necessity,Description,Default
   Ops Manager,Create One Backup Daemon Configuration,Backup Daemon Configurations,https://docs-opsmanager-staging.mongodb.com/john.williams/master/reference/api/admin/backup/daemonConfigs/create-one-backup-daemon-configuration.html,PUT,https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0/admin/backup,/admin/backup/daemon/configs/{MACHINE},Path Param,MACHINE,string,Required,Hostname or IP address of the machine that serves the Backup Daemon.,
   Ops Manager,Create One Backup Daemon Configuration,Backup Daemon Configurations,https://docs-opsmanager-staging.mongodb.com/john.williams/master/reference/api/admin/backup/daemonConfigs/create-one-backup-daemon-configuration.html,PUT,https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0/admin/backup,/admin/backup/daemon/configs/{MACHINE},Query Param,pretty,boolean,Optional,Flag indicating whether the response body should be in a prettyprint format.,false
   Ops Manager,Create One Backup Daemon Configuration,Backup Daemon Configurations,https://docs-opsmanager-staging.mongodb.com/john.williams/master/reference/api/admin/backup/daemonConfigs/create-one-backup-daemon-configuration.html,PUT,https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0/admin/backup,/admin/backup/daemon/configs/{MACHINE},Query Param,envelope,boolean,Optional,"Flag that indicates whether or not to wrap the response in an envelope. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. For endpoints that return one result, the response body includes: Name Description status HTTP response code envelope Expected response body",false
   Ops Manager,Create One Backup Daemon Configuration,Backup Daemon Configurations,https://docs-opsmanager-staging.mongodb.com/john.williams/master/reference/api/admin/backup/daemonConfigs/create-one-backup-daemon-configuration.html,PUT,https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0/admin/backup,/admin/backup/daemon/configs/{MACHINE},Body Param,assignmentEnabled,boolean,Optional,Flag indicating whether this Backup Daemon can be assigned backup jobs.,
   Ops Manager,Create One Backup Daemon Configuration,Backup Daemon Configurations,https://docs-opsmanager-staging.mongodb.com/john.williams/master/reference/api/admin/backup/daemonConfigs/create-one-backup-daemon-configuration.html,PUT,https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0/admin/backup,/admin/backup/daemon/configs/{MACHINE},Body Param,backupJobsEnabled,boolean,Optional,Flag indicating whether this Backup Daemon can be used to backup databases.,

   ...
   ```

## Troubleshooting

For each endpoint, the extraction script for each MongoDB Cloud product
invokes the core extractor, `api-extractor.py`.

If your receive an error, run the core extractor against the endpoint
that failed to get detailed error information:

```
$ python api-extractor.py error-test.csv https://<url>/reference/api/ssh-keys.html
```
