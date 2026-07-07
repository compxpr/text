[CmdletBinding()]
param([switch]$RecreateVenv)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

$RepoRoot = Resolve-Path (Join-Path $PSScriptRoot '..\..')
$VenvPath = Join-Path $RepoRoot '.venv-contracts'
$IsWindowsHost = ($PSVersionTable.PSEdition -eq 'Desktop') -or ($env:OS -eq 'Windows_NT')
$VenvPythonRelative = if ($IsWindowsHost) { 'Scripts\python.exe' } else { 'bin/python' }
$PythonExe = Join-Path $VenvPath $VenvPythonRelative

function Get-BootstrapPython {
    $candidates = @('python', 'py')
    foreach ($candidate in $candidates) {
        try {
            if ($candidate -eq 'py') {
                & py -3 --version *> $null
            }
            else {
                & $candidate --version *> $null
            }

            if ($LASTEXITCODE -eq 0) {
                return $candidate
            }
        }
        catch {
            continue
        }
    }

    throw 'Python 3 was not found on PATH. Install Python 3 and rerun the validator.'
}

Push-Location $RepoRoot
try {
    if ($RecreateVenv -and (Test-Path $VenvPath)) {
        Remove-Item -Path $VenvPath -Recurse -Force
    }

    if (-not (Test-Path $PythonExe)) {
        $BootstrapPython = Get-BootstrapPython
        if ($BootstrapPython -eq 'py') {
            & py -3 -m venv .venv-contracts
        }
        else {
            & $BootstrapPython -m venv .venv-contracts
        }
    }

    if (-not (Test-Path $PythonExe)) {
        throw "Virtual environment Python was not created at $PythonExe."
    }

    & $PythonExe -m pip install --upgrade pip
    if ($LASTEXITCODE -ne 0) {
        throw "pip upgrade failed with exit code $LASTEXITCODE."
    }

    & $PythonExe -m pip install -r contract-requirements.txt
    if ($LASTEXITCODE -ne 0) {
        throw "Contract dependency install failed with exit code $LASTEXITCODE."
    }

    & $PythonExe contracts\tools\check.py
    if ($LASTEXITCODE -ne 0) {
        throw "Contract checker failed with exit code $LASTEXITCODE."
    }
}
finally {
    Pop-Location
}
