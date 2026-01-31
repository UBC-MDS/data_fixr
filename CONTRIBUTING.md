# Contributing

Contributions of all kinds are welcome for the data_fixr package and are greatly appreciated!
Every little bit helps, and credit will always be given.

## Branching and Workflow

This project follows a Github Flow Workflow.

- The main branch always contains stable, production-ready code
- Direct commits to the 'main' branch are prohibited.
- All work should be conducted on short-lived branches created from 'main'.
- Branches should be named using appropriate prefixes such as 'feat-' or 'fix-'.
- Changes must be proposed via pull request to the main branch.
- Each Pull request must be reviewed by at least one other team member and granted approval before merging. 

## Example Contributions

You can contribute in many ways, for example:

* [Report bugs](#report-bugs)
* [Fix Bugs](#fix-bugs)
* [Implement Features](#implement-features)
* [Write Documentation](#write-documentation)
* [Submit Feedback](#submit-feedback)

### Report Bugs

Report bugs at https://github.com/UBC-MDS/data_fixr/issues.

**If you are reporting a bug, please follow the template guidelines. The more
detailed your report, the easier and thus faster we can help you.**

### Fix Bugs

Look through the GitHub issues for bugs. Anything labelled with `bug` and
`help wanted` is open to whoever wants to implement it. When you decide to work on such
an issue, please assign yourself to it and add a comment that you'll be working on that,
too. If you see another issue without the `help wanted` label, just post a comment, the
maintainers are usually happy for any support that they can get.

### Implement Features

Look through the GitHub issues for features. Anything labelled with
`enhancement` and `help wanted` is open to whoever wants to implement it. As
for [fixing bugs](#fix-bugs), please assign yourself to the issue and add a comment that
you'll be working on that, too. If another enhancement catches your fancy, but it
doesn't have the `help wanted` label, just post a comment, the maintainers are usually
happy for any support that they can get.

### Write Documentation

data_fixr could always use more documentation, whether as
part of the official documentation, in docstrings, or even on the web in blog
posts, articles, and such. Just
[open an issue](https://github.com/UBC-MDS/data_fixr/issues)
to let us know what you will be working on so that we can provide you with guidance.

### Submit Feedback

The best way to send feedback is to file an issue at
https://github.com/UBC-MDS/data_fixr/issues. If your feedback fits the format of one of
the issue templates, please use that. Remember that this is a volunteer-driven
project and everybody has limited time.

## Get Started!

Ready to contribute? Here's how to set up data_fixr for
local development.

1. Fork the https://github.com/UBC-MDS/data_fixr
   repository on GitHub.
2. Clone your fork locally (*if you want to work locally*)

    ```shell
    git clone git@github.com:your_name_here/data_fixr.git
    ```

3. [Install hatch](https://hatch.pypa.io/latest/install/).

4. Create a branch for local development using the default branch (typically `main`) as a starting point. Use `fix` or `feat` as a prefix for your branch name.

    ```shell
    git checkout main
    git checkout -b fix-name-of-your-bugfix
    ```

    Now you can make your changes locally.

5. When you're done making changes, apply the quality assurance tools and check
   that your changes pass our test suite. This is all included with Hatch.

    ```shell
    hatch run test:run
    ```

6. Commit your changes and push your branch to GitHub. Please use [semantic
   commit messages](https://www.conventionalcommits.org/).

    ```shell
    git add .
    git commit -m "fix: summarize your changes"
    git push -u origin fix-name-of-your-bugfix
    ```

7. Open the link displayed in the message when pushing your new branch in order
   to submit a pull request.

## Pull Request Guidelines

Before you submit a pull request, check that it meets these guidelines:

1. The pull request should include tests.
2. If the pull request adds functionality, the docs should be updated. Put your
   new functionality into a function with a docstring.
3. Your pull request will automatically be checked by the full test suite.
   It needs to pass all of them before it can be considered for merging.

## Project Retrospective

Here we present a retrospective analysis of the *data_fixr* project, developed as part of **2025–26 DSCI-524 Group 3**.  
The goal of this retrospective is to reflect on our planning accuracy, workflow organization, tooling decisions, and collaboration practices, using evidence collected from GitHub Projects across all four milestones.

---

### Evidence Used

This retrospective is grounded in data from the following GitHub Project views and insights:

- **Milestone Progress** (Table view grouped by milestone)
- **Burn-up / Completion Chart** (Insights view grouped by milestone and status)
- **Team Workload** (Table view grouped by assignee, filtered to completed tasks)

These views were used to assess scope evolution, bottlenecks, and contribution balance.

---

### Milestone Progress and Planning Accuracy

Using the **Milestone Progress** view, we observed that workload was the most during Milestone 2.

- **Milestone 1** primarily focused on project setup, writing function documentations, and scaffolding. (Count of Items: 13)
- **Milestone 2** introduced function implementations and unit testing, with a moderate increase in issue count. (Count of Items: 17)
- **Milestone 3** showed a moderate amount of issues related to CI/CD configuration, documentation builds, and deployment previews. (Count of Items: 13)
- **Milestone 4** had fewer issues overall, but required higher coordination and review effort.

**Reflection:**  
Infrastructure-related tasks, particularly CI/CD and documentation deployment, were underestimated during early planning. While core function development proceeded smoothly, automation and deployment required more iterative debugging than anticipated.

---

### Workflow and Bottlenecks

The **Burn-up / Completion Chart** revealed temporary bottlenecks during Milestone 3.

- Several issues accumulated in the *In Progress* and *Review* states while CI/CD workflows were being debugged.

**Reflection:**  
CI/CD setup became the primary bottleneck, delaying dependent tasks. Earlier experimentation with deployment workflows could have reduced friction later in the project. Distribution of Tasks was even in Milestone 3 aswell but that was just the nature of the tasks.

---

### Team Contributions and Bus Factor

The **Team Workload** view showed a generally balanced distribution of completed issues across team members.

- Some contributors had fewer issues assigned but worked on higher-complexity tasks, such as CI/CD workflows and deployment previews.
- Milestone 3 caused disparity in the distribution of tasks which showed some members to have lower amount of tasks than others.
- Other contributors handled multiple smaller issues related to documentation and testing.

**Reflection:**  
While issue counts were not perfectly uniform, the overall workload was balanced when task complexity was considered.

---

### Retrospective Summary (DAKI)

### Drop
- Using Slack for communication issues rather than Github issues.

### Add
- Earlier CI/CD prototyping during the project timeline.
- Posting documentation preview links directly in pull request comments.
- Clearer pull request templates to standardize reviews.

### Keep
- Issue-based task ownership with clear assignees.
- Writing unit tests alongside function implementations.
- Using GitHub Projects to track progress across milestones.

### Improve
- Milestone scoping to better account for infrastructure and automation complexity.
- Cross-training team members on CI/CD workflows to reduce bus-factor risk.

---

### Tools, Infrastructure, and Scaling Considerations

Throughout the project, we applied several development tools and practices introduced in this course, including GitHub Actions for testing and deployment, GitHub Projects for task tracking, and structured branching workflows.

If this project were to be scaled up or extended (e.g., as a capstone project), we would:
- Introduce additional CI checks such as linting and formatting enforcement.
- Apply stricter branch protection rules earlier.
- Expand documentation automation and preview tooling.
- Distribute infrastructure knowledge more evenly across the team.

These improvements would enhance maintainability, reliability, and collaboration efficiency as project complexity grows.

## Code of Conduct

Please note that the data_fixr package is released with a [Code of Conduct](https://github.com/UBC-MDS/data_fixr/blob/main/CODE_OF_CONDUCT.md). By contributing to this project you agree to abide by its terms.
