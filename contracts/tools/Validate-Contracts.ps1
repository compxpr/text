[CmdletBinding()]
param([switch]$RecreateVenv)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

$RepoRoot = Resolve-Path (Join-Path $PSScriptRoot '..\..')
$VenvPath = Join-Path $RepoRoot '.venv-contracts'
$PythonExe = Join-Path $VenvPath 'Scripts\python.exe'

Push-Location $RepoRoot
try {
    if ($RecreateVenv -and (Test-Path $VenvPath)) {
        Remove-Item -Path $VenvPath -Recurse -Force
    }
    if (-not (Test-Path $PythonExe)) {
        python -m venv .venv-contracts
    }
    & $PythonExe -m pip install --upgrade pip
    & $PythonExe -m pip install -r contract-requirements.txt
    & $PythonExe contracts\tools\check.py
}
finally {
    Pop-Location
}
