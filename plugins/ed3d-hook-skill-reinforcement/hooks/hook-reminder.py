#!/usr/bin/env python
"""UserPromptSubmit hook for ed3d-hook-skill-reinforcement plugin."""
import json
import sys

output = {
    "hookSpecificOutput": {
        "hookEventName": "UserPromptSubmit",
        "additionalContext": (
            "<EXTREMELY_IMPORTANT>\n"
            "Before responding to this prompt, consider whether you have any skills in "
            "<available_skills /> that apply. If you do and they have not been activated "
            "in this session, use the Skill tool to activate them.\n"
            "</EXTREMELY_IMPORTANT>"
        )
    }
}

print(json.dumps(output))
sys.exit(0)
