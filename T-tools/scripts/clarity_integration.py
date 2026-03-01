#!/usr/bin/env python3
"""
CLARITY Integration for Paid Search Agent
Fetches heatmap, session recording, and conversion funnel data from Microsoft Clarity
Analyzes user behavior patterns to inform ad copy and landing page optimization
"""

import os
import json
import pickle
import requests
from datetime import datetime, timedelta

# Configuration
CLARITY_API_BASE = "https://api.clarity.microsoft.com"
CLARITY_PROJECT_ID = None  # Will be set from env or config

# Paths
SCRIPT_DIR = os.path.dirname(__file__)
TTOOLS_DIR = os.path.dirname(SCRIPT_DIR)
WORKSPACE_ROOT = os.path.dirname(TTOOLS_DIR)
CONFIG_DIR = os.path.join(WORKSPACE_ROOT, 'B-brain', 'google-auth')
OUTPUT_DIR = os.path.join(WORKSPACE_ROOT, 'B-brain', 'clarity-analysis')

# Create output directory if it doesn't exist
os.makedirs(OUTPUT_DIR, exist_ok=True)


def load_clarity_credentials():
    """Load CLARITY API key from config file"""
    config_file = os.path.join(CONFIG_DIR, 'clarity-config.json')

    if not os.path.exists(config_file):
        print("[FAIL] CLARITY config file not found")
        print(f"Create this file: {config_file}")
        print("Format:")
        print("""{
  "api_key": "YOUR_CLARITY_API_KEY",
  "project_id": "YOUR_PROJECT_ID"
}""")
        return None

    try:
        with open(config_file, 'r') as f:
            config = json.load(f)
        return config
    except Exception as e:
        print(f"[FAIL] Error loading CLARITY config: {e}")
        return None


def fetch_heatmap_data(config):
    """Fetch heatmap data from CLARITY"""
    print("[*] Fetching heatmap data from CLARITY...")

    try:
        headers = {
            "Authorization": f"Bearer {config['api_key']}",
            "Content-Type": "application/json"
        }

        # Get last 7 days of heatmap data
        end_date = datetime.now().date()
        start_date = end_date - timedelta(days=7)

        url = f"{CLARITY_API_BASE}/projects/{config['project_id']}/heatmaps"
        params = {
            "startDate": str(start_date),
            "endDate": str(end_date)
        }

        response = requests.get(url, headers=headers, params=params, timeout=30)
        response.raise_for_status()

        data = response.json()
        print(f"[OK] Fetched heatmap data: {len(data.get('heatmaps', []))} pages tracked")

        return data
    except requests.exceptions.RequestException as e:
        print(f"[WARN] Error fetching heatmap data: {e}")
        return None
    except Exception as e:
        print(f"[FAIL] Unexpected error: {e}")
        return None


def fetch_session_recordings(config):
    """Fetch session recording data from CLARITY"""
    print("[*] Fetching session recording insights...")

    try:
        headers = {
            "Authorization": f"Bearer {config['api_key']}",
            "Content-Type": "application/json"
        }

        # Get summary of session recordings
        url = f"{CLARITY_API_BASE}/projects/{config['project_id']}/sessions"
        params = {
            "limit": 100,
            "sortBy": "engagement_score"
        }

        response = requests.get(url, headers=headers, params=params, timeout=30)
        response.raise_for_status()

        data = response.json()
        print(f"[OK] Fetched {len(data.get('sessions', []))} top engagement sessions")

        return data
    except requests.exceptions.RequestException as e:
        print(f"[WARN] Error fetching sessions: {e}")
        return None
    except Exception as e:
        print(f"[FAIL] Unexpected error: {e}")
        return None


def fetch_conversion_funnels(config):
    """Fetch conversion funnel data from CLARITY"""
    print("[*] Fetching conversion funnel analysis...")

    try:
        headers = {
            "Authorization": f"Bearer {config['api_key']}",
            "Content-Type": "application/json"
        }

        # Get conversion funnel data
        url = f"{CLARITY_API_BASE}/projects/{config['project_id']}/funnels"

        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status()

        data = response.json()
        print(f"[OK] Fetched funnel analysis: {len(data.get('funnels', []))} funnels tracked")

        return data
    except requests.exceptions.RequestException as e:
        print(f"[WARN] Error fetching funnels: {e}")
        return None
    except Exception as e:
        print(f"[FAIL] Unexpected error: {e}")
        return None


def analyze_user_friction(heatmap_data, session_data, funnel_data):
    """Analyze friction points from CLARITY data"""
    report = []
    report.append("# CLARITY User Behavior Analysis\n\n")
    report.append(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")

    # Heatmap insights
    report.append("## [DATA] Heatmap Insights\n\n")
    if heatmap_data:
        heatmaps = heatmap_data.get('heatmaps', [])
        report.append(f"**Pages with heatmaps:** {len(heatmaps)}\n\n")

        if heatmaps:
            report.append("### Top Clicked Areas\n")
            for hm in heatmaps[:5]:
                report.append(f"- **{hm.get('page_url', 'Unknown')}**\n")
                report.append(f"  - Clicks: {hm.get('click_count', 0)}\n")
                report.append(f"  - Scrolls: {hm.get('scroll_depth', 0)}%\n")
    else:
        report.append("_No heatmap data available_\n")

    report.append("\n---\n\n")

    # Session recordings
    report.append("## [*] Session Recording Patterns\n\n")
    if session_data:
        sessions = session_data.get('sessions', [])
        report.append(f"**Recorded sessions:** {len(sessions)}\n\n")

        if sessions:
            report.append("### High-Engagement Sessions\n")
            for session in sessions[:5]:
                report.append(f"- Session ID: {session.get('id', 'Unknown')}\n")
                report.append(f"  - Duration: {session.get('duration_seconds', 0)}s\n")
                report.append(f"  - Engagement Score: {session.get('engagement_score', 0)}\n")
    else:
        report.append("_No session data available_\n")

    report.append("\n---\n\n")

    # Conversion funnels
    report.append("## [ADS] Conversion Funnel Analysis\n\n")
    if funnel_data:
        funnels = funnel_data.get('funnels', [])
        report.append(f"**Funnels tracked:** {len(funnels)}\n\n")

        if funnels:
            report.append("### Drop-off Points\n")
            for funnel in funnels[:3]:
                report.append(f"- **{funnel.get('name', 'Unknown Funnel')}**\n")
                steps = funnel.get('steps', [])
                for i, step in enumerate(steps):
                    dropoff = step.get('dropoff_percent', 0)
                    if dropoff > 20:
                        report.append(f"  - Step {i+1}: **HIGH DROP-OFF** ({dropoff}%)\n")
                    else:
                        report.append(f"  - Step {i+1}: {dropoff}% drop-off\n")
    else:
        report.append("_No funnel data available_\n")

    report.append("\n---\n\n")

    # Ad Copy Recommendations
    report.append("## [INFO] Ad Copy Implications\n\n")
    report.append("Based on CLARITY data, consider:\n\n")
    report.append("1. **Address friction points** - If users are scrolling but not clicking CTA, test different CTA copy\n")
    report.append("2. **Value proposition placement** - Use heatmaps to place main message where users look first\n")
    report.append("3. **Funnel landing pages** - Test different ad copy for high-drop-off funnel steps\n")
    report.append("4. **Trust signals** - High engagement sessions may reveal which messages resonate\n\n")

    return "\n".join(report)


def save_analysis(content):
    """Save analysis to markdown file"""
    timestamp = datetime.now().strftime("%Y-%m-%d")
    filename = os.path.join(OUTPUT_DIR, f"{timestamp}-clarity-analysis.md")

    with open(filename, 'w') as f:
        f.write(content)

    return filename


def main():
    print("=" * 60)
    print("[DATA] CLARITY Integration for Paid Search Agent")
    print("=" * 60)
    print()

    # Load CLARITY credentials
    config = load_clarity_credentials()
    if not config:
        exit(1)

    # Fetch all data
    heatmap_data = fetch_heatmap_data(config)
    session_data = fetch_session_recordings(config)
    funnel_data = fetch_conversion_funnels(config)

    print()
    print("[*] Analyzing user behavior patterns...")
    analysis = analyze_user_friction(heatmap_data, session_data, funnel_data)

    # Save analysis
    filename = save_analysis(analysis)
    print(f"[OK] Analysis saved to: {filename}")

    print()
    print("[INFO] CLARITY analysis location:")
    print(f"   {OUTPUT_DIR}")
    print()
    print("[NEXT] Next steps:")
    print("   1. Review this analysis in Paid Search Agent briefing")
    print("   2. Use friction points to refine ad copy")
    print("   3. Test different messaging for high-drop-off pages")
    print("   4. Feed winning patterns to M-memory/learning-log.md")


if __name__ == '__main__':
    main()
