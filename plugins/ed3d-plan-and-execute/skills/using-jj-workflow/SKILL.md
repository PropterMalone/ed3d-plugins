---
name: using-jj-workflow
description: Use when working with Jujutsu (jj) VCS - guides change management, description, and navigation with jj's intuitive workflow model
---

# Using Jujutsu (jj) Workflow

## Overview

Jujutsu provides a simpler, more intuitive version control model than git. Key differences:
- **No staging area** - all changes in working copy are part of current change
- **Changes, not commits** - work on changes that can be edited, described, and moved
- **Automatic change creation** - `jj new` creates a fresh change automatically
- **Safe operations** - most operations are reversible via `jj op undo`

**Core principle:** Create changes freely, describe them when ready, move between them easily.

**Announce at start:** "I'm using the using-jj-workflow skill to manage changes with Jujutsu."

## Common Workflows

### Starting New Work

**Create a new change for feature work:**

```bash
# Create new change off current change
jj new -m "feat: descriptive message"

# Or create without message (add later)
jj new
```

**Create new change from a bookmark (like a branch):**

```bash
# List available bookmarks
jj bookmark list

# Create new change from main
jj new main -m "feat: new feature"
```

### Working on Changes

**Check what you're working on:**

```bash
# Show current change and status
jj status

# Or shorter form
jj st

# See change graph
jj log
```

**Describe your current change:**

```bash
# Add/update description (like git commit)
jj describe -m "feat: implement feature X"

# Or open editor for longer message
jj describe
```

**Amend changes (always safe in jj):**

Just make your edits and describe again:
```bash
# Make changes to files
# No need to stage - all working copy changes are included
jj describe -m "Updated message"
```

### Moving Between Changes

**Switch to a different change:**

```bash
# By change ID (shown in jj log)
jj edit qpvuntsm

# Or by bookmark
jj edit main

# Create new change on top of specific change
jj new main
```

**See available changes:**

```bash
# Show change graph (like git log)
jj log

# More detailed view
jj log --summary
```

### Organizing Changes

**Squash current change into parent:**

```bash
jj squash
```

**Split a change into multiple:**

```bash
# Interactive split (choose which files go in each part)
jj split
```

**Insert a new change between current and parent:**

```bash
jj new --insert-before
```

### Working with Remotes

**Push to remote:**

```bash
# Push current bookmark
jj git push

# Push specific bookmark
jj git push --bookmark feature-branch
```

**Fetch from remote:**

```bash
jj git fetch
```

**Create/move bookmarks (like git branches):**

```bash
# Create bookmark at current change
jj bookmark create feature-name

# Move bookmark to current change
jj bookmark set feature-name

# Delete bookmark
jj bookmark delete old-feature
```

## Key Concepts

### Changes vs Commits

- In jj, you work on **changes** (mutable) that become **commits** when pushed
- You can always edit, describe, or reorganize changes
- Changes have short IDs (e.g., `qpvuntsm`) and optional descriptions

### Working Copy

- The working copy is always associated with a change
- All file modifications automatically belong to the current change
- No staging area - what you see is what you'll describe

### Bookmarks vs Branches

- **Bookmarks** in jj are like git branches
- They point to changes and move when you create new changes on top
- Multiple bookmarks can point to the same change

### Operation Log

- Every jj operation is recorded
- Can undo/redo any operation: `jj op log` then `jj op undo`

## Safety Features

**Undo any operation:**
```bash
# See recent operations
jj op log

# Undo last operation
jj op undo

# Redo after undo
jj op redo
```

**Abandoned changes are recoverable:**
- Abandoned changes still exist in operation log
- Can restore them with `jj op undo` or by their change ID

## Integration with Git

Jujutsu works seamlessly with git repositories:

```bash
# Initialize jj in existing git repo
jj git init --git-repo=.

# Or create new repo with git backend
jj git init --git-repo=. my-project
```

All git operations still work:
- `.git` directory is shared between jj and git
- Can use git commands alongside jj
- Bookmarks sync with git branches

## Quick Reference

| Task | jj Command | git Equivalent |
|------|------------|----------------|
| New change | `jj new -m "message"` | `git checkout -b branch` + `git commit` |
| Status | `jj status` | `git status` |
| History | `jj log` | `git log` |
| Describe | `jj describe -m "msg"` | `git commit -m "msg"` |
| Amend | Just describe again | `git commit --amend` |
| Switch change | `jj edit CHANGE_ID` | `git checkout COMMIT` |
| Push | `jj git push` | `git push` |
| Fetch | `jj git fetch` | `git fetch` |
| Undo operation | `jj op undo` | `git reset` (less safe) |

## When to Use This Skill

Use this skill when:
- Starting new feature work with jj
- Need to organize or clean up changes
- Working with jj in a git repository
- Teaching users about jj workflow

Don't use when:
- Project requires specific git workflows (use using-git-worktrees)
- Working with pure git repositories where jj isn't set up
