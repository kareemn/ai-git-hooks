# AI Git Hooks

This repository contains a Git commit hook that uses OpenAI to automatically generate commit messages based on the changes made in the commit.

<p align="center">
<img src="https://github.com/kareemn/ai-git-hooks/blob/master/demo.gif" width="500">
</p>

## How it works

The prepare-commit-msg script is a Git commit hook that is triggered automatically before each commit. It extracts the changes made in the commit and passes them to the create_git_message.py script, which uses the OpenAI API to generate a commit message based on the changes. The generated commit message is then added to the commit.

## Requirements
- Python 3
- Git
- OpenAI API key

## Setup
Clone the repository:
```bash
git clone https://github.com/kareemn/ai-git-hooks.git
```

Install the required Python packages:
```
pip install openai
```
Set your OpenAI API key:
```
export OPENAI_API_KEY=<your-api-key>
```
Make the prepare-commit-msg script executable:
```
chmod +x prepare-commit-msg
```

Install the prepare-commit-msg hook:
```
cp prepare-commit-msg <new-repo>/.git/hooks/prepare-commit-msg
cp create_git_message.py <new-repo>/.git/hooks/create_git_message.py
```

## Usage

Simply make changes to your repository and commit them as usual. The Git commit hook will automatically generate a commit message based on the changes you made.

Note that the generated commit message may not always be perfect and may require some editing. However, it should provide a good starting point for your commit message and save you time and effort.

