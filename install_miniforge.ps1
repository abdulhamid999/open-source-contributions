$tempDir = 'C:\OpenSource\temp'
if (-not (Test-Path $tempDir)) { 
    New-Item -ItemType Directory -Path $tempDir | Out-Null 
}
$miniforgeInstaller = "$tempDir\Miniforge3.exe"

Write-Host "Downloading Miniforge installer..."
curl.exe -L -o $miniforgeInstaller "https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Windows-x86_64.exe"

Write-Host "Running silent installation for Miniforge..."
$installPath = "$env:USERPROFILE\miniforge3"
$proc = Start-Process -FilePath $miniforgeInstaller -ArgumentList "/InstallationType=JustMe /RegisterPython=1 /AddToPath=1 /S /D=$installPath" -Wait -PassThru

Write-Host "Process exit code: $($proc.ExitCode)"
$condaBin = "$installPath\condabin\conda.bat"
if (Test-Path $condaBin) {
    & $condaBin --version
    $userPath = [Environment]::GetEnvironmentVariable('Path', [EnvironmentVariableTarget]::User)
    $newEntries = @($installPath, "$installPath\Scripts", "$installPath\condabin")
    foreach ($entry in $newEntries) {
        if ($userPath -notlike "*$entry*") {
            $userPath = "$userPath;$entry"
        }
    }
    [Environment]::SetEnvironmentVariable('Path', $userPath, [EnvironmentVariableTarget]::User)
    Write-Host "Successfully added Miniforge to User PATH."
} else {
    Write-Host "conda.bat not found at $condaBin"
}

