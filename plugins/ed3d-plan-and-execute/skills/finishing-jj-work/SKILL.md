---
name: finishing-jj-work
description: Use when completing work with Jujutsu - guides change finalization, bookmark management, and push/PR workflows
---

# Finishing Work with Jujutsu

## Overview

Complete development work in a jj repository by organizing changes, creating bookmarks, and pushing to remote.

**Core principle:** Verify tests → Organize changes → Create bookmark → Push/PR → Clean up.

**Announce at start:** "I'm using the finishing-jj-work skill to complete this work."

## The Process

### Step 1: Verify Tests

**Before finishing, verify tests pass:**

```bash
# Run project's test suite
npm test / cargo test / pytest / go test ./...
```

**If tests fail:**
```
Tests failing (<N> failures). Must fix before completing:

[Show failures]

Cannot proceed with push/PR until tests pass.
```

Stop. Don't proceed to Step 2.

**If tests pass:** Continue to Step 2.

### Step 2: Review Change Graph

**See your changes:**

```bash
# View change graph
jj log

# Or with more detail
jj log --summary
```

**Check for:**
- Are all your changes described properly?
- Do you need to squash any changes?
- Are you on the right parent change?

### Step 3: Organize Changes (Optional)

**If you have multiple related changes that should be one:**

```bash
# Squash current change into parent
jj squash

# Or squash specific change
jj squash --from CHANGE_ID
```

**If you need to split a change:**

```bash
# Interactive split
jj split
```

**If changes need better descriptions:**

```bash
# Update description of current change
jj describe -m "Better description"

# Or edit specific change
jj describe CHANGE_ID
```

### Step 4: Create/Update Bookmark

**For new work, create a bookmark:**

```bash
# Create bookmark at current change
jj bookmark create feature-name

# Or create and set in one step
jj bookmark set feature-name
```

**For existing work, verify bookmark:**

```bash
# List bookmarks
jj bookmark list

# Move bookmark if needed
jj bookmark set feature-name
```

### Step 5: Present Options

Present these options to the user:

```
Work is complete and tests pass. How would you like to proceed?

1. Push to remote and create PR
   - Push current bookmark: jj git push --bookmark feature-name
   - Open PR via: gh pr create

2. Push to remote only
   - Push without creating PR
   - Useful for backup or collaboration

3. Squash all changes and push
   - Combine all changes into one
   - Then push as single change

4. Stay local
   - Keep changes unpushed
   - Continue working or review later

Which option? [1-4]
```

### Step 6: Execute Choice

**Option 1: Push and PR**

```bash
# Push bookmark to remote
jj git push --bookmark feature-name

# Create PR
gh pr create --title "Title" --body "Description"
```

**Option 2: Push Only**

```bash
jj git push --bookmark feature-name
```

**Option 3: Squash and Push**

```bash
# Squash all changes into first one
jj squash --into FIRST_CHANGE_ID

# Update description
jj describe -m "Final description"

# Push
jj git push --bookmark feature-name
```

**Option 4: Stay Local**

No action needed. User can continue working.

### Step 7: Update Project Context (After Push/PR)

**If changes affect contracts or architecture:**

```
Changes pushed. Considering invoking project-claude-librarian to update CLAUDE.md files?

[Wait for user decision]
```

### Step 8: Clean Up (Optional)

**After PR is merged:**

```bash
# Fetch latest
jj git fetch

# Delete local bookmark
jj bookmark delete feature-name

# Or abandon the changes (safe - still in op log)
jj abandon CHANGE_ID
```

## Key Differences from Git Workflow

### No Branch Protection

- In jj, you work on changes, not branches
- Bookmarks are just pointers, not containers
- Can freely reorganize changes even after describing them

### Squashing is Simpler

```bash
# Git requires interactive rebase
git rebase -i main

# jj just squashes
jj squash
```

### Undoing is Always Safe

```bash
# Made a mistake? Just undo
jj op undo

# Or redo if you undid too much
jj op redo
```

## Integration with GitHub/GitLab

**Jujutsu bookmarks map to git branches:**

- Creating a bookmark in jj creates a branch for git
- Pushing a bookmark updates the corresponding branch
- PRs/MRs work the same way as with git

**Use gh/glab CLI normally:**

```bash
# GitHub CLI works with jj bookmarks
gh pr create --head feature-name

# View PR
gh pr view
```

## When to Use This Skill

Use this skill when:
- Completing feature work in a jj repository
- Ready to push changes and create PR
- Need to organize changes before pushing
- Working with jj bookmarks

Don't use when:
- Project uses pure git (use finishing-a-development-branch)
- Not ready to push (continue working)
- Tests are failing (fix first)

## Common Patterns

### Quick PR from Single Change

```bash
jj describe -m "feat: feature description"
jj bookmark create feature-name
jj git push --bookmark feature-name
gh pr create
```

### Organize Multiple Changes into Logical Sequence

```bash
# View graph
jj log

# Squash experimental attempts
jj squash --from CHANGE_ID

# Split overly large change
jj split

# Reorder if needed (rebase in jj)
jj rebase -r CHANGE_ID -d NEW_PARENT

# Push organized sequence
jj git push --bookmark feature-name
```

### Sync with Upstream

```bash
# Fetch latest
jj git fetch

# Rebase your changes onto latest main
jj rebase -d main

# Push updated changes
jj git push --bookmark feature-name --force
```

## Safety Tips

1. **Always fetch before pushing:**
   ```bash
   jj git fetch
   jj rebase -d main  # If needed
   jj git push
   ```

2. **Review change graph before push:**
   ```bash
   jj log --summary
   ```

3. **Use operation log as safety net:**
   ```bash
   # See what you did
   jj op log

   # Undo if needed
   jj op undo
   ```

4. **Test after squashing:**
   - Squashing can combine incompatible changes
   - Always run tests after organizing changes
