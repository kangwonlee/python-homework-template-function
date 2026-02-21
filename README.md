# Python Homework Template
Please work on : `exercise.py`

## Purpose:

Why do we want to do this assignment? What do we want to accomplish?

## Description:

* Describe homework here

## Instructions:

* How to do this homework
* This repository is for a python assignment writing a function in `exercise.py`.
* `classroom.yml` file is at `.github/workflows/` folder. `.github` folder is hidden on the Linux operating system but will be visible on the Github repository.
* Please set `vars.PYTHON_GRADER_???` (replace `???` with assignment identifier) in the repository settings (Settings > Secrets and Variables > Actions > Variables) to your grader image (e.g., `ghcr.io/your-org/python-pytest-301:latest`).
* Set your AI feedback natural language in `classroom.yml`.

## Example Run:

* input
```
input example here
```
* output
```
----------
output example here
```

## Tips:

* please add some more hints here

__Happy coding!__

## Grading Criteria

| Criteria | Points |
|:--------:|:------:|
| Is the code written according to Python syntax? | 1 |
| Does code respect style guidelines? | 1 |
| Does the code satisfy the requirements? | 3 |

## Instructor Setup

This template is designed for use with [GitHub Classroom](https://classroom.github.com/). Before distributing to students, configure the following in your GitHub organization or repository settings.

### How the Two-Repo Pattern Works

Each assignment requires **two** repositories:

1. **Homework template** (this repo) — student-facing, contains the assignment skeleton (`exercise.py`) and the `classroom.yml` workflow that pulls the grader image and runs tests on student pushes.
2. **Grader template** ([python-pytest-template](https://github.com/kangwonlee/python-pytest-template)) — instructor-facing, contains pytest test files and a Dockerfile. Its CI builds and publishes a grader Docker image to GHCR.

### Required Secrets

Set these in **Settings > Secrets and variables > Actions > Secrets** at the organization level (recommended) or per repository.

#### `CR_PAT` (required)

A GitHub Personal Access Token used to pull the grader Docker image from GHCR.

1. Go to **GitHub > Settings (user) > Developer settings > Personal access tokens > Fine-grained tokens**.
2. Click **Generate new token**.
3. Set the following permissions:

| Permission | Access | Purpose |
|:----------:|:------:|:--------|
| Packages   | Read   | Pull grader Docker images from GHCR |

4. Copy the token and save it as a repository or organization secret named `CR_PAT`.

> If using GitHub Classroom, set `CR_PAT` as an **organization secret** so all student repos inherit it automatically.

#### LLM API Keys (at least one required)

The AI tutor step provides personalized feedback to students. At least one key must be set. The workflow validates this and fails early if none are configured.

| Secret Name | Service | Where to Obtain |
|:-----------:|:-------:|:----------------|
| `CLAUDE_API_KEY` | Anthropic Claude | https://console.anthropic.com/ |
| `GOOGLE_API_KEY` | Google Gemini | https://aistudio.google.com/ |
| `XAI_API_KEY` | xAI Grok | https://console.x.ai/ |
| `NVIDIA_NIM_API_KEY` | NVIDIA NIM | https://build.nvidia.com/ |
| `PERPLEXITY_API_KEY` | Perplexity | https://perplexity.ai/settings/api |

#### `DEFAULT_MODEL` (optional)

Specifies the preferred LLM model. If unset, the AI tutor defaults to Gemini or uses whichever single key is available.

### Repository Variable

Set in **Settings > Secrets and variables > Actions > Variables** tab.

#### `PYTHON_GRADER_???`

Replace `???` with your assignment identifier (e.g., `PYTHON_GRADER_301` for assignment 301). The value is the full GHCR image URL of the grader, e.g.:

```
ghcr.io/your-org/python-pytest-301:latest
```

If this variable is not set, the workflow falls back to auto-constructing the URL as `ghcr.io/{owner}/python-pytest-{assignment_num}:latest`, where `{assignment_num}` is extracted from the repository name.

### Customizing for a New Assignment

1. Use this template to create a new repository (click **Use this template** on GitHub).
2. Edit `README.md` — fill in the Purpose, Description, Instructions, Example Run, and Tips sections.
3. Edit `exercise.py` — provide starter code or an empty skeleton for students.
4. Update the grading criteria table if point allocations differ.
5. Set `INPUT_EXPLANATION-IN` in `classroom.yml` to the desired feedback language (default: `"English"`).
6. Set the `CR_PAT` secret, at least one LLM API key, and the `PYTHON_GRADER_???` variable.

``From here is common to all assignments.``

## Submission

1. Modify the contents of the `exercise.py` file to write your program.
2. Use the GitHub online editor to commit and push your changes. (See below for detailed instructions)
3. At the Actions tab of your Github repository, please check the result.

## How to Use the GitHub Online Editor

* Press the <kbd>.</kbd> key while viewing the files in your repository on GitHub. This will launch a web version of VS Code.
* Make your changes to the `exercise.py` file.
* To commit your changes, click on the branch icon on the left sidebar (the third icon after the magnifying glass).
* Click the "+" sign next to the filename to stage your changes.
* Write a brief description of your changes in the text box above.
* Click "Commit & Push."
* Click "Back to Repository" on the branch icon to return to your repository.

## Writing Descriptive Git Commit Messages

* To help you develop a better coding habits, we encourage descriptive Git commit messages when committing changes to your repositroy.
* A good commit message clearly explains what you changed and why, making it easier for you to understand your work later.

### Guidelines for Commit Messages
* Describe the change more specifically, e.g., "Add factorial function to exercise.py" or "Fix bug in sum calculation".
* Use Action Verbs: Start with words like "Add", "Fix", "Update", or "Refactor".

* Avoid Vague Messages: Messages like "update" or "fix" can be too general.

* Keep It Concise: Aim for 15-50 characters, but ensure clarity.
* Examples 예:
  * Good: "Add unit tests for sort function in exercise.py"
  * Bad: "update", "fix 1", "changed file"

### Why It Matters
* Clear commit messages improve collaboration, debugging, and code review in real-world projects.

### Resources
* [How to Write a Git Commit Message](https://cbea.ms/git-commit/)

## NOTICE REGARDING STUDENT SUBMISSIONS

* Your submissions for this assignment may be used for various educational purposes. These purposes may include developing and improving educational tools, research, creating test cases, and training datasets.

* The submissions will be anonymized and used solely for educational or research purposes. No personally identifiable information will be shared.

* If you do not wish to have your submission used for any of these purposes, please inform the instructor before the assignment deadline.

## Acknowledgments

* The template for this assigment is registered as a part of #C-2025-016393 in the Korea Copyright Commission.

``Until here is common to all assignments.``
