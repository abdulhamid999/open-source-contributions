Set-Location 'C:\OpenSource\deepchem'
Write-Host "=== DeepChem: git status ==="
git status

Write-Host "=== DeepChem: git remote -v ==="
git remote -v

Write-Host "=== DeepChem: import test ==="
$python = "$env:USERPROFILE\miniforge3\envs\deepchem\python.exe"
& $python -c "import deepchem as dc; print('DeepChem:', dc.__version__)"

Write-Host "=== DeepChem: pytest collect-only ==="
& $python -m pytest --collect-only deepchem/splits/tests

