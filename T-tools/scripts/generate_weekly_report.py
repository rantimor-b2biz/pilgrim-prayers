#!/usr/bin/env python3
"""
Generate Weekly Report
Orchestrator script that runs all data extraction scripts
and creates a unified weekly summary
"""

import os
import subprocess
import sys
from datetime import datetime

# Paths
SCRIPT_DIR = os.path.dirname(__file__)
TTOOLS_DIR = os.path.dirname(SCRIPT_DIR)
WORKSPACE_ROOT = os.path.dirname(TTOOLS_DIR)
SCRIPTS_DIR = SCRIPT_DIR
OUTPUT_DIR = os.path.join(WORKSPACE_ROOT, 'B-brain', 'ads-performance')

def run_script(script_name):
    """Run a Python script and return success status"""
    script_path = os.path.join(SCRIPTS_DIR, script_name)

    if not os.path.exists(script_path):
        print(f"[FAIL] Script not found: {script_path}")
        return False

    print(f"\n[RUN] Running {script_name}...")
    try:
        result = subprocess.run(
            [sys.executable, script_path],
            capture_output=True,
            text=True,
            timeout=60
        )

        if result.returncode == 0:
            print(result.stdout)
            return True
        else:
            print(f"[WARN] {script_name} completed with warnings:")
            print(result.stdout)
            if result.stderr:
                print(result.stderr)
            return True  # Still return true for warnings
    except subprocess.TimeoutExpired:
        print(f"[FAIL] {script_name} timed out")
        return False
    except Exception as e:
        print(f"[FAIL] Error running {script_name}: {e}")
        return False

def create_weekly_summary():
    """Create unified weekly summary from individual reports"""
    timestamp = datetime.now().strftime("%Y-%m-%d")
    summary_file = os.path.join(OUTPUT_DIR, f"{timestamp}-weekly-summary.md")

    ga4_file = os.path.join(OUTPUT_DIR, f"{timestamp}-ga4-report.md")
    gsc_file = os.path.join(OUTPUT_DIR, f"{timestamp}-gsc-report.md")
    ads_file = os.path.join(OUTPUT_DIR, f"{timestamp}-ads-report.md")

    summary = []
    summary.append("# Weekly Performance Summary\n\n")
    summary.append(f"**Week of:** {timestamp}\n")
    summary.append(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")

    summary.append("## [GA4] Google Analytics (GA4)\n\n")
    if os.path.exists(ga4_file):
        with open(ga4_file, 'r') as f:
            content = f.read()
            # Extract just the content part
            lines = content.split('\n')[3:]  # Skip header
            summary.append('\n'.join(lines))
    else:
        summary.append("_GA4 report not yet generated_\n")

    summary.append("\n---\n\n")
    summary.append("## [GSC] Google Search Console (GSC)\n\n")
    if os.path.exists(gsc_file):
        with open(gsc_file, 'r') as f:
            content = f.read()
            lines = content.split('\n')[3:]  # Skip header
            summary.append('\n'.join(lines))
    else:
        summary.append("_GSC report not yet generated_\n")

    summary.append("\n---\n\n")
    summary.append("## [ADS] Google Ads\n\n")
    if os.path.exists(ads_file):
        with open(ads_file, 'r') as f:
            content = f.read()
            lines = content.split('\n')[3:]  # Skip header
            summary.append('\n'.join(lines))
    else:
        summary.append("_Google Ads report not yet generated_\n")

    summary.append("\n---\n\n")
    summary.append("## [TODO] Next Steps\n\n")
    summary.append("1. **Analyze Performance:** Review metrics above to identify trends\n")
    summary.append("2. **Extract Ad Hooks:** Use top-performing queries and pages for ad copy inspiration\n")
    summary.append("3. **Update Keyword Map:** Add new keywords from GSC organic queries\n")
    summary.append("4. **Optimize Bids:** Adjust bids based on conversion performance\n")
    summary.append("5. **Feed M-memory:** Log winning messages and patterns to learning-log.md\n")

    with open(summary_file, 'w') as f:
        f.write("".join(summary))

    return summary_file

if __name__ == '__main__':
    print("=" * 60)
    print("[DATA] Pilgrim Prayers Weekly Performance Report Generator")
    print("=" * 60)
    print()

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # Run individual extraction scripts
    scripts = [
        'pull_ga4_data.py',
        'pull_gsc_data.py',
        'pull_ads_data.py',
        'clarity_integration.py'
    ]

    success_count = 0
    for script in scripts:
        if run_script(script):
            success_count += 1

    print("\n" + "=" * 60)
    print(f"[OK] Data extraction complete ({success_count}/{len(scripts)} scripts)")
    print("=" * 60)

    # Create unified summary
    print("\n[*] Creating weekly summary...")
    summary_file = create_weekly_summary()
    print(f"[OK] Summary saved to: {summary_file}\n")

    print("[INFO] Reports location:")
    print(f"   {OUTPUT_DIR}\n")

    print("[NEXT] Next action:")
    print("   Review the summary above and use it for:")
    print("   - Paid Search Agent's weekly performance analysis")
    print("   - Identifying ad copy winners")
    print("   - Updating keyword strategy")
    print("   - Feeding insights to M-memory")
