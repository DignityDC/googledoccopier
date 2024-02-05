# Google Docs Copier

This Python script automates the process of copying a Google Doc and sharing the new copy with a specified email address using the Google Docs and Google Drive APIs.

## Prerequisites

Before you can run the script, you need to:

1. Have Python installed on your machine.
2. Create a project in the Google Cloud Console, enable the Google Docs and Google Drive APIs for your project, and obtain OAuth 2.0 credentials (`credentials.json`).

## Setup

1. Clone this repository to your local machine.
2. Place your `credentials.json` file in the root directory of the project. This file can be obtained by following the steps outlined in the official Google documentation for setting up OAuth 2.0 credentials.
3. Install the required Python packages by running the following command in your terminal:

```bash
pip install -r requirements.txt
