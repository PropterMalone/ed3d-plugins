#!/usr/bin/env python
"""SessionStart hook for ed3d-basic-agents plugin."""
import json
import sys

output = {
    "hookSpecificOutput": {
        "hookEventName": "SessionStart",
        "additionalContext": (
            "<EXTREMELY_IMPORTANT>\n"
            "Whenever instructed to use a 'general-purpose' agent, you MUST invoke the "
            "'using-generic-agents' skill, which will guide you on how to correctly use a generic agent.\n"
            "</EXTREMELY_IMPORTANT>"
        )
    }
}

print(json.dumps(output))
sys.exit(0)
