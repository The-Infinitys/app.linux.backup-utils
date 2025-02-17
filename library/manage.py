import git_utils,terminal
import os,sys,json

setting=json.loads(open(os.path.join(os.path.dirname(__file__), "../settings/setting.json")).read())
print(setting)