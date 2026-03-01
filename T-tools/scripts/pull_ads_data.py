#!/usr/bin/env python3
"""
Pull Google Ads Data
Fetches campaign, ad group, and keyword performance
Outputs to B-brain/ads-performance/[date]-ads-report.md
"""

import os
import pickle
from datetime import datetime, timedelta
from google.ads.googleads.client import GoogleAdsClient

# Configuration
CUSTOMER_ID = "2568647503"  # Without hyphens: 256-864-7503

# Paths
SCRIPT_DIR = os.path.dirname(__file__)
TTOOLS_DIR = os.path.dirname(SCRIPT_DIR)
WORKSPACE_ROOT = os.path.dirname(TTOOLS_DIR)
AUTH_DIR = os.path.join(WORKSPACE_ROOT, 'B-brain', 'google-auth')
TOKEN_FILE = os.path.join(AUTH_DIR, 'token.pickle')
OUTPUT_DIR = os.path.join(WORKSPACE_ROOT, 'B-brain', 'ads-performance')

def load_credentials():
    """Load credentials from token.pickle"""
    if not os.path.exists(TOKEN_FILE):
        print(f"[FAIL] Token file not found: {TOKEN_FILE}")
        print("Run google_auth_setup.py first to generate token.pickle")
        return None

    with open(TOKEN_FILE, 'rb') as token:
        from google.oauth2.credentials import Credentials
        creds = pickle.load(token)
    return creds

def fetch_ads_data(creds):
    """Fetch Google Ads data"""
    # Note: Google Ads API requires developer token and manager account setup
    # This is a simplified version - full implementation depends on account structure

    try:
        client = GoogleAdsClient.load_from_storage(
            version="v16",
            credentials=creds
        )

        ga_service = client.get_service("GoogleAdsService")

        # Query recent campaigns
        query = """
            SELECT
                campaign.id,
                campaign.name,
                campaign.status,
                metrics.impressions,
                metrics.clicks,
                metrics.cost_micros,
                metrics.conversions,
                metrics.conversion_value
            FROM campaign
            WHERE segments.date DURING LAST_7_DAYS
            ORDER BY metrics.impressions DESC
            LIMIT 20
        """

        results = ga_service.search_stream(customer_id=CUSTOMER_ID, query=query)
        return results
    except Exception as e:
        print(f"[WARN] Note: Google Ads API requires additional setup (developer token)")
        print(f"Error: {e}")
        return None

def format_ads_report(results):
    """Format Ads response into markdown"""
    report = []
    report.append("# Google Ads Performance Report\n")
    report.append(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    report.append(f"**Customer ID:** 256-864-7503\n")
    report.append(f"**Period:** Last 7 days\n\n")

    report.append("## Campaign Performance\n")
    report.append("| Campaign | Status | Impressions | Clicks | Cost | Conversions |\n")
    report.append("|----------|--------|-------------|--------|------|-------------|\n")

    if results:
        for batch in results:
            for row in batch.results:
                campaign = row.campaign.name
                status = row.campaign.status
                impressions = row.metrics.impressions
                clicks = row.metrics.clicks
                cost = row.metrics.cost_micros / 1_000_000  # Convert from micros
                conversions = row.metrics.conversions

                report.append(f"| {campaign[:30]} | {status} | {impressions} | {clicks} | ${cost:.2f} | {conversions} |\n")
    else:
        report.append("| No data available | - | - | - | - | - |\n")

    report.append("\n## Note\n")
    report.append("Full Google Ads API integration requires:\n")
    report.append("1. Developer token from Google Ads account\n")
    report.append("2. Manager account configuration\n")
    report.append("3. OAuth credentials with Google Ads scope\n")

    return "".join(report)

def save_report(report_content):
    """Save report to file"""
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d")
    filename = os.path.join(OUTPUT_DIR, f"{timestamp}-ads-report.md")

    with open(filename, 'w') as f:
        f.write(report_content)

    return filename

if __name__ == '__main__':
    print("[ADS] Google Ads Data Extraction")
    print(f"Customer ID: 256-864-7503")
    print()

    print("[WARN] Note: Full Google Ads API access requires:")
    print("1. Developer token registered with Google")
    print("2. Manager account properly configured")
    print("3. OAuth credentials with 'adwords' scope")
    print()

    # For now, just save a template report
    report = format_ads_report(None)
    filename = save_report(report)
    print(f"[OK] Template report saved to: {filename}")
    print("[INFO] To enable full integration:")
    print("   - Get Google Ads Developer Token")
    print("   - Update CUSTOMER_ID and developer token in this script")
    print("   - Re-run google_auth_setup.py with new scopes")
