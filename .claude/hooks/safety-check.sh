#!/bin/bash
# PreToolUse hook: blocks file deletion commands (not text that mentions them)
INPUT=$(cat)
RESULT=$(echo "$INPUT" | python -c "
import sys, json, re

d = json.load(sys.stdin)
command = d.get('tool_input', {}).get('command', '')

# Strip heredoc body content so commit messages don't trigger false positives
# Matches: <<'EOF' or <<EOF ... EOF
command_clean = re.sub(r\"<<['\\\"]?\\w+['\\\"]?.*\", '', command, flags=re.DOTALL)

# Match dangerous commands only when they appear as actual shell commands:
# at start of string, or after ; & | operators
if re.search(r'(?:^|[;&|])\s*(?:rm|del|Remove-Item)[\s\-]', command_clean, re.MULTILINE | re.IGNORECASE):
    print('BLOCK')
" 2>/dev/null)

if [ "$RESULT" = "BLOCK" ]; then
  echo '{"hookSpecificOutput":{"hookEventName":"PreToolUse","permissionDecision":"deny","permissionDecisionReason":"⚠️ File deletion blocked by safety-check hook. Command contains rm/del/Remove-Item."}}'
  exit 2
fi
exit 0
