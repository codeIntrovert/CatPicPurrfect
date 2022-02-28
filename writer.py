from github import Github

def filewrite(x):
    github = Github('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')
    repository = github.get_user().get_repo('twat')
    # path in the repository
    content = x
    filename = 'logFile.txt'
    f = repository.create_file(filename, "create_file via PyGithub",content)

