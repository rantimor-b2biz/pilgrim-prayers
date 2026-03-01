#!/usr/bin/env python3
"""
Google OAuth Authentication Setup
Generates token.pickle for accessing Google APIs
Run this ONCE to authorize, then use token.pickle for subsequent calls
"""

import os
import pickle
from google.auth.transport.requests import Request
from google.oauth2.service_account import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow

# Scopes for the APIs we're using
SCOPES = [
    'https://www.googleapis.com/auth/analytics.readonly',  # GA4
    'https://www.googleapis.com/auth/webmasters.readonly',  # GSC
    'https://www.googleapis.com/auth/adwords'  # Google Ads
]

# Paths - navigate to Pilgrim Prayers folder
SCRIPT_DIR = os.path.dirname(__file__)
TTOOLS_DIR = os.path.dirname(SCRIPT_DIR)  # T-tools
WORKSPACE_ROOT = os.path.dirname(TTOOLS_DIR)  # Pilgrim Prayers
AUTH_DIR = os.path.join(WORKSPACE_ROOT, 'B-brain', 'google-auth')
CLIENT_SECRET_FILE = os.path.join(AUTH_DIR, 'client_secret.json')
TOKEN_FILE = os.path.join(AUTH_DIR, 'token.pickle')

def authenticate():
    """Authenticate with Google APIs and create token.pickle"""

    if not os.path.exists(CLIENT_SECRET_FILE):
        print(f"[FAIL] Error: client_secret.json not found at {CLIENT_SECRET_FILE}")
        print("Please download OAuth credentials from Google Cloud Console and save as client_secret.json")
        return None

    creds = None

    # If token.pickle exists, load it
    if os.path.exists(TOKEN_FILE):
        print(f"[OK] Loading existing token from {TOKEN_FILE}")
        with open(TOKEN_FILE, 'rb') as token:
            creds = pickle.load(token)

    # If not authorized or credentials invalid, re-authenticate
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            print("[*] Refreshing credentials...")
            creds.refresh(Request())
        else:
            print("[*] Opening browser for authentication...")
            flow = InstalledAppFlow.from_client_secrets_file(
                CLIENT_SECRET_FILE,
                SCOPES
            )
            creds = flow.run_local_server(port=0)

        # Save token for future use
        with open(TOKEN_FILE, 'wb') as token:
            pickle.dump(creds, token)
        print(f"[OK] Token saved to {TOKEN_FILE}")

    return creds

if __name__ == '__main__':
    print("[LOCK] Google OAuth Authentication Setup")
    print(f"Auth directory: {AUTH_DIR}")
    print(f"Client secret: {CLIENT_SECRET_FILE}")
    print(f"Token file: {TOKEN_FILE}")
    print()

    creds = authenticate()

    if creds:
        print(f"[OK] Authentication successful!")
        print(f"[OK] Token.pickle is ready. Other scripts can now use it.")
    else:
        print(f"[FAIL] Authentication failed.")
