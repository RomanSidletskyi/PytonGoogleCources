
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



 
