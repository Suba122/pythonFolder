import os.path
from git import *
import git, os, shutil
# create local Repo/Folder
UPLOAD_FOLDER = "/home/apnx-desk02/Api"
if not os.path.exists(UPLOAD_FOLDER):
  os.makedirs(UPLOAD_FOLDER)
  print(UPLOAD_FOLDER)
new_path = os.path.join(UPLOAD_FOLDER)

DIR_NAME = new_path
REMOTE_URL = "https://github.com/Suba122/pythonFolder.git"  # if you already connected with server you dont need to give any credential
# REMOTE_URL looks "git@github.com:path of Repo"
# code for clone
# code for push
class git_operation_push():
  def git_push_file(self):
    try:
        repo = Repo(DIR_NAME)
        commit_message = 'pushing folders'
        # repo.index.add(u=True)
        repo.git.add('--all')
        repo.index.commit(commit_message)
        origin = repo.remote(name='origin')
        origin.push('master')
        repo.git.add(update=True)
        print("repo push succesfully")
    except Exception as e:
        print(str(e))
if __name__ == '__main__':
   a = git_operation_push()
   git_operation_push.git_push_file('')
