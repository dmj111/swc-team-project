

Here is a stab in the dark at script, maybe more like a template, for
talking about gitignore files.

These directions assume you are in this repository, but a different
location could be used.


## Setup ##
   - clone this repository
   - make a small change to `script.py` so git sees it as changed.
      - this program creates some empty output files, and a directory
        with output files

## Start -- Show the problem ##

 - run `git status`, it shows `script.py` as changed
 - run `python script.py`, creating some data files.
 - run `git status` -- it shows `script.py` as modified,
   and the data files as `?` [show as 'untracked' for me - PB]
 - check in the code file?

## Ignore file ##

- create a `.gitignore` file.
- add this line to gitignore

    *.out

- `git status`
- should show that the out files are missing, but the data directory
  is still `?`

 - ignore the directory now [do you want to add this to the .gitignore file?]

    /data/


- this ignores the `data` directory, but only in the root directory
- through all of this, `.gitignore`  will show up in the status too...


## Seeing ignored files ##

- `git status --ignored` to see the status, including the ignored files.


## Extra ##

- `git add data` or `git add 1.dat` complains about adding ignored files
- more details of the ignore files
- different ignore files:  
`~/.gitignore` global ignores
    `.gitignore`, deals with the current directory [and its subdirectories?]
 `.git/info/exclude` [I would skip discussing this -- looks complicated]
- `git clean` removes untracked files from the working tree
