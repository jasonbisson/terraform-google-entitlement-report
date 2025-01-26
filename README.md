# Purpose 

This module will deploy a cloud function that will produce a Google Cloud Infrastructure Entitlement Report. 

### Detailed

The resources/services/activations/deletions that this module will create/trigger are:

- A Cloud function to execute a python script to produce a Google Cloud Infrastructure Entitlement Report

## Architecture
![Reference Architecture](diagram/entitlements.svg)

### Prerequisites

1. Create a User-Managed Service Account on Google Cloud Project

Use the following `gcloud` command to create a service account:

```bash
gcloud iam service-accounts create <SERVICE_ACCOUNT_ID> \
    --display-name "<DISPLAY_NAME>"
```

2. Enable Admin Api on Google Cloud Project 

```
gcloud services enable admin.googleapis.com
```

3. Create a Custom Role in the Admin Console
- Open your web browser and go to admin.google.com.
- Sign in with administrator account.
- Navigate to custom roles:
- In the left-hand navigation menu, go to Account -> Admin roles.
- Click the "Create Role" button.
- Give the role a name (e.g., "Entitlement reporting").
- Optionally, provide a description.
- Assign permissions
- Select the specific read permissions required for entitlement reporting:
- Read Organization
- Read group
- Read user
- Review the permissions you've selected.
- Click the "Create" button.

4. Assign the Service Account to the Custom Role
- In the left-hand navigation menu, go to Account -> Admin roles.
- Find the custom role:
- Locate the custom role that you created (e.g., "Entitlement reporting").
- Assign the service account to the custom role:
- Click on the custom role.
- Click on the "Admins" tab.
- Click the "Assign service accounts" button.
- Enter the service account's email address.
- Click "Add" button.
- Click "Assign role" button.


## Usage

1. Clone repo
```
git clone https://github.com/jasonbisson/terraform-google-entitlement-report.git

```
2. Rename and update required variables in terraform.tvfars.template
```
mv terraform.tfvars.template terraform.tfvars
#Update required variables
```
3. Execute Terraform commands with existing identity (human or service account) to build Infrastructure 

```
terraform init
terraform plan
terraform apply
```

<!-- BEGINNING OF PRE-COMMIT-TERRAFORM DOCS HOOK -->
## Inputs


## Outputs


<!-- END OF PRE-COMMIT-TERRAFORM DOCS HOOK -->

## Requirements

These sections describe requirements for using this module.

### Software

The following dependencies must be available:

- [Terraform][terraform] v0.13
- [Terraform Provider for GCP][terraform-provider-gcp] plugin v3.0

### Service Account

A service account with the following roles must be used to provision
the resources of this module:

- 

### APIs

A project with the following APIs enabled must be used to host the
resources of this module:

- 

## Troubleshooting
Run script with Google Local Application Default Crediatials(https://cloud.google.com/docs/authentication/application-default-credentials) 

```
python ~/terraform-google-entitlement-report/files/cloud_identity_entitlements.py --customer_id <Your Customer ID>

```

Determine the identity autheticating
```
curl -X GET   'https://www.googleapis.com/oauth2/v3/userinfo'   -H "Authorization: Bearer $(gcloud auth print-access-token)"
```

## Contributing

Refer to the [contribution guidelines](./CONTRIBUTING.md) for
information on contributing to this module.


## Security Disclosures

Please see our [security disclosure process](./SECURITY.md).
