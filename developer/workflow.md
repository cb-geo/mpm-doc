# CB-Geo Developer Workflow

CB-Geo flow is a branch-based workflow that supports teams to develop an integrated codebase for regular deployments of features. Based on [Atlassian](https://www.atlassian.com/blog/git/simple-git-workflow-is-simple) and [GitHub Flow](https://guides.github.com/introduction/flow/) documents.

## 1. Checkout develop

Start by pulling down the latest changes from `develop`

```
git checkout develop
git pull origin develop
```

## 2. Create a branch

When you're working on a project, you're going to have a bunch of different features or ideas in progress at any given time – some of which are ready to go, and others which are not. Branching exists to help you manage this workflow.

When you create a branch in your project, you're creating an environment where you can try out new ideas. Changes you make on a branch don't affect the master branch, so you're free to experiment and commit changes, safe in the knowledge that your branch won't be merged until it's ready to be reviewed by someone you're collaborating with.

### Branches for a bug-fix

All hot-fix branches should be prefixed with `hotfix/`. Create a new branch whenever a hotfix is needed. Branch off to isolate an issue and fix. 


### Branches for feature development
Before you create a branch for feature development, open a Request for Comments [RFC](https://github.com/cb-geo/mpm/issues/new?template=request_for_comments.md) explaining the feature and the design principle. **RFC should contain code snippets, class outlines, inheritance schemes, outline of new features.** Without this detail RFCs are not useful to discuss ideas. Merely mentioning a new feature will be implemented is NOT a useful RFC. It would become a placeholder for your PR and not a design and discussion board, before the actual implementation of the code. Once the RFC has been approved, please go ahead and create a new branch. Prefix a feature branchname with `feature/`.

```
git checkout -b feature/parallel/dynamic_loadbalance
```

Feature branches without an RFC will be deleted. All major RFCs should have an associated milestone with a deadline. This helps others know when a particular feature will be ready.

### Feature pull request
For a small feature addition without a prior RFC, you may choose to create a PR from your personal fork of the project. However, this **feature PR must have sections on Design Detail, Rationale, and Alternatives.**

## 3. Add commits

Once your branch has been created, it's time to start making changes. Whenever you add, edit, or delete a file, you're making a commit, and adding them to your branch. This process of adding commits keeps track of your progress as you work on a feature branch.

Commits also create a transparent history of your work that others can follow to understand what you've done and why. Each commit has an associated commit message, which is a description explaining why a particular change was made. Furthermore, each commit is considered a separate unit of change. This lets you roll back changes if a bug is found, or if you decide to head in a different direction. Do not cluster separate changes together. Follow the git message guidelines outlined in this document.


Keep your feature branch fresh and up to date with the latest changes in `develop`, use rebase. Every week during the development update the feature branch with the latest changes in develop. 

```
git fetch origin
git rebase origin/develop
```

In the (somewhat less common) case where other people are also working on the same shared remote feature branch, also rebase changes coming from it:

```
git rebase origin/feature/parallel/dynamic_loadbalance
```

At this point solve any conflicts that come out of the rebase.

Resolving conflicts during the rebase allows you to have always clean merges at the end of the feature development. It also keeps your feature branch history clean and focused without spurious noise.

**Avoid pushing code which does not build locally.**

## 4. Open a Pull Request

Pull Requests initiate discussion about your commits. Because they're tightly integrated with the underlying Git repository, anyone can see exactly what changes would be merged if they accept your request. Use the PR template in GitHub and describe the rational behind the PR, link any RFCs / issues. 

You can open a Pull Request at any point during the development process: when you have little or no code but want to share some screenshots or general ideas, when you're stuck and need help or advice, or when you're ready for someone to review your work. Use a draft pull request if you like to have comments from other developers. Use a regular pull request when your work is ready to merge. PRs without tests will not be merged.

```
git push -u origin feature/parallel/dynamic_loadbalance
```


## 5. Discuss and review your code

Once a Pull Request has been opened, the person or team reviewing your changes may have questions or comments. Perhaps the coding style doesn't match project guidelines, the change is missing unit tests, or maybe everything looks great and props are in order. Pull Requests are designed to encourage and capture this type of conversation. You can also continue to push to your branch in light of discussion and feedback about your commits. If someone comments that you forgot to do something or if there is a bug in the code, you can fix it in your branch and push up the change. 

You are strongly encouraged to get your code reviewed by a reviewer as soon as there is any code to review, to get a second opinion on the chosen solution and implementation, and an extra pair of eyes looking for bugs, logic problems, or uncovered edge cases. 

> The responsibility of the reviewer

Review the merge request thoroughly. **Always use encouraging language on comments and reviews.** Request for more information to understand the reasoning behind the change and do not dismiss any code without a comment. When you are confident that it meets all requirements, you should:

    * Click the Approve button.
    * Advise the author their merge request has been reviewed and approved.

## 6. Merge

Once your pull request has been reviewed and the branch passes your tests, you can deploy your changes to verify them in production. This requires the benchmark tests to pass. Now that your changes have been benchmark verified, it is time to merge your code into the `develop` branch. If your branch causes issues, i.e., nightly benchmark fails, you can roll it back by deploying the existing develop into production.
