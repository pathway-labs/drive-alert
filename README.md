# Build a real-time alerting app with Pathway

This repo demontrates how to build real-time alerts in your [LLM app](https://github.com/pathwaycom/llm-app). The app reacts to document changes in [Google Docs](https://www.google.com/docs/about/) and sends notifications to [Slack](https://slack.com/) when some relevant information is modified. Read more in this article: [Use LLMs for notifications](https://pathway.com/developers/showcases/llm-alert-pathway/)

## How to run the project

Follow the steps to install and get started using the sample app.

### Step 1: Open the project

Choose one of these environments to open the project:

1. [GitHub Codespaces](#open-in-github-codespaces).

2. [VS Code Dev Containers](#open-in-dev-container).

3. [Local environment](#open-in-local-environment).

#### Open in GitHub Codespaces

Click here to open in GitHub Codespaces

[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=GitHub+Codespaces&message=Open&color=lightgrey&logo=github)](https://codespaces.new/pathway-labs/drive-alert)

#### Open in Dev Container

Click here to open in Dev Container

[![Open in Dev Container](https://img.shields.io/static/v1?style=for-the-badge&label=Dev+Container&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/pathway-labs/drive-alert)

#### Open in Local environment

##### Prerequisites

1. Make sure that [Python](https://www.python.org/downloads/) 3.10 or above installed on your machine.
2. Download and Install [Pip](https://pip.pypa.io/en/stable/installation/) to manage project packages.

### Step 2: Create a new project in the Google API console

Before running the app, you will need to give the app access to the Google Drive folder, we follow the steps below.

In order to access files on your Google Drive from the Pathway app, you will need a Google Cloud project and a service user.

- Go to [https://console.cloud.google.com/projectcreate](https://console.cloud.google.com/projectcreate) and create new project
- Enable Google Drive API by going to [https://console.cloud.google.com/apis/library/drive.googleapis.com](https://console.cloud.google.com/apis/library/drive.googleapis.com), make sure the newly created project is selected in the top left corner
- Configure consent screen:
  - Go to [https://console.cloud.google.com/apis/credentials/consent](https://console.cloud.google.com/apis/credentials/consent)
  - If using a private Gmail, select "External", and go next.
  - Fill required parameters: application name, user support, and developer email (your email is fine)
  - On the next screen click "Add or remove scopes" search for "drive.readonly" and select this scope
  - Save and click through other steps
- Create service user:

  - Go to [https://console.cloud.google.com/apis/credentials](https://console.cloud.google.com/apis/credentials)
  - Click "+ Create credentials" and create a service account
  - Name the service user and click through the next steps
- Generate service user key:
  - Once more go to [https://console.cloud.google.com/apis/credentials](https://console.cloud.google.com/apis/credentials) and click on your newly created user (under Service Accounts)
  - Go to "Keys", click "Add key" -> "Create new key" -> "JSON"
  
  A JSON file will be saved to your computer.

Rename this JSON file to `secrets.json` and put it under `examples/pipelines/drive_alert` next to `app.py` so that it is easily reachable from the app.

You can now share desired Google Drive resources with the created user.
Note the email ending with `gserviceaccount.com` we will share the folder with this email.

Once you've done it, you will need an ID of some file or directory. You can obtain it manually by right-clicking on the file -> share -> copy link. It will be part of the URL.

[https://drive.google.com/file/d/[FILE_ID]/view?usp=drive_link](https://drive.google.com/file/d/%5BFILE_ID%5D/view?usp=drive_link)

For folders,
First, right-click on the folder and click share, link will be of the format: [https://drive.google.com/drive/folders/[folder_id]?usp=drive_link](https://drive.google.com/drive/folders/%7Bfolder_id%7D?usp=drive_link)
Copy the folder_id from the URL.
Second, click on share and share the folder with the email ending with `gserviceaccount.com`

### Step 3: Setup Slack notifications

For this demo, Slack notifications are optional and notifications will be printed if no Slack API keys are provided. See: [Slack Apps](https://api.slack.com/apps) and [Getting a token](https://api.slack.com/tutorials/tracks/getting-a-token).
Your Slack application  will need at least `chat:write.public` scope enabled.

### Step 4: Setup environment variables

Set your env variables in the .env file placed in the root of the repo.

```bash
PATHWAY_REST_CONNECTOR_HOST=localhost
OPENAI_API_KEY=sk-...
SLACK_ALERT_CHANNEL_ID=  # If unset, alerts will be printed to the terminal
SLACK_ALERT_TOKEN=
FILE_OR_DIRECTORY_ID=  # file or folder ID that you want to track that we have retrieved earlier
GOOGLE_CREDS=examples/pipelines/drive_alert/secrets.json  # Default location of Google Drive authorization secrets
```

### Step 5: Run the project

#### Install the app dependencies

Install the required packages:

```bash
pip install --upgrade -r requirements.txt
```

#### Run the Pathway API

You start the application by navigating to `backend` foler and running `api.py`:

```bash
cd backend
python api.py
```

#### Run Streamlit UI

You can run the UI separately by running Streamlit app
`streamlit run ui.py` command. It connects to the Pathway's backend API automatically and you will see the UI frontend is running on your browser.

##### (Optional) Connect to a remote backend API

The app has default connection setup to `localhost:8080`. If you use the remote backend API address, you set a host address in Streamlit UI. 