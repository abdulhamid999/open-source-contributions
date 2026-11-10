# Ensure Flutter is in User Path
$userPath = [Environment]::GetEnvironmentVariable('Path', [EnvironmentVariableTarget]::User)
if ($userPath -notlike '*C:\src\flutter\bin*') {
    $userPath = "$userPath;C:\src\flutter\bin"
    [Environment]::SetEnvironmentVariable('Path', $userPath, [EnvironmentVariableTarget]::User)
    Write-Host "Added C:\src\flutter\bin to User Path."
} else {
    Write-Host "C:\src\flutter\bin already in User Path."
}

# Ensure Miniforge is in User Path
$miniforgePath = "$env:USERPROFILE\miniforge3"
$miniforgeEntries = @($miniforgePath, "$miniforgePath\Scripts", "$miniforgePath\condabin")
foreach ($entry in $miniforgeEntries) {
    if ($userPath -notlike "*$entry*") {
        $userPath = "$userPath;$entry"
        [Environment]::SetEnvironmentVariable('Path', $userPath, [EnvironmentVariableTarget]::User)
    }
}

# Create conda deepchem environment if not already existing
$condaBat = "$miniforgePath\condabin\conda.bat"
Write-Host "Checking conda environment..."
$envList = & $condaBat env list
if ($envList -notmatch "deepchem") {
    Write-Host "Creating conda environment 'deepchem' with Python 3.11..."
    & $condaBat create -n deepchem python=3.11 -y
} else {
    Write-Host "Conda environment 'deepchem' already exists."
}

Write-Host "Enabling Flutter windows desktop..."
& "C:\src\flutter\bin\flutter.bat" config --enable-windows-desktop

Write-Host "Verification completed."

