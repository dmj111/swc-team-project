

Here is a stab in the dark at script, maybe more like a template, for
talking about gitignore files.

## Setup ##

   - a git repository with
       - at least one code file, that creates some
         output files  (a few `.out` files, and a `data` directory?)
   - add the code file to the git repository (but don't check in yet!)




## Start -- Show the problem ##

 - run `git status`, it shows the code file as added
 - run the code file, creating some data files
 - run `git status` -- it shows the code file, and the data files as `?`
 - check in the code file?

## Ignore file ##


 - add this line to gitignore

    *.out

 - `git status`
     - should show that the out files are missing, but the data directory
       is still `?`

 - ignore the directory now

    /data/


   - this ignores the `data` directory, but only in the root directory


 - through all of this, `.gitignore`  will show up in the status too...


## Seeing ignored files ##

  - `git status --ignored` to see the status, including the ignored files.



## Extra ##

 - `git add data` *should* complain about adding ignored files
     - but `git add 1.out` will work, because it wasn't a wildcard
 - more details of the ignore files
 - different ignore files:  `~/.gitignore`,
    `.gitignore`, `.git/info/exclude`
 - `git clean`
