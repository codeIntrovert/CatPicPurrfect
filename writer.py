from github import Github

def filewrite(x):
    r = open("logFile.txt","a")
    r.write(x)
    r.close()
    
    github = Github('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')
    repository = github.get_user().get_repo('twat')
    # path in the repository
    filename = 'logFile.txt'
    f = repository.create_file(filename, "create_file via PyGithub")

