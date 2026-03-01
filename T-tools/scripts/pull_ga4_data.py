#!/usr/bin/env python3
"""
Pull GA4 Data
Fetches performance metrics from Google Analytics 4
Outputs to B-brain/ads-performance/[date]-ga4-report.md
"""

import os
import pickle
from datetime import datetime, timedelta
from google.analytics.data import (
    BetaAnalyticsDataClient,
    RunReportRequest,
    Dimension,
    Metric,
    DateRange
)

# Configuration
GA4_PROPERTY_ID = "448264628"

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

def fetch_ga4_data(creds):
    """Fetch GA4 data"""
    client = BetaAnalyticsDataClient(credentials=creds)

    # Last 7 days
    end_date = datetime.now().date()
    start_date = end_date - timedelta(days=7)

    request = RunReportRequest(
        property=f"properties/{GA4_PROPERTY_ID}",
        date_ranges=[DateRange(start_date=str(start_date), end_date=str(end_date))],
        dimensions=[Dimension(name="pagePath"), Dimension(name="deviceCategory")],
        metrics=[
            Metric(name="screenPageViews"),
            Metric(name="sessions"),
            Metric(name="bounceRate"),
            Metric(name="conversions"),
            Metric(name="averageSessionDuration"),
        ],
    )

    response = client.run_report(request)
    return response

def format_ga4_report(response):
    """Format GA4 response into markdown"""
    report = []
    report.append("# GA4 Performance Report\n")
    report.append(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    report.append(f"**Property ID:** 448264628\n")
    report.append(f"**Period:** Last 7 days\n\n")

    report.append("## Overview\n")
    report.append("| Metric | Value |\n")
    report.append("|--------|-------|\n")

    # Aggregate metrics
    total_views = 0
    total_sessions = 0
    total_bounces = 0
    total_conversions = 0
    total_duration = 0
    count = 0

    for row in response.rows:
        values = row.metric_values
        total_views += int(values[0].value)
        total_sessions += int(values[1].value)
        total_bounces += float(values[2].value)
        total_conversions += int(values[3].value)
        total_duration += float(values[4].value)
        count += 1

    avg_bounce = total_bounces / count if count > 0 else 0
    avg_duration = total_duration / count if count > 0 else 0

    report.append(f"| Total Page Views | {total_views} |\n")
    report.append(f"| Total Sessions | {total_sessions} |\n")
    report.append(f"| Average Bounce Rate | {avg_bounce:.1f}% |\n")
    report.append(f"| Total Conversions | {total_conversions} |\n")
    report.append(f"| Avg Session Duration | {avg_duration:.0f}s |\n\n")

    report.append("## Top Landing Pages\n")
    report.append("| Page | Device | Views | Sessions | Bounce Rate | Conversions |\n")
    report.append("|------|--------|-------|----------|-------------|-------------|\n")

    for row in response.rows[:10]:
        page = row.dimension_values[0].value
        device = row.dimension_values[1].value
        views = row.metric_values[0].value
        sessions = row.metric_values[1].value
        bounce = row.metric_values[2].value
        conversions = row.metric_values[3].value

        report.append(f"| {page[:30]} | {device} | {views} | {sessions} | {bounce}% | {conversions} |\n")

    return "".join(report)

def save_report(report_content):
    """Save report to file"""
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d")
    filename = os.path.join(OUTPUT_DIR, f"{timestamp}-ga4-report.md")

    with open(filename, 'w') as f:
        f.write(report_content)

    return filename

if __name__ == '__main__':
    print("[GA4] GA4 Data Extraction")
    print(f"Property ID: {GA4_PROPERTY_ID}")
    print()

    creds = load_credentials()
    if not creds:
        print("[FAIL] Failed to load credentials")
        exit(1)

    print("[*] Fetching GA4 data...")
    try:
        response = fetch_ga4_data(creds)
        print(f"[OK] Fetched {len(response.rows)} rows")

        report = format_ga4_report(response)
        filename = save_report(report)
        print(f"[OK] Report saved to: {filename}")
    except Exception as e:
        print(f"[FAIL] Error: {e}")
        exit(1)
