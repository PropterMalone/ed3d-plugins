#!/usr/bin/env python
"""SessionStart hook for ed3d-plan-and-execute plugin."""
import json
import sys
import os
from pathlib import Path

# Determine plugin root directory
script_dir = Path(__file__).parent.resolve()
plugin_root = script_dir.parent

# Read using-plan-and-execute content
skill_path = plugin_root / "skills" / "using-plan-and-execute" / "SKILL.md"

try:
    with open(skill_path, 'r', encoding='utf-8') as f:
        using_plan_content = f.read()
except Exception as e:
    using_plan_content = f"Error reading using-plan-and-execute skill: {e}"

# Output context injection as JSON
output = {
    "hookSpecificOutput": {
        "hookEventName": "SessionStart",
        "additionalContext": (
            "<EXTREMELY_IMPORTANT>\n"
            "**The content below is from skills/using-plan-and-execute/SKILL.md - "
            "your introduction to using skills:**\n\n"
            f"{using_plan_content}\n"
            "</EXTREMELY_IMPORTANT>"
        )
    }
}

print(json.dumps(output))
sys.exit(0)
