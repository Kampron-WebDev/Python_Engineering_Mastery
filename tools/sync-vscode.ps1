<#
.SYNOPSIS
  Copies the master VS Code config (tools/vscode-template) into the course root,
  every Stage / Level / Module / Lesson / Project folder, and every folder with Python code.

.DESCRIPTION
  VS Code only reads the .vscode folder of the folder you OPEN. With a copy everywhere,
  Ctrl+Shift+B (run), "Run Test Task" (test) and F5 (debug) work wherever you open it.

  Change a setting everywhere: edit tools/vscode-template, then run
      powershell -ExecutionPolicy Bypass -File tools\sync-vscode.ps1
#>
$ErrorActionPreference = 'Stop'
$root     = Split-Path -Parent $PSScriptRoot
$template = Join-Path $PSScriptRoot 'vscode-template'
$skip     = '[\\/](\.vscode|\.venv|\.git|tools|__pycache__)([\\/]|$)'

$targets = [System.Collections.Generic.HashSet[string]]::new()
[void]$targets.Add($root)

Get-ChildItem $root -Directory -Recurse |
    Where-Object { $_.FullName -notmatch $skip -and $_.Name -match '^(\d\d\.|Stage\d|Lv\d\d\.|M\d{3}\.|L\d\d\.|P\d\d\.|Projects$|Final|Level-Exam)' } |
    ForEach-Object { [void]$targets.Add($_.FullName) }

Get-ChildItem $root -Recurse -File -Include *.py |
    Where-Object { $_.FullName -notmatch $skip } |
    ForEach-Object { [void]$targets.Add($_.DirectoryName) }

$count = 0
foreach ($dir in $targets) {
    $dest = Join-Path $dir '.vscode'
    New-Item -ItemType Directory -Force $dest | Out-Null
    Copy-Item (Join-Path $template '*') $dest -Force
    $count++
}
Write-Host "Synced .vscode into $count folders." -ForegroundColor Green
