#!/bin/bash
# PostToolUse hook: runs black formatter on .py files after Write or Edit
INPUT=$(cat)
FILE=$(echo "$INPUT" | python -c "import sys, json; d=json.load(sys.stdin); print(d.get('tool_input', {}).get('file_path', ''))" 2>/dev/null)

if [[ "$FILE" == *.py ]]; then
  python -m black "$FILE" 2>/dev/null
fi
exit 0
