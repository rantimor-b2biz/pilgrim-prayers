#!/usr/bin/env python3
"""
Pull Google Search Console Data
Fetches organic search queries, CTR, impressions
Outputs to B-brain/ads-performance/[date]-gsc-report.md
"""

import os
import pickle
from datetime import datetime, timedelta
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

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

def fetch_gsc_data(creds, site_url="https://pilgrimprayers.org/"):
    """Fetch GSC data"""
    try:
        webmasters_service = build('webmasters', 'v3', credentials=creds)

        # Query search analytics
        end_date = datetime.now().date()
        start_date = end_date - timedelta(days=28)

        request = {
            'startDate': str(start_date),
            'endDate': str(end_date),
            'dimensions': ['query', 'page'],
            'rowLimit': 10000
        }

        response = webmasters_service.searchanalytics().query(
            siteUrl=site_url,
            body=request
        ).execute()

        return response
    except Exception as e:
        print(f"[WARN] Error querying GSC: {e}")
        print("Note: GSC API requires proper site verification in Search Console")
        return None

def format_gsc_report(response):
    """Format GSC response into markdown"""
    report = []
    report.append("# Google Search Console Report\n")
    report.append(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    report.append(f"**Site:** https://pilgrimprayers.org/\n")
    report.append(f"**Period:** Last 28 days\n\n")

    report.append("## Overview\n")

    if not response or 'rows' not in response:
        report.append("No data available. Please ensure:\n")
        report.append("1. Site is verified in Google Search Console\n")
        report.append("2. OAuth credentials include webmasters scope\n")
        report.append("3. Account has GSC access\n\n")
        report.append("## Top Queries\n")
        report.append("| Query | Clicks | Impressions | CTR | Avg Position |\n")
        report.append("|-------|--------|-------------|-----|-------------|\n")
        report.append("| No data | - | - | - | - |\n")
        return "".join(report)

    # Aggregate stats
    total_clicks = 0
    total_impressions = 0
    rows = response.get('rows', [])

    for row in rows:
        total_clicks += row.get('clicks', 0)
        total_impressions += row.get('impressions', 0)

    avg_ctr = (total_clicks / total_impressions * 100) if total_impressions > 0 else 0

    report.append("| Metric | Value |\n")
    report.append("|--------|-------|\n")
    report.append(f"| Total Clicks | {total_clicks} |\n")
    report.append(f"| Total Impressions | {total_impressions} |\n")
    report.append(f"| Average CTR | {avg_ctr:.1f}% |\n\n")

    report.append("## Top Queries\n")
    report.append("| Query | Clicks | Impressions | CTR | Avg Position |\n")
    report.append("|-------|--------|-------------|-----|-------------|\n")

    for row in rows[:20]:
        query = row.get('keys', ['Unknown'])[0]
        clicks = row.get('clicks', 0)
        impressions = row.get('impressions', 0)
        ctr = (clicks / impressions * 100) if impressions > 0 else 0
        position = row.get('position', 0)

        report.append(f"| {query[:40]} | {clicks} | {impressions} | {ctr:.1f}% | {position:.1f} |\n")

    report.append("\n## Top Pages\n")
    report.append("| Page | Clicks | Impressions | CTR | Avg Position |\n")
    report.append("|------|--------|-------------|-----|-------------|\n")

    # Re-query grouped by page
    page_stats = {}
    for row in rows:
        page = row.get('keys', ['', 'Unknown'])[1] if len(row.get('keys', [])) > 1 else 'Unknown'
        if page not in page_stats:
            page_stats[page] = {'clicks': 0, 'impressions': 0, 'positions': []}

        page_stats[page]['clicks'] += row.get('clicks', 0)
        page_stats[page]['impressions'] += row.get('impressions', 0)
        page_stats[page]['positions'].append(row.get('position', 0))

    for page, stats in sorted(page_stats.items(), key=lambda x: x[1]['clicks'], reverse=True)[:10]:
        clicks = stats['clicks']
        impressions = stats['impressions']
        ctr = (clicks / impressions * 100) if impressions > 0 else 0
        avg_position = sum(stats['positions']) / len(stats['positions']) if stats['positions'] else 0

        report.append(f"| {page[:40]} | {clicks} | {impressions} | {ctr:.1f}% | {avg_position:.1f} |\n")

    return "".join(report)

def save_report(report_content):
    """Save report to file"""
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d")
    filename = os.path.join(OUTPUT_DIR, f"{timestamp}-gsc-report.md")

    with open(filename, 'w') as f:
        f.write(report_content)

    return filename

if __name__ == '__main__':
    print("[GSC] Google Search Console Data Extraction")
    print(f"Site: https://pilgrimprayers.org/")
    print()

    creds = load_credentials()
    if not creds:
        print("[FAIL] Failed to load credentials")
        exit(1)

    print("[*] Fetching GSC data...")
    try:
        response = fetch_gsc_data(creds)
        report = format_gsc_report(response)
        filename = save_report(report)
        print(f"[OK] Report saved to: {filename}")
    except Exception as e:
        print(f"[FAIL] Error: {e}")
        # Still save a template
        report = format_gsc_report(None)
        filename = save_report(report)
        print(f"[WARN] Template saved to: {filename}")
        print("[INFO] To enable GSC access:")
        print("   - Verify your site in Google Search Console")
        print("   - Ensure OAuth has 'webmasters' scope")
        print("   - Re-run google_auth_setup.py")
