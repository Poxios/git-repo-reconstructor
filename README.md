# Git Repo Reconstructor

## What is this?
* Change file structure of git repo without removal of each file's timestamp like creation time.

## How to use?

## How it works?
1. Get each file's full paths, history of first commit, and target paths (path want to change) and write it into db file.
2. Re-commit all of file in oldest order. If more than one file have same timestamp, 

### DB Structure
Original file name + file hash | commit hash

### Sequence
```
git filter-branch --tree-filter 'if [ -f old ]; then mkdir dir && mv old dir/new; fi' HEAD
```

## License
MIT
