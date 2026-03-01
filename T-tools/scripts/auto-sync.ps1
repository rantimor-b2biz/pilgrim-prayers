# auto-sync.ps1
# Automatically syncs the local project folder with GitHub (master branch)
# Runs silently in the background every 5 minutes
#
# Setup: Run setup-auto-sync.bat once to register with Windows Task Scheduler
# Manual run: Right-click → Run with PowerShell

param(
    [string]$ProjectPath = "C:\Users\rant\Documents\ran-workspace\Pilgrim Prayers",
    [int]$IntervalMinutes = 5,
    [switch]$RunOnce
)

$logFile = Join-Path $ProjectPath "T-tools\scripts\sync-log.txt"

function Write-Log {
    param([string]$Message)
    $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    $line = "[$timestamp] $Message"
    Add-Content -Path $logFile -Value $line -ErrorAction SilentlyContinue
}

function Sync-Project {
    Set-Location $ProjectPath

    try {
        # Fetch latest from remote (silent)
        $fetch = git fetch origin 2>&1

        # Check if master is behind origin/master
        $status = git rev-list HEAD..origin/master --count 2>&1

        if ($status -match '^\d+$' -and [int]$status -gt 0) {
            # Pull latest master
            git checkout master 2>&1 | Out-Null
            $merge = git merge origin/master --ff-only 2>&1
            Write-Log "Synced $status new commit(s) from GitHub: $merge"
        }

        # Also merge any completed claude/* branches into master
        $claudeBranches = git branch -r 2>&1 | Where-Object { $_ -match 'origin/claude/' }
        foreach ($branch in $claudeBranches) {
            $branchName = $branch.Trim()
            $localName  = $branchName -replace 'origin/', ''

            # Check if this branch has commits not yet in master
            $ahead = git rev-list master..$branchName --count 2>&1
            if ($ahead -match '^\d+$' -and [int]$ahead -gt 0) {
                git checkout master 2>&1 | Out-Null
                $result = git merge $branchName --ff-only 2>&1
                if ($LASTEXITCODE -eq 0) {
                    Write-Log "Merged $localName into master ($ahead commit(s))"
                }
            }
        }

    } catch {
        Write-Log "ERROR: $_"
    }
}

# --- Main loop ---
Write-Log "Auto-sync started. Project: $ProjectPath | Interval: ${IntervalMinutes}m"

if ($RunOnce) {
    Sync-Project
    Write-Log "Auto-sync complete (single run)."
} else {
    while ($true) {
        Sync-Project
        Start-Sleep -Seconds ($IntervalMinutes * 60)
    }
}
