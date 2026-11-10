Set-Location 'C:\OpenSource\pslab-app'
Write-Host "=== PSLab: git status ==="
git status

Write-Host "=== PSLab: git remote -v ==="
git remote -v

Write-Host "=== PSLab: flutter doctor ==="
$flutter = "C:\src\flutter\bin\flutter.bat"
& $flutter doctor

Write-Host "=== PSLab: flutter analyze ==="
& $flutter analyze

Write-Host "=== PSLab: flutter test ==="
& $flutter test

