
``diff`` is used to find differences between two files. On its own, it’s a bit hard to use; instead, use it with diff -u to find lines which differ in two files:

``diff -u`` is used to compare two files, line by line, and have the differing lines compared side-by-side in the same output. See below:

There are some other interesting patch and diff commands such as patch -p1, diff -r !

``Patch`` is useful for applying file differences. See the below example, which compares two files. The comparison is saved as a .diff file, which is then patched to the original file!
Check them out in the following references:

- http://man7.org/linux/man-pages/man1/diff.1.html
- http://man7.org/linux/man-pages/man1/patch.1.html

## More Information About Git
Check out the following links for more information:

- https://git-scm.com/doc
- https://www.mercurial-scm.org/
- https://subversion.apache.org/
- https://en.wikipedia.org/wiki/Version_control

The [Linux kernel documentation](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/Documentation/process/submitting-patches.rst?id=HEAD) itself, as well as [impassioned](http://stopwritingramblingcommitmessages.com/) opinions from other [developers](https://robots.thoughtbot.com/5-useful-tips-for-a-better-commit-message). 

There are many useful git cheatsheets online as well. Please take some time to research and study a few, such as this one.

**.gitignore files**
.gitignore files are used to tell the git tool to intentionally ignore some files in a given Git repository. For example, this can be useful for configuration files or metadata files that a user may not want to check into the master branch. Check out more at: https://git-scm.com/docs/gitignore.

### Git Revert Cheat Sheet
[git checkout](https://git-scm.com/docs/git-checkout) is effectively used to switch branches.
[git reset](https://git-scm.com/docs/git-reset#_examples) basically resets the repo, throwing away some changes. It’s somewhat difficult to understand, so reading the examples in the documentation may be a bit more useful.
There are some other useful articles online, which discuss more aggressive approaches to [resetting the repo](https://jwiegley.github.io/git-from-the-bottom-up/3-Reset/4-doing-a-hard-reset.html).

[git commit --amend](https://git-scm.com/docs/git-commit#Documentation/git-commit.txt---amend) is used to make changes to commits after-the-fact, which can be useful for making notes about a given commit.

[git revert](https://git-scm.com/docs/git-revert) makes a new commit which effectively rolls back a previous commit. It’s a bit like an undo command.

There are a [few ways](https://git-scm.com/book/en/v2/Git-Basics-Undoing-Things) you can rollback commits in Git.

There are some interesting considerations about how git object data is stored, such as the usage of sha-1. 
### Git Branches and Merging Cheat Sheet

- git branch : [Used to manage branches
- git branch <name>  : [Creates the branch](https://git-scm.com/docs/git-branch) 
- git branch -d <name> : [Deletes the branch](https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging)
- git branch -D <name> : [Forcibly deletes the branch](https://git-scm.com/docs/git-branch#Documentation/git-branch.txt--D) 
- git checkout <branch>  : [Switches to a branch](https://git-scm.com/docs/git-checkout). 
- git checkout -b <branch> : Creates a new branch and [switches to it](https://git-scm.com/docs/git-checkout#Documentation/git-checkout.txt--bltnewbranchgt).
- git merge <branch>  : [Merge joins branches together](https://git-scm.com/docs/git-merge). 
- git merge --abort : If there are merge conflicts (meaning files are incompatible), --abort can be used to abort the merge action.
- git log --graph --oneline : [This shows a summarized view of the commit history for a repo](https://git-scm.com/book/en/v2/Git-Basics-Viewing-the-Commit-History).

## GitHub

### Some useful commands for getting started:

- git clone URL : [Git clone is used to clone a remote repository into a local workspace](https://git-scm.com/docs/git-clone)
- git push : [Git push is used to push commits from your local repo to a remote repo](https://git-scm.com/docs/git-push)
- git pull : [Git pull is used to fetch the newest updates from a remote repository](https://git-scm.com/docs/git-pull)

 ### Git Remotes Cheat-Sheet
- git remote : [Lists remote repos](https://git-scm.com/docs/git-remote)
- git remote -v : [List remote repos verbosely](https://git-scm.com/docs/git-remote#Documentation/git-remote.txt--v)
- git remote show <name> : [Describes a single remote repo](https://git-scm.com/docs/git-remote#Documentation/git-remote.txt-emshowem)
- git remote update : [Fetches the most up-to-date objects](https://git-scm.com/docs/git-remote#Documentation/git-remote.txt-emupdateem)
- git fetch : [Downloads specific objects](https://git-scm.com/docs/git-fetch)
- git branch -r : [Lists remote branches](https://git-scm.com/docs/git-branch#Documentation/git-branch.txt--r); can be combined with other branch arguments to manage remote branches

You can also see more in the video [Cryptography in Action](https://www.coursera.org/learn/it-security/item/P1I8z) from the course [IT Security: Defense against the digital dark arts](https://www.coursera.org/learn/it-security/home/welcome).
 
- chmod 600 ~/Documents/downloads/qwiklabs-L7072132.pem
-  ssh -i ~/Documents/downloads/qqwiklabs-L7072132.pem student-01-3b2f35b83401@35.202.64.242

 
