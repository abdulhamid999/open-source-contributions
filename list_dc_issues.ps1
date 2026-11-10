$issues = gh api 'repos/deepchem/deepchem/issues?state=open&per_page=50' | ConvertFrom-Json
foreach ($i in $issues) {
    if (-not $i.pull_request) {
        $a = if ($i.assignee) { $i.assignee.login } else { 'None' }
        Write-Host "#$($i.number): $($i.title) (Assignee: $a, Comments: $($i.comments))"
    }
}

