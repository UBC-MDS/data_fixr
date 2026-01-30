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

## Retrospective

In every project, whether successful or challenging, looking back and analyzing how the work unfolded is critical for continuous improvement. In agile software development, this practice is known as a **retrospective**.

This project encourages structured retrospectives at the end of major milestones to reflect on planning accuracy, tooling, collaboration practices, and workflow bottlenecks, with a focus on actionable improvements for future work.

### Retrospective Framework (DAKI)

For retrospectives, we recommend using the **DAKI** framework:

- **Drop**: Practices, tools, or workflows that did not work well and should be discontinued.
- **Add**: New practices, tools, or processes that should be introduced in future work.
- **Keep**: Practices that worked well and should be continued.
- **Improve**: Existing practices that were helpful but need refinement.

This framework helps keep reflections concise, structured, and actionable.

---

### Creating GitHub Project Views to Support Retrospectives

Retrospectives should be grounded in evidence from the project’s GitHub tracking data. Before analysis, ensure good **data hygiene** in the GitHub Project board.

#### Data Hygiene Checklist

- **Status Check**: All completed tasks are moved to the `Done` column.
- **Attribution**: Every issue has an assigned contributor.
- **Clarity**: Tasks are appropriately split or cross-linked if necessary.
- **Timeline**: Every issue is assigned to a milestone (M1, M2, M3, M4).

Bulk-editing in the Table view is encouraged to correct metadata efficiently.

---

### Analytical Views

#### Milestone Progress (Velocity)

To assess how project scope evolved over time we created a view to assess our milestone progress.

This view helps answer questions such as:
- How did the scope change from one milestone to the next?
   
- Were later milestones more work-intensive than expected?

---

## Code of Conduct

Please note that the data_fixr package is released with a [Code of Conduct](https://github.com/UBC-MDS/data_fixr/blob/main/CODE_OF_CONDUCT.md). By contributing to this project you agree to abide by its terms.
