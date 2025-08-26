## git init directory structure before and after a commit. When you git add, a file is copied, sha1 and compressed into a Sha designated directory. What happens with commit? Does it write to a sqlite database or what? It's called an object database

Before a commit:
- **.git/objects**: Contains subdirectories for objects but is mostly empty before the first commit.
- **.git/refs/heads**: Empty, as no branches have been created yet.

After `git add` but before commit:
- **.git/objects**: Contains the blobs (content) and trees (directory structures) for the staged changes.

After a commit:
- **.git/objects**: Now also contains a commit object, storing metadata (author, date, message) and a pointer to the tree.
- **.git/refs/heads**: Contains a reference to the commit for the current branch.

Git's object database isn't a SQL database. It's a simple key-value store. Each object (commit, tree, blob, tag) is identified by its SHA-1 hash. These objects are stored as files in the `.git/objects` directory. The commit object links everything together, pointing to the tree and parent commits, storing the project's history as a graph.

## actual contents of a commit object.

A commit object in Git contains several pieces of information, formatted as plain text. Here's an example of what it might look like:

```plaintext
commit 176
tree d670460b4b4aece5915caf5c68d12f560a9fe3e4
parent 9c68fdc529d5e6c9e5e7f5f040f96f803f8ea7cb
author John Doe <john@example.com> 1599870773 -0400
committer John Doe <john@example.com> 1599870773 -0400

Initial commit
```

- **Commit size**: `commit 176` indicates the size of the commit object.
- **Tree**: The SHA-1 hash of the tree object representing the top directory of the working tree at this commit.
- **Parent**: The SHA-1 hash of the parent commit(s). This line is absent for the initial commit.
- **Author/Committer**: Information about who made the changes and when (timestamp and timezone).
- **Commit message**: A description of the commit, e.g., "Initial commit".

This text is stored in a file in the `.git/objects` directory, with a filename derived from the SHA-1 hash of the contents. To view the contents of a commit object directly, you can use the `git cat-file -p [commit-hash]` command in the terminal.

## Does the top directory of the working tree mean the start of a new branch?

No, the "top directory of the working tree" in the context of a Git commit object does not refer to the start of a new branch. Instead, it refers to the highest-level directory in your repository at the time of that commit.

Here's what it means:

1. **Top Directory of the Working Tree**: This is the root directory of your project in your local environment. It's where your `.git` directory resides along with all the project files and folders.

2. **Commit's Relation to Branches**: When you make a commit, it's not inherently about starting a new branch. It's about recording the current state of your working tree in the history of the branch you're currently on. A commit represents a snapshot of your repository at a specific point in time.

3. **Branches in Git**: Branches are pointers to commits. When you start a new branch (`git branch new-branch`), Git creates a new pointer to the current commit. If you make changes and commit them on this new branch, the branch pointer moves forward to include these new commits.

So, the "top directory of the working tree" is just about the state of your files and directories in a commit, and not specifically about branching. Branches are more about how you navigate and record the history of these changes in your repository.

## highest level directory = the directory where you first ran `git init` and contains the .git folder?

Exactly. The "highest level directory" or "top directory of the working tree" in a Git repository is the directory where you initially ran `git init`. This directory contains the `.git` folder, which holds all of the Git configuration and repository data, including branches, commits, tags, and more. Everything you manage with Git in your project is relative to this top-level directory.

