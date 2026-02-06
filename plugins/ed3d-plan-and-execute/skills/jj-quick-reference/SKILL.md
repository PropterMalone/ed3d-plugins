---
name: jj-quick-reference
description: Quick reference for common Jujutsu commands and git equivalents - use for fast lookup when working with jj
---

# Jujutsu Quick Reference

## Daily Commands

### Status & History

```bash
jj status              # Show working copy status
jj st                  # Short form
jj log                 # Show change graph
jj log --summary       # Show with file changes
jj show               # Show current change details
```

### Creating Changes

```bash
jj new                 # Create new change (working copy moves to it)
jj new -m "message"    # Create with description
jj new main            # Create new change from main
jj new --insert-before # Insert change between current and parent
```

### Describing Changes

```bash
jj describe                    # Open editor for description
jj describe -m "message"       # Set description directly
jj describe CHANGE_ID          # Describe specific change
```

### Moving Between Changes

```bash
jj edit CHANGE_ID      # Switch to different change
jj edit main           # Switch to bookmark
```

### Organizing Changes

```bash
jj squash              # Squash current change into parent
jj squash --from ID    # Squash specific change
jj split               # Split current change interactively
jj abandon CHANGE_ID   # Mark change as abandoned (still in op log)
```

### Bookmarks (Branches)

```bash
jj bookmark list                # List all bookmarks
jj bookmark create name         # Create bookmark at current change
jj bookmark set name            # Move/create bookmark to current change
jj bookmark delete name         # Delete bookmark
jj bookmark track name@remote   # Track remote bookmark
```

### Remote Operations

```bash
jj git fetch                    # Fetch from all remotes
jj git push                     # Push current bookmark
jj git push --bookmark name     # Push specific bookmark
jj git push --all               # Push all bookmarks
jj git push --change CHANGE_ID  # Create change-specific branch
```

### Rebasing

```bash
jj rebase -d DESTINATION       # Rebase current change
jj rebase -r CHANGE -d DEST    # Rebase specific change
jj rebase -s SOURCE -d DEST    # Rebase change and descendants
```

### Undoing Operations

```bash
jj op log              # Show operation history
jj op undo             # Undo last operation
jj op redo             # Redo after undo
jj op restore OPERATION_ID  # Restore specific operation
```

## Git Equivalents

| Task | Git | Jujutsu |
|------|-----|---------|
| Clone repo | `git clone URL` | `jj git clone URL` |
| Init repo | `git init` | `jj git init --git-repo=.` |
| Status | `git status` | `jj status` |
| Log | `git log` | `jj log` |
| New branch | `git checkout -b NAME` | `jj new -m "msg"` + `jj bookmark create NAME` |
| Switch branch | `git checkout NAME` | `jj edit NAME` |
| Commit | `git add .` + `git commit -m "msg"` | `jj describe -m "msg"` |
| Amend commit | `git add .` + `git commit --amend` | Just edit and `jj describe` again |
| Interactive rebase | `git rebase -i` | `jj squash` / `jj split` / `jj rebase` |
| Push | `git push` | `jj git push` |
| Fetch | `git fetch` | `jj git fetch` |
| Pull | `git pull` | `jj git fetch` + `jj rebase -d main` |
| Reset hard | `git reset --hard` | `jj op undo` |
| Stash | `git stash` | `jj new` (create temp change) |
| Cherry-pick | `git cherry-pick` | `jj rebase -r CHANGE_ID -d DEST` |
| Undo commit | `git reset HEAD~` | `jj abandon` or `jj op undo` |

## Advanced Patterns

### Work on Multiple Changes Simultaneously

```bash
# Create change for feature A
jj new -m "feat: A"
# ... make changes ...

# Create sibling change for feature B
jj new main -m "feat: B"
# ... make changes ...

# Switch back to A
jj edit CHANGE_ID_A
# ... continue work ...

# Both changes exist independently
```

### Clean Up Messy History

```bash
# View current state
jj log

# Squash experimental changes into main work
jj squash --from EXPERIMENTAL_ID

# Split overly large change
jj edit LARGE_CHANGE_ID
jj split

# Reorder changes
jj rebase -r CHANGE_ID -d NEW_PARENT
```

### Sync with Remote

```bash
# Fetch latest
jj git fetch

# Rebase your work onto latest main
jj rebase -d main@origin

# Push updated changes (force if rebased)
jj git push --bookmark feature-name --force
```

### Recover from Mistakes

```bash
# See what you did
jj op log

# Undo last operation
jj op undo

# Or restore to specific point
jj op restore OPERATION_ID
```

## Configuration Tips

### Useful Aliases

Add to `~/.jjconfig.toml`:

```toml
[aliases]
st = ["status"]
l = ["log", "-r", "::@"]
ll = ["log", "--summary"]
sync = ["git", "fetch"]
```

### Default Push Behavior

```toml
[git]
push-bookmark-prefix = "karls/"  # Prefix remote bookmarks
auto-local-bookmark = true        # Auto-create local bookmarks
```

### UI Customization

```toml
[ui]
default-command = "log"
pager = "less -FRX"
```

## Change ID Format

- **Full ID:** `qpvuntsmwlqtpsluzzsnyyzlqlkwuwya`
- **Short ID:** `qpvuntsm` (first 8 chars, usually unique)
- **Symbol:** `@` means working copy change
- **Symbol:** `@-` means parent of working copy

## Common Workflows

### Start Feature Work

```bash
jj git fetch
jj new main -m "feat: description"
jj bookmark create feature-name
# ... make changes ...
jj git push --bookmark feature-name
```

### Quick Fix

```bash
# Make changes directly in working copy
jj describe -m "fix: bug description"
jj bookmark create fix-name
jj git push --bookmark fix-name
```

### Review Before Push

```bash
jj log --summary              # See all changes
jj show                       # See current change details
jj squash                     # Combine if needed
jj git push --bookmark name   # Push when ready
```

## When to Use This Skill

Use for quick lookup of:
- Common jj commands
- Git to jj equivalents
- Advanced patterns
- Configuration options

Don't use for:
- Detailed workflow guidance (use using-jj-workflow)
- Finishing work (use finishing-jj-work)
