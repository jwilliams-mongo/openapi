import os
import sys
import subprocess


if len(sys.argv) < 1:
    print ('Usage: %s <output-file>' % sys.argv[0])
    sys.exit(1)

api_url_first_half = "https://docs.atlas.mongodb.com"

api_url_sec_half = ["/reference/api/alerts-get-all-alerts",
      "/reference/api/alerts-get-alert",
      "/reference/api/alerts-acknowledge-alert",
      "/reference/api/alert-configurations-get-all-configs",
      "/reference/api/alert-configurations-create-config",
      "/reference/api/alert-configurations-get-config",
      "/reference/api/alert-configurations-update-config",
      "/reference/api/alert-configurations-enable-disable-config",
      "/reference/api/alert-configurations-delete-config",
      "/reference/api/alert-configurations-get-open-alerts",
      "/reference/api/enable-disable-api-key",
      "/reference/api/delete-api-key",
      "/reference/api/apiKeys-orgs-get-all",
      "/reference/api/apiKeys-orgs-get-one",
      "/reference/api/apiKeys-org-whitelist-get-all",
      "/reference/api/apiKeys-org-whitelist-get-one",
      "/reference/api/apiKeys-orgs-create-one",
      "/reference/api/apiKeys-org-whitelist-create",
      "/reference/api/apiKeys-orgs-update-one",
      "/reference/api/apiKeys-org-whitelist-delete-one",
      "/reference/api/apiKey-delete-one-apiKey",
      "/reference/api/auditing-get-auditLog",
      "/reference/api/auditing-set-auditLog",
      "/reference/api/checkpoints-get-all",
      "/reference/api/checkpoints-get-one",
      "/reference/api/cloud-provider-snapshot-get-all",
      "/reference/api/cloud-provider-snapshot-get-one",
      "/reference/api/cloud-provider-snapshot-delete-one",
      "/reference/api/cloud-provider-snapshot-take-one-ondemand",
      "/reference/api/cloud-provider-snapshot-schedule-get-all",
      "/reference/api/cloud-provider-snapshot-schedule-modify-one",
      "/reference/api/cloud-provider-snapshot-restore-jobs-get-all",
      "/reference/api/cloud-provider-snapshot-restore-jobs-get-one",
      "/reference/api/cloud-provider-snapshot-restore-jobs-create-one",
      "/reference/api/cloud-provider-snapshot-restore-jobs-delete-one",
      "/reference/api/clusters-get-all",
      "/reference/api/clusters-get-one",
      "/reference/api/clusters-get-advanced-configuration-options",
      "/reference/api/clusters-create-one",
      "/reference/api/clusters-modify-one",
      "/reference/api/clusters-modify-advanced-configuration-options",
      "/reference/api/clusters-delete-one",
      "/reference/api/custom-roles-get-all-roles",
      "/reference/api/custom-roles-get-single-role",
      "/reference/api/custom-roles-create-a-role",
      "/reference/api/custom-roles-update-a-role",
      "/reference/api/custom-roles-delete-a-role",
      "/reference/api/database-users-get-all-users",
      "/reference/api/database-users-get-single-user",
      "/reference/api/database-users-create-a-user",
      "/reference/api/database-users-update-a-user",
      "/reference/api/database-users-delete-a-user",
      "/reference/api/events-orgs-get-all",
      "/reference/api/events-orgs-get-one",
      "/reference/api/events-projects-get-all",
      "/reference/api/events-projects-get-one",
      "/reference/api/global-clusters-retrieve-namespaces",
      "/reference/api/global-clusters-add-namespace",
      "/reference/api/global-clusters-add-customzonemapping",
      "/reference/api/global-clusters-delete-customzonemappings",
      "/reference/api/organization-get-all-invoices",
      "/reference/api/organization-get-one-invoice",
      "/reference/api/organization-get-pending-invoices",
      "/reference/api/ldaps-configuration-request-verification",
      "/reference/api/ldaps-configuration-verification-status",
      "/reference/api/ldaps-configuration-save",
      "/reference/api/ldaps-configuration-get-current",
      "/reference/api/ldaps-configuration-remove-usertodnmapping",
      "/reference/api/maintenance-windows-view-in-one-project",
      "/reference/api/maintenance-window-update",
      "/reference/api/maintenance-window-defer",
      "/reference/api/maintenance-window-clear",
      "/reference/api/organization-get-all",
      "/reference/api/organization-get-one",
      "/reference/api/organization-users-get-all-users",
      "/reference/api/organization-create-one",
      "/reference/api/organization-rename",
      "/reference/api/organization-delete-one",
      "/reference/api/organization-get-all-projects",
      "/reference/api/pa-namespaces-get-all",
      "/reference/api/pa-existing-indexes-get-all",
      "/reference/api/pa-get-slow-query-logs",
      "/reference/api/pa-suggested-indexes-get-all",
      ]

api_url_list = []

for sec_half in api_url_sec_half:
	api_url_full = api_url_first_half + sec_half
	api_url_list.append(api_url_full)

for url in api_url_list:
	print(['python', sys.argv[0], url, sys.argv[1]])
	output = subprocess.check_output(['python', 'api-extractor.py', sys.argv[1], url])


























