foreach ($num in @(5234, 5226, 5217)) {
    $prs = gh pr list --repo deepchem/deepchem --state all --search "$num" --json number,title,state | ConvertFrom-Json
    Write-Host "PRs matching #$num`: $($prs.Count)"
    foreach ($pr in $prs) {
        Write-Host "  PR #$($pr.number): $($pr.title) ($($pr.state))"
    }
}

