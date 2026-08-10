# Contribution Guidelines for `apis`

## What This Repo Is

This is the **central API testing & documentation repo** for the team. It is not tied to a single project — every developer, across every project, uses it whenever they add or change an API.

- API collections are maintained here using **[Bruno](https://www.usebruno.com/)**.
- Documentation for every collection is generated automatically on push (see `.github/workflows/docs.yml`).
- Each project's actual source code lives in its own repo on **Azure DevOps**. This repo is separate from those — you will typically have two repos checked out for one piece of work: your project's code repo, and this one.

Work/task management for all projects happens on **Azure DevOps Boards (Scrum)**, regardless of where the code itself is hosted. Every change — in your project repo or in this repo — must trace back to the same **Work Item**.

---

## When You Must Update This Repo

If your task **adds, changes, or removes an API endpoint**, you must update this repo in addition to your project's code repo:

1. Clone this repo (if you haven't already) and open it in **Bruno**.
2. Add/update the request(s) in the relevant collection under `collections/`, and update `environments/` if variables changed.
3. Verify the request works against the API in Bruno.
4. Commit and push your changes here — following the same branch/commit/PR rules below, using the **same Work Item ID** as your code change in the project repo.

Treat the code change and the collection change as one task with two repos, not two separate tasks.

---

## Task Workflow

- All work is tracked as a **Work Item** on the Azure DevOps Scrum board (Task, User Story, or Bug — whichever fits).
- Move your work item from **New/To Do** → **In Progress** when you start working on it.
- Every branch, commit, and PR — in both the project repo and this repo — must reference the same **Work Item ID**.
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
- If this PR pairs with a code change in a project repo, link that PR too in the description for traceability.

---

## Linking to Azure Boards

Mentioning `#{WORK_ITEM_ID}` in a commit message or PR title/description automatically links that commit/PR to the corresponding Azure Boards work item — no manual linking needed.

- This creates a **link**, not a status change. Still move the work item to **Review** when the PR is opened, and to **Done** yourself once it's merged — mentioning the ID does not transition the board state on its own.
- Add the **PR link** as a comment/attachment on the work item for traceability.

---

## Adding or Updating API Collections

- New or changed collections go under `collections/`, environments under `environments/`.
- Make changes in Bruno, not by hand-editing the collection files, so the format stays consistent.
- Documentation is generated automatically by the `docs` workflow on push — you do not need to regenerate docs manually. Just make sure your collection is valid before pushing.
- Follow the same branch/commit/PR rules above for collection and environment changes — they are tracked like any other task.

---

## Useful Links

- [Bruno](https://www.usebruno.com/)
- [Commitlint](https://commitlint.js.org/)
- Azure DevOps Boards — team Scrum board (see your project's board URL)

---

## Contributed by

- [Mohammad Mehedi Hasan Shuvo](https://github.com/shuvo-asl)
