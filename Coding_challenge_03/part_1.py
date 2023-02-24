# 1. Simple directory tree
# Replicate this tree of directories and subdirectories:
#
# ├── draft_code
# |   ├── pending
# |   └── complete
# ├── includes
# ├── layouts
# |   ├── default
# |   └── post
# |       └── posted
# └── site
# Using os.system or os.mkdirs replicate this simple directory tree.
# Delete the directory tree without deleting your entire hard drive.

import os

#1st I create the 4 main folders:
os.mkdir('draft_code')
os.mkdir('includes')
os.mkdir('layouts')
os.mkdir('site')

#Next I add the subfolders to draft_code and layouts:
os.mkdir('draft_code/pending')
os.mkdir('draft_code/complete')
os.mkdir('layouts/default')
os.mkdir('layouts/post')

#Last I add the sub-subfolder to the post subfolder:
os.mkdir('layouts/post/posted')

#I include the 2 lines below just to check that the directories actually get made.
list = os.listdir()
print(list)

#Now I remove them in the opposite order, from the inside out:
os.removedirs('layouts/post/posted')

os.removedirs('draft_code/pending')
os.removedirs('draft_code/complete')
os.removedirs('layouts/default')

os.removedirs('includes')
os.removedirs('site')
