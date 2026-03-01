#!/usr/bin/env python3
"""
Agent Scheduler for Pilgrim Prayers
Automatically runs agents on a fixed schedule
- Paid Search Agent: Weekly (every Friday at 6 AM)
- UX Expert Agent: Weekly (every Monday at 8 AM)
- Custom on-demand: Manual triggers via command line
"""

import os
import sys
import json
import subprocess
from datetime import datetime
from pathlib import Path

# Paths
SCRIPT_DIR = os.path.dirname(__file__)
TTOOLS_DIR = os.path.dirname(SCRIPT_DIR)
WORKSPACE_ROOT = os.path.dirname(TTOOLS_DIR)
LOG_DIR = os.path.join(WORKSPACE_ROOT, 'B-brain', 'agent-logs')
CONFIG_FILE = os.path.join(WORKSPACE_ROOT, 'T-tools', 'agent-schedule.json')

# Create log directory
os.makedirs(LOG_DIR, exist_ok=True)


def load_schedule():
    """Load agent schedule from config file"""
    default_schedule = {
        "paid_search": {
            "enabled": True,
            "day_of_week": "friday",
            "hour": 6,
            "minute": 0,
            "script": "generate_weekly_report.py",
            "description": "Pull GA4, GSC, Google Ads, and CLARITY data"
        },
        "ux_expert": {
            "enabled": True,
            "day_of_week": "monday",
            "hour": 8,
            "minute": 0,
            "script": "ux_expert_analysis.py",
            "description": "Analyze landing pages and friction points"
        }
    }

    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, 'r') as f:
                return json.load(f)
        except:
            return default_schedule
    else:
        # Create default schedule file
        with open(CONFIG_FILE, 'w') as f:
            json.dump(default_schedule, f, indent=2)
        return default_schedule


def save_schedule(schedule):
    """Save schedule to config file"""
    with open(CONFIG_FILE, 'w') as f:
        json.dump(schedule, f, indent=2)


def log_execution(agent_name, status, message=""):
    """Log agent execution to file"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_file = os.path.join(LOG_DIR, f"agent-execution.log")

    log_entry = f"[{timestamp}] {agent_name}: {status}"
    if message:
        log_entry += f" - {message}"

    with open(log_file, 'a') as f:
        f.write(log_entry + "\n")

    print(log_entry)


def run_agent(script_name, agent_name):
    """Run an agent script and log the result"""
    script_path = os.path.join(SCRIPT_DIR, script_name)

    if not os.path.exists(script_path):
        log_execution(agent_name, "[FAIL]", f"Script not found: {script_name}")
        return False

    try:
        print(f"\n[*] Running {agent_name}...")
        result = subprocess.run(
            [sys.executable, script_path],
            capture_output=True,
            text=True,
            timeout=300
        )

        if result.returncode == 0:
            log_execution(agent_name, "[OK]", "Execution successful")
            return True
        else:
            error_msg = result.stderr if result.stderr else "Unknown error"
            log_execution(agent_name, "[WARN]", error_msg)
            return True  # Still return true for scheduling

    except subprocess.TimeoutExpired:
        log_execution(agent_name, "[FAIL]", "Script timed out (300 seconds)")
        return False
    except Exception as e:
        log_execution(agent_name, "[FAIL]", str(e))
        return False


def check_and_run_scheduled_agents():
    """Check if any agents should run based on schedule"""
    schedule = load_schedule()
    now = datetime.now()

    day_names = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    current_day = day_names[now.weekday()]
    current_hour = now.hour
    current_minute = now.minute

    print("=" * 60)
    print(f"[DATA] Agent Scheduler - {now.strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 60)
    print()

    agents_run = 0

    for agent_key, agent_config in schedule.items():
        if not agent_config.get('enabled', False):
            print(f"[INFO] {agent_key} is disabled")
            continue

        scheduled_day = agent_config.get('day_of_week', '').lower()
        scheduled_hour = agent_config.get('hour', -1)
        scheduled_minute = agent_config.get('minute', 0)

        # Check if it's time to run
        is_right_day = current_day == scheduled_day
        is_right_time = (current_hour == scheduled_hour and current_minute == scheduled_minute)

        print(f"[INFO] {agent_key}:")
        print(f"       Scheduled: {scheduled_day} at {scheduled_hour:02d}:{scheduled_minute:02d}")
        print(f"       Current: {current_day} at {current_hour:02d}:{current_minute:02d}")

        if is_right_day and is_right_time:
            print(f"[*] RUNNING NOW!")
            script = agent_config.get('script')
            if script:
                if run_agent(script, agent_key):
                    agents_run += 1
        else:
            print(f"[*] Not time yet")

        print()

    return agents_run


def list_schedule():
    """Display current schedule"""
    schedule = load_schedule()

    print("=" * 60)
    print("[DATA] Current Agent Schedule")
    print("=" * 60)
    print()

    for agent_key, config in schedule.items():
        status = "[ON]" if config.get('enabled') else "[OFF]"
        print(f"{status} {agent_key}")
        print(f"    When: {config.get('day_of_week')} at {config.get('hour', 0):02d}:{config.get('minute', 0):02d}")
        print(f"    Script: {config.get('script')}")
        print(f"    Description: {config.get('description', 'N/A')}")
        print()


def run_agent_now(agent_name):
    """Run a specific agent immediately"""
    schedule = load_schedule()

    if agent_name not in schedule:
        print(f"[FAIL] Agent '{agent_name}' not found")
        print(f"Available agents: {', '.join(schedule.keys())}")
        return False

    agent_config = schedule[agent_name]
    script = agent_config.get('script')

    if not script:
        print(f"[FAIL] No script configured for {agent_name}")
        return False

    print(f"[*] Running {agent_name} now (on-demand)")
    return run_agent(script, agent_name)


def edit_schedule():
    """Edit schedule interactively"""
    schedule = load_schedule()

    print("=" * 60)
    print("[DATA] Edit Agent Schedule")
    print("=" * 60)
    print()

    for i, (agent_key, config) in enumerate(schedule.items(), 1):
        print(f"{i}. {agent_key}")
        print(f"   Enabled: {config.get('enabled')}")
        print(f"   When: {config.get('day_of_week')} at {config.get('hour', 0):02d}:{config.get('minute', 0):02d}")
        print()

    print("To edit, directly edit this file:")
    print(f"   {CONFIG_FILE}")
    print()


def show_execution_log():
    """Show recent agent executions"""
    log_file = os.path.join(LOG_DIR, "agent-execution.log")

    if not os.path.exists(log_file):
        print("[INFO] No execution log yet")
        return

    print("=" * 60)
    print("[DATA] Recent Agent Executions")
    print("=" * 60)
    print()

    with open(log_file, 'r') as f:
        lines = f.readlines()
        # Show last 20 lines
        for line in lines[-20:]:
            print(line.rstrip())


def main():
    if len(sys.argv) < 2:
        # Default: check and run scheduled agents
        check_and_run_scheduled_agents()
    else:
        command = sys.argv[1].lower()

        if command == 'check':
            check_and_run_scheduled_agents()
        elif command == 'list':
            list_schedule()
        elif command == 'run':
            if len(sys.argv) < 3:
                print("[FAIL] Usage: python agent-scheduler.py run <agent_name>")
                print("Example: python agent-scheduler.py run paid_search")
                return
            run_agent_now(sys.argv[2])
        elif command == 'edit':
            edit_schedule()
        elif command == 'log':
            show_execution_log()
        elif command == 'help':
            print("Agent Scheduler Commands:")
            print()
            print("  python agent-scheduler.py check   - Check and run scheduled agents")
            print("  python agent-scheduler.py list    - Show current schedule")
            print("  python agent-scheduler.py run <agent> - Run specific agent now")
            print("  python agent-scheduler.py edit    - Edit schedule")
            print("  python agent-scheduler.py log     - Show execution log")
            print()
            print("Examples:")
            print("  python agent-scheduler.py run paid_search")
            print("  python agent-scheduler.py run ux_expert")
        else:
            print(f"[FAIL] Unknown command: {command}")
            print("Run: python agent-scheduler.py help")


if __name__ == '__main__':
    main()
