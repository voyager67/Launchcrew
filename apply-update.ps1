$ErrorActionPreference = 'Stop'
$root = $PSScriptRoot
if (-not (Test-Path (Join-Path $root '.agents/skills') -PathType Container) -or -not (Test-Path (Join-Path $root 'scripts/validate_project.py') -PathType Leaf)) {
    throw 'Run this helper only from the root of your existing LaunchCrew repository.'
}

Write-Host 'LaunchCrew layout repair' -ForegroundColor Cyan
Write-Host "Project: $root"

# Remove only duplicate legacy files when their contents exactly match the canonical file.
$mappings = @(
    @{ Old = 'scripts/styles/the-sprint.md'; New = 'styles/the-sprint.md' },
    @{ Old = 'scripts/styles/the-craft.md'; New = 'styles/the-craft.md' },
    @{ Old = 'scripts/tests/test_validate_project.py'; New = 'tests/test_validate_project.py' },
    @{ Old = 'scripts/templates/spec/requirements.md'; New = 'templates/spec/requirements.md' },
    @{ Old = 'scripts/templates/spec/design.md'; New = 'templates/spec/design.md' },
    @{ Old = 'scripts/templates/spec/plan.md'; New = 'templates/spec/plan.md' },
    @{ Old = 'scripts/templates/spec/acceptance.md'; New = 'templates/spec/acceptance.md' }
)

foreach ($mapping in $mappings) {
    $oldPath = Join-Path $root $mapping.Old
    $newPath = Join-Path $root $mapping.New
    if (-not (Test-Path -LiteralPath $oldPath -PathType Leaf)) { continue }

    if (-not (Test-Path -LiteralPath $newPath -PathType Leaf)) {
        $newParent = Split-Path -Parent $newPath
        New-Item -ItemType Directory -Path $newParent -Force | Out-Null
        Copy-Item -LiteralPath $oldPath -Destination $newPath
        Write-Host "Recovered missing canonical file: $($mapping.New)"
        continue
    }

    $oldHash = (Get-FileHash -LiteralPath $oldPath -Algorithm SHA256).Hash
    $newHash = (Get-FileHash -LiteralPath $newPath -Algorithm SHA256).Hash
    if ($oldHash -eq $newHash) {
        Remove-Item -LiteralPath $oldPath -Force
        Write-Host "Removed duplicate legacy file: $($mapping.Old)"
    }
    else {
        Write-Warning "Kept $($mapping.Old) because it differs from $($mapping.New); review this file manually."
    }
}

foreach ($relativeDir in @('scripts/styles', 'scripts/tests', 'scripts/templates')) {
    $directory = Join-Path $root $relativeDir
    if ((Test-Path -LiteralPath $directory -PathType Container) -and
        -not (Get-ChildItem -LiteralPath $directory -File -Force -Recurse | Select-Object -First 1)) {
        Remove-Item -LiteralPath $directory -Force -Recurse
        Write-Host "Removed empty legacy directory: $relativeDir"
    }
}

$pythonLauncher = Get-Command py -ErrorAction SilentlyContinue
$python = Get-Command python -ErrorAction SilentlyContinue
if ($pythonLauncher) {
    $pythonExe = $pythonLauncher.Source
    $pythonPrefix = @('-3')
}
elseif ($python) {
    $pythonExe = $python.Source
    $pythonPrefix = @()
}
else {
    Write-Warning 'Python was not found. Layout repair is complete, but local validation was skipped; GitHub Actions can run the checks after you push.'
    $pythonExe = $null
    $pythonPrefix = @()
}

if ($pythonExe) {
    $checks = @(
        @('scripts/validate_project.py'),
        @('-m', 'unittest', 'discover', '-s', 'tests', '-v'),
        @('scripts/package_chatgpt_skills.py', '--check')
    )
    foreach ($check in $checks) {
        $argsToRun = @($pythonPrefix) + @($check)
        Write-Host ("`n> {0} {1}" -f $pythonExe, ($argsToRun -join ' ')) -ForegroundColor DarkCyan
        & $pythonExe @argsToRun
        if ($LASTEXITCODE -ne 0) {
            throw "Validation failed (exit code $LASTEXITCODE). The update script was kept so you can rerun or inspect it."
        }
    }
}

if (Get-Command git -ErrorAction SilentlyContinue) {
    Write-Host "`nGit status:" -ForegroundColor Cyan
    & git -C $root status --short
}

Write-Host "`nRepair complete. Review the changes in GitHub Desktop, commit them, and push to origin/main." -ForegroundColor Green
# Keep the repository clean: this helper is only for applying the update patch.
try { Remove-Item -LiteralPath $PSCommandPath -Force -ErrorAction SilentlyContinue } catch { }
