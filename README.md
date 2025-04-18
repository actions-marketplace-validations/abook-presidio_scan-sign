# scan-sign

This is the repository for the **Scan and Sign** Github plugin

You can use this plugin action for the following:

- Scanning your containers for:
  - vulnerabilties
  - secrets
  - malware
  - sensitive data

If it passes all of the scans then it will move on to the signature phase of the action.

# Prerequisites

- a **WiZ** service account [ Client ID / Client Secret Key ]
- The following secrets stored securely in your pipeline
  - 'WIZ_CLIENT_ID'
  - 'WIZ_SECRET_ID'
- a cloud provider [ AWS or Azure ]
  - 'CLOUD'
- an account id [ either an AWS account id OR an Azure subscription id ]
  - 'ACCOUNT'
- a Linux runner (Ubuntu, Debian, etc.)

# Usage

The following block shows how to use the plugin in a github action

```yaml
- name: "scan and sign plugin"
  uses: abook-presidio/sign-sign@alpha10
  with:
  #variables to pass
  CLOUD: "AWS"
  ACCOUNT: "123456789012"
  WIZ_CLIENT_ID: ${{ secrets.WIZ_CLIENT_ID }}
  WIZ_CLIENT_SECRET: ${{ secrets.WIZ_CLIENT_SECRET }}
```
