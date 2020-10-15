import os
import sys
import subprocess
import csv


if len(sys.argv) < 1:
    print ('Usage: %s <output-file>' % sys.argv[0])
    sys.exit(1)

api_url_first_half = "https://docs.atlas.mongodb.com"

api_url_sec_half = [
# root

"/reference/api/access-lists",
"/reference/api/access-tracking-get-database-history-clustername",
"/reference/api/access-tracking-get-database-history-hostname",
"/reference/api/access-tracking",
"/reference/api/alert-configurations-create-config",
"/reference/api/alert-configurations-delete-config",
"/reference/api/alert-configurations-enable-disable-config",
"/reference/api/alert-configurations-get-all-configs",
"/reference/api/alert-configurations-get-config",
"/reference/api/alert-configurations-get-matchers-field-names",
"/reference/api/alert-configurations-get-open-alerts",
"/reference/api/alert-configurations-update-config",
"/reference/api/alert-configurations",
"/reference/api/alerts-acknowledge-alert",
"/reference/api/alerts-get-alert",
"/reference/api/alerts-get-all-alerts",
"/reference/api/alerts",
"/reference/api/api-errors",
"/reference/api/api-key-get-all",
"/reference/api/api-key",
"/reference/api/apiKey-delete-one-apiKey",
"/reference/api/apiKeys-org-whitelist-create",
"/reference/api/apiKeys-org-whitelist-delete-one",
"/reference/api/apiKeys-org-whitelist-get-all",
"/reference/api/apiKeys-org-whitelist-get-one",
"/reference/api/apiKeys-orgs-create-one",
"/reference/api/apiKeys-orgs-get-all",
"/reference/api/apiKeys-orgs-get-one",
"/reference/api/apiKeys-orgs-update-one",
"/reference/api/apiKeys",
"/reference/api/atlas-search",
"/reference/api/auditing-get-auditLog",
"/reference/api/auditing-set-auditLog",
"/reference/api/auditing",
"/reference/api/aws-custom-dns-get",
"/reference/api/aws-custom-dns-update",
"/reference/api/aws-custom-dns",
"/reference/api/checkpoints-get-all",
"/reference/api/checkpoints-get-one",
"/reference/api/checkpoints",
"/reference/api/cloud-provider-access-authorize-one-role",
"/reference/api/cloud-provider-access-create-one-role",
"/reference/api/cloud-provider-access-deauthorize-one-role",
"/reference/api/cloud-provider-access-get-roles",
"/reference/api/cloud-provider-access",
"/reference/api/clusters-check-operation-status",
"/reference/api/clusters-create-one",
"/reference/api/clusters-delete-one",
"/reference/api/clusters-get-advanced-configuration-options",
"/reference/api/clusters-get-all-key",
"/reference/api/clusters-get-all",
"/reference/api/clusters-get-one",
"/reference/api/clusters-modify-advanced-configuration-options",
"/reference/api/clusters-modify-one",
"/reference/api/clusters-test-failover",
"/reference/api/clusters",
"/reference/api/custom-role-actions",
"/reference/api/custom-roles-create-a-role",
"/reference/api/custom-roles-delete-a-role",
"/reference/api/custom-roles-get-all-roles",
"/reference/api/custom-roles-get-single-role",
"/reference/api/custom-roles-update-a-role",
"/reference/api/custom-roles",
"/reference/api/database-users-create-a-user",
"/reference/api/database-users-delete-a-user",
"/reference/api/database-users-get-all-users",
"/reference/api/database-users-get-single-user",
"/reference/api/database-users-update-a-user",
"/reference/api/database-users",
"/reference/api/delete-api-key",
"/reference/api/enable-configure-encryptionatrest",
"/reference/api/enable-disable-api-key",
"/reference/api/encryption-at-rest",
"/reference/api/events-orgs-get-all",
"/reference/api/events-orgs-get-one",
"/reference/api/events-projects-get-all",
"/reference/api/events-projects-get-one",
"/reference/api/events",
"/reference/api/fts-analyzers-get-all",
"/reference/api/fts-analyzers-update-all",
"/reference/api/fts-indexes-create-one",
"/reference/api/fts-indexes-delete-one",
"/reference/api/fts-indexes-get-all",
"/reference/api/fts-indexes-get-one",
"/reference/api/fts-indexes-update-one",
"/reference/api/get-configuration-encryptionatrest",
"/reference/api/get-private-ip-mode-for-project",
"/reference/api/global-clusters-add-customzonemapping",
"/reference/api/global-clusters-add-namespace",
"/reference/api/global-clusters-delete-customzonemappings",
"/reference/api/global-clusters-delete-namespace",
"/reference/api/global-clusters-retrieve-namespaces",
"/reference/api/global-clusters",
"/reference/api/indexes",
"/reference/api/invoices",
"/reference/api/ldaps-configuration-get-current",
"/reference/api/ldaps-configuration-remove-usertodnmapping",
"/reference/api/ldaps-configuration-request-verification",
"/reference/api/ldaps-configuration-save",
"/reference/api/ldaps-configuration-verification-status",
"/reference/api/ldaps-configuration",
"/reference/api/logs",
"/reference/api/maintenance-window-clear",
"/reference/api/maintenance-window-defer",
"/reference/api/maintenance-window-update",
"/reference/api/maintenance-windows-view-in-one-project",
"/reference/api/maintenance-windows",
"/reference/api/monitoring-and-logs",
"/reference/api/online-archive-create-one",
"/reference/api/online-archive-delete-one",
"/reference/api/online-archive-get-all-for-cluster",
"/reference/api/online-archive-get-one",
"/reference/api/online-archive-update-one",
"/reference/api/online-archive",
"/reference/api/organization-delete-one",
"/reference/api/organization-get-all-invoices",
"/reference/api/organization-get-all-projects",
"/reference/api/organization-get-all",
"/reference/api/organization-get-one-invoice",
"/reference/api/organization-get-one",
"/reference/api/organization-get-pending-invoices",
"/reference/api/organization-rename",
"/reference/api/organization-users-get-all-users",
"/reference/api/organizations",
"/reference/api/pa-get-slow-query-logs",
"/reference/api/pa-namespaces-get-all",
"/reference/api/pa-suggested-indexes-get-all",
"/reference/api/performance-advisor",
"/reference/api/private-endpoint-create-one-interface-endpoint",
"/reference/api/private-endpoint-create-one-private-endpoint-connection",
"/reference/api/private-endpoint-delete-one-interface-endpoint",
"/reference/api/private-endpoint-delete-one-private-endpoint-connection",
"/reference/api/private-endpoint-get-all-private-endpoint-connections",
"/reference/api/private-endpoint-get-one-interface-endpoint",
"/reference/api/private-endpoint-get-one-private-endpoint-connection",
"/reference/api/private-endpoint",
"/reference/api/private-endpoints-endpoint-create-one",
"/reference/api/private-endpoints-endpoint-delete-one",
"/reference/api/private-endpoints-endpoint-get-one",
"/reference/api/private-endpoints-service-create-one",
"/reference/api/private-endpoints-service-delete-one",
"/reference/api/private-endpoints-service-get-all",
"/reference/api/private-endpoints-service-get-one",
"/reference/api/private-endpoints",
"/reference/api/process-databases-measurements",
"/reference/api/process-databases",
"/reference/api/process-disks-measurements",
"/reference/api/process-disks",
"/reference/api/process-measurements",
"/reference/api/processes-get-all",
"/reference/api/processes-get-one",
"/reference/api/project-add-team",
"/reference/api/project-create-one",
"/reference/api/project-delete-one",
"/reference/api/project-get-all",
"/reference/api/project-get-one-by-name",
"/reference/api/project-get-one",
"/reference/api/project-get-teams",
"/reference/api/project-remove-user",
"/reference/api/projects",
"/reference/api/rolling-index-create-one",
"/reference/api/root",
"/reference/api/set-private-ip-mode-for-project",
"/reference/api/teams-add-user",
"/reference/api/teams-create-one",
"/reference/api/teams-delete-one",
"/reference/api/teams-get-all-users",
"/reference/api/teams-get-all",
"/reference/api/teams-get-one-by-id",
"/reference/api/teams-get-one-by-name",
"/reference/api/teams-remove-from-project",
"/reference/api/teams-remove-user",
"/reference/api/teams-rename-one",
"/reference/api/teams-update-roles",
"/reference/api/teams",
"/reference/api/third-party-integration-settings-create",
"/reference/api/third-party-integration-settings-delete",
"/reference/api/third-party-integration-settings-get-all",
"/reference/api/third-party-integration-settings-get-one",
"/reference/api/third-party-integration-settings-update",
"/reference/api/third-party-integration-settings",
"/reference/api/user-create",
"/reference/api/user-get-all",
"/reference/api/user-get-by-id",
"/reference/api/user-get-one-by-name",
"/reference/api/user-update",
"/reference/api/user",
"/reference/api/vpc-create-container",
"/reference/api/vpc-create-peering-connection",
"/reference/api/vpc-delete-one-container",
"/reference/api/vpc-delete-peering-connection",
"/reference/api/vpc-get-connection",
"/reference/api/vpc-get-connections-list",
"/reference/api/vpc-get-container",
"/reference/api/vpc-get-containers-list-all",
"/reference/api/vpc-get-containers-list",
"/reference/api/vpc-update-container",
"/reference/api/vpc-update-peering-connection",
"/reference/api/vpc",
"/reference/api/whitelist-add-one",
"/reference/api/whitelist-api",
"/reference/api/whitelist-delete-one",
"/reference/api/whitelist-get-all",
"/reference/api/whitelist-get-one-entry",
"/reference/api/whitelist",
"/reference/api/x509-configuration-create-certificate",
"/reference/api/x509-configuration-disable-advanced",
"/reference/api/x509-configuration-get-certificates",
"/reference/api/x509-configuration-get-current",
"/reference/api/x509-configuration-save",
"/reference/api/x509-configuration",

# /cloud-backup/backup

"/reference/api/cloud-backup/backup/backups",
"/reference/api/cloud-backup/backup/delete-one-backup",
"/reference/api/cloud-backup/backup/get-all-backups",
"/reference/api/cloud-backup/backup/get-one-backup",
"/reference/api/cloud-backup/backup/take-one-ondemand-backup",

# /cloud-backup/restore

"/reference/api/cloud-backup/restore/create-one-restore-job",
"/reference/api/cloud-backup/restore/delete-one-restore-job",
"/reference/api/cloud-backup/restore/get-all-restore-jobs",
"/reference/api/cloud-backup/restore/get-one-restore-job",
"/reference/api/cloud-backup/restore/restores",

# /cloud-backup/schedule

"/reference/api/cloud-backup/schedule/get-all-schedules",
"/reference/api/cloud-backup/schedule/modify-one-schedule",
"/reference/api/cloud-backup/schedule/schedules",

# /ip-access-list

"/reference/api/ip-access-list/add-entries-to-access-list",
"/reference/api/ip-access-list/delete-one-access-list-entry",
"/reference/api/ip-access-list/get-all-access-list-entries",
"/reference/api/ip-access-list/get-one-access-list-entry",

# /legacy-backup/backup

"/reference/api/legacy-backup/backup/backups",
"/reference/api/legacy-backup/backup/change-one-snapshot-expiration",
"/reference/api/legacy-backup/backup/delete-one-snapshot",
"/reference/api/legacy-backup/backup/get-all-snapshots",
"/reference/api/legacy-backup/backup/get-one-snapshot",

# /legacy-backup/restore

"/reference/api/legacy-backup/restore/create-one-restore-job",
"/reference/api/legacy-backup/restore/get-all-restore-jobs",
"/reference/api/legacy-backup/restore/get-one-restore-job",
"/reference/api/legacy-backup/restore/restores",

# /legacy-backup/schedule

"/reference/api/legacy-backup/schedule/get-schedule",
"/reference/api/legacy-backup/schedule/patch-schedule",
"/reference/api/legacy-backup/schedule/schedules",

# /projectApiKeys

"/reference/api/projectApiKeys/assign-one-org-apiKey-to-one-project",
"/reference/api/projectApiKeys/create-one-apiKey-in-one-project",
"/reference/api/projectApiKeys/delete-one-apiKey-in-one-project",
"/reference/api/projectApiKeys/get-all-apiKeys-in-one-project",
"/reference/api/projectApiKeys/update-one-apiKey-in-one-project",

# /shared-backup/backup

"/reference/api/shared-backup/backup/backups",
"/reference/api/shared-backup/backup/download-one-snapshot",
"/reference/api/shared-backup/backup/get-all-snapshots",
"/reference/api/shared-backup/backup/get-one-snapshot",

# /shared-backup/restore

"/reference/api/shared-backup/restore/create-one-restore-job",
"/reference/api/shared-backup/restore/get-all-restore-jobs",
"/reference/api/shared-backup/restore/get-one-restore-job",
"/reference/api/shared-backup/restore/restores"
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
