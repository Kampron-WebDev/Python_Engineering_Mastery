<#
.SYNOPSIS
  Runs the tests of every exercise / debugging challenge / exam task in the course
  against its MODEL SOLUTION. A green run proves all the practice material is healthy.

.DESCRIPTION
  Each exercise folder contains:
      main.py           <- the student's file (starter with TODOs, or buggy code)
      test_main.py      <- tests; they use the `main` / `load` fixtures from conftest.py,
                           which import solution/ instead when CHECK_SOLUTION=1
      solution/main.py  <- the model answer

  -Starters  also checks that every STARTER fails its tests. Add an empty file named
             .starter-passes to a folder whose starter is meant to pass.

.EXAMPLE
  powershell -ExecutionPolicy Bypass -File tools\check-exercises.ps1
  powershell -ExecutionPolicy Bypass -File tools\check-exercises.ps1 -Filter M001 -Starters
#>
param([string]$Filter = '', [switch]$Starters)
$root = Split-Path -Parent $PSScriptRoot
$py   = Join-Path $root '.venv\Scripts\python.exe'
if (-not (Test-Path $py)) { throw "No virtual environment found at $py (see 00.Orientation)." }

$dirs = Get-ChildItem $root -Recurse -File -Filter 'test_*.py' |
    Where-Object { $_.FullName -notmatch '[\\/](\.venv|\.git|tools|__pycache__)[\\/]' -and $_.FullName -like "*$Filter*" } |
    Select-Object -ExpandProperty DirectoryName -Unique | Sort-Object

function Invoke-Tests([string]$dir, [bool]$solution) {
    if ($solution) { $env:CHECK_SOLUTION = '1' } else { Remove-Item Env:CHECK_SOLUTION -ErrorAction SilentlyContinue }
    Push-Location $dir
    $files = @(Get-ChildItem -File -Filter 'test_*.py' | Select-Object -ExpandProperty Name)
    # -P: don't put the current folder on sys.path, so a file that shadows the standard library
    #     in a STARTER folder (on purpose) can't leak into the solution check.
    $log = & $py -P -m pytest @files 2>&1
    $code = $LASTEXITCODE
    Pop-Location
    Remove-Item Env:CHECK_SOLUTION -ErrorAction SilentlyContinue
    return @{ Code = $code; Log = $log }
}

$pass = 0; $fail = @()
foreach ($d in $dirs) {
    if (Test-Path (Join-Path $d '.skip-check')) { continue }
    $rel = $d.Substring($root.Length + 1)

    $r = Invoke-Tests $d $true
    if ($r.Code -eq 0) { $pass++; Write-Host "  ok   $rel" -ForegroundColor DarkGreen }
    else {
        $fail += $rel; Write-Host "  FAIL $rel (solution)" -ForegroundColor Red
        $r.Log | Select-String -Pattern 'FAILED|Error|assert' | Select-Object -First 8 | ForEach-Object { Write-Host "       $_" }
    }

    if ($Starters -and -not (Test-Path (Join-Path $d '.starter-passes'))) {
        $s = Invoke-Tests $d $false
        if ($s.Code -eq 0) { $fail += "$rel (starter)"; Write-Host "  FAIL $rel (starter already passes!)" -ForegroundColor Red }
    }
}
Write-Host ""
Write-Host "Passed: $pass   Failed: $($fail.Count)" -ForegroundColor ($(if ($fail.Count) { 'Red' } else { 'Green' }))
exit $fail.Count
