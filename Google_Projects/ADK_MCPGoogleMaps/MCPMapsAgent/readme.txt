checkout
https://docs.cloud.google.com/mcp/enable-disable-mcp-servers?cloudshell=false 

To eliminate the 403 Forbidden error when connecting to [https://mapstools.googleapis.com/mcp](https://mapstools.googleapis.com/mcp), follow these step-by-step actions:
Step 1: Enable the "Maps Grounding Lite API"

The remote endpoint is hosted by the Maps Grounding Lite API (mapstools.googleapis.com).

    Go to the Google Cloud Console API Library.

    Confirm your active project (gen-lang-client-0671401948) is selected.

    Search for Maps Grounding Lite API (or look up mapstools.googleapis.com).

    Click Enable.

Step 2: Grant IAM / Auth Permissions to ADC

Ensure your local gcloud Application Default Credentials (ADC) are authenticated against the exact GCP project hosting the enabled service:

    Open PowerShell and re-authenticate ADC:

    & "C:\Users\samin\AppData\Local\Google\Cloud SDK\google-cloud-sdk\bin\gcloud.cmd" auth application-default login

2. Confirm your .env file inside ADK_MCPGoogleMaps includes your project ID alongside your API keys:

GOOGLE_CLOUD_PROJECT=gen-lang-client-0671401948
MAPS_API_KEY=your_maps_api_key

Step 3: Check API Key Restrictions

    In Google Cloud Console, navigate to APIs & Services > Credentials.

    Click on your MAPS_API_KEY.

    Under API restrictions, ensure Maps Grounding Lite API (or mapstools.googleapis.com) is checked in the allowed list.

Step 4: Restart the ADK Web Server & Test

    Stop the current running ADK server in your terminal (CTRL+C).

    Relaunch the server:

adk web