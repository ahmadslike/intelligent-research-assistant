# Deploy Check

Check if the project is ready for deployment:

1. Verify all required files exist: requirements.txt, .env.example, CLAUDE.md
2. Check that venv exists and dependencies are installed
3. Verify the FastAPI server starts without errors
4. Check that all Python files have no syntax errors
5. Verify .gitignore includes .env and api-keys.txt
6. Report a checklist of what passed and what needs fixing
