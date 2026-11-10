$tempDir = 'C:\OpenSource\temp'
if (-not (Test-Path $tempDir)) { 
    New-Item -ItemType Directory -Path $tempDir | Out-Null 
}
$zipPath = "$tempDir\flutter_windows_3.47.9-stable.zip"
$flutterUrl = "https://storage.googleapis.com/flutter_infra_release/releases/stable/windows/flutter_windows_3.47.9-stable.zip"

if (-not (Test-Path $zipPath)) {
    Write-Host "Downloading Flutter 3.47.9 (~1.1 GB)..."
    curl.exe -L -o $zipPath $flutterUrl
} else {
    Write-Host "Flutter zip already downloaded."
}

$destDir = "C:\src"
if (-not (Test-Path $destDir)) {
    New-Item -ItemType Directory -Path $destDir | Out-Null
}

$flutterDir = "C:\src\flutter"
if (-not (Test-Path "$flutterDir\bin\flutter.bat")) {
    Write-Host "Extracting Flutter to C:\src..."
    tar.exe -xf $zipPath -C $destDir
} else {
    Write-Host "Flutter already extracted to C:\src\flutter."
}

$flutterBin = "$flutterDir\bin"
if (Test-Path "$flutterBin\flutter.bat") {
    $userPath = [Environment]::GetEnvironmentVariable('Path', [EnvironmentVariableTarget]::User)
    if ($userPath -notlike "*$flutterBin*") {
        $userPath = "$userPath;$flutterBin"
        [Environment]::SetEnvironmentVariable('Path', $userPath, [EnvironmentVariableTarget]::User)
        Write-Host "Added $flutterBin to User PATH."
    } else {
        Write-Host "$flutterBin is already in User PATH."
    }
    Write-Host "Verifying Flutter version..."
    & "$flutterBin\flutter.bat" --version
} else {
    Write-Host "Error: flutter.bat not found at $flutterBin"
}

