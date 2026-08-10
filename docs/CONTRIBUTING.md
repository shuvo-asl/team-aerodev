# Contribution Guidelines for `apis`

This repository holds our API collections, environments, and the workflow that auto-generates API documentation on every push. It is a shared, multi-purpose repo, so please follow this guide when contributing.

We use **Git & GitHub** for version control and **Azure DevOps Boards (Scrum)** for work/task management. Every change must trace back to a work item — no work item, no branch, no PR.

---

## Task Workflow

- All work is tracked as a **Work Item** on the Azure DevOps Scrum board (Task, User Story, or Bug — whichever fits).
- Move your work item from **New/To Do** → **In Progress** when you start working on it.
- Every branch, commit, and PR must reference the **Work Item ID**.
- Create a branch using the following convention:
  - `feature/{WORK_ITEM_ID}-short-title`
  - `bugfix/{WORK_ITEM_ID}-short-title`
  - Example → `feature/1234-add-invoice-endpoint`
  - Use `-` instead of spaces; no `_`.

---

## Commit Rules

- Follow [Commitlint](https://commitlint.js.org/) conventions for commit messages.
- Reference the work item in the commit message so it links back to the board, e.g.:
  ```
  feat: add invoice creation endpoint (#1234)
  ```

---

## Pull Request (PR) Workflow

- After finishing your task, open a **Pull Request** from your branch into the parent branch.
- **PR Title** must start with the Work Item ID:
  ```
  [#1234] Short description of the task
  ```
- **PR Description** must use the [PR template](../.github/pull_request_template.md) and include:
  - A summary of the change / changelog.
  - The linked **Work Item ID** (`#1234`) so it auto-links on the Azure Boards work item.
  - Reviewers assigned.
  - Labels assigned.

---

## Linking to Azure Boards

Mentioning `#{WORK_ITEM_ID}` in a commit message or PR title/description automatically links that commit/PR to the corresponding Azure Boards work item — no manual linking needed.

- This creates a **link**, not a status change. Still move the work item to **Review** when the PR is opened, and to **Done** yourself once it's merged — mentioning the ID does not transition the board state on its own.
- Add the **PR link** as a comment/attachment on the work item for traceability.

---

## Adding or Updating API Collections

- New or changed collections go under `collections/`, environments under `environments/`.
- Documentation is generated automatically by the `docs` workflow on push — you do not need to regenerate docs manually. Just make sure your collection is valid before pushing.
- Follow the same branch/commit/PR rules above for collection and environment changes — they are tracked like any other task.

---

## Useful Links

- [Commitlint](https://commitlint.js.org/)
- Azure DevOps Boards — team Scrum board (see your project's board URL)

---

## Contributed by

- [Mohammad Mehedi Hasan Shuvo](https://github.com/shuvo-asl)
