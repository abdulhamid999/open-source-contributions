$condaBat = "$env:USERPROFILE\miniforge3\condabin\conda.bat"
Write-Host "Creating conda environment 'deepchem' with Python 3.11..."
& $condaBat create -n deepchem python=3.11 -y
Write-Host "Conda environment created."

