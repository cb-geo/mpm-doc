
# CB-Geo Git Workflow


CB-Geo Git flow is a branch-based workflow that supports teams to develop an integrated codebase for regular deployments of features

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
Before you create a branch for feature development, open a Request for Comments [RFC](https://github.com/cb-geo/mpm/issues/new?template=request_for_comments.md) explaining the feature and the design principle. Once the RFC has been approved, please go ahead and create a new branch. Prefix a feature branchname with `feature/`.

```
git checkout -b feature/parallel/dynamic_loadbalance
```

Feature branches without an RFC will be deleted. 

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

## 4. Open a Pull Request

Pull Requests initiate discussion about your commits. Because they're tightly integrated with the underlying Git repository, anyone can see exactly what changes would be merged if they accept your request. Use the PR template in GitHub and describe the rational behind the PR, link any RFCs / issues. 

You can open a Pull Request at any point during the development process: when you have little or no code but want to share some screenshots or general ideas, when you're stuck and need help or advice, or when you're ready for someone to review your work. Use a draft pull request if you like to have comments from other developers. Use a regular pull request when your work is ready to merge. PRs without tests will not be merged.

```
git push -u origin feature/parallel/dynamic_loadbalance
```


## 5. Discuss and review your code

Once a Pull Request has been opened, the person or team reviewing your changes may have questions or comments. Perhaps the coding style doesn't match project guidelines, the change is missing unit tests, or maybe everything looks great and props are in order. Pull Requests are designed to encourage and capture this type of conversation. You can also continue to push to your branch in light of discussion and feedback about your commits. If someone comments that you forgot to do something or if there is a bug in the code, you can fix it in your branch and push up the change. 

## 6. Merge

Once your pull request has been reviewed and the branch passes your tests, you can deploy your changes to verify them in production. This requires the benchmark tests to pass. Now that your changes have been benchmark verified, it is time to merge your code into the `develop` branch. If your branch causes issues, i.e., nightly benchmark fails, you can roll it back by deploying the existing develop into production.

# Developer guidelines
## Git Guidelines

- Repositories should have a short, memorable, and topical name. Avoid the use
of capital letters and special characters.

- Repositories should only contain source code or source-code-tangent
information. Do not use `git` for storing analysis results, figures, or sample
outputs. They are more appropriately stored on a cloud storage system.

- Repositories should contain a detailed `README.md` file which should include the following:
  - A detailed description of the project
  - Installation/setup instructions
  - Links to detailed documentation
  - At least one interest-provoking figure or example

- Repositories should be intuitively organized (e.g., tests should be located in
a `test` folder, source in a `src` folder). Follow the conventions provided by
your coding language for organizing your projects. When naming directories do
not use capital letters, spaces, and special characters. File names should be meaningful.
Names such as `first analysis.txt`, `version2.txt`, `January2016.txt` should be avoided.
If there are multiple folders each with it’s own input files or project, each folder must
have a README describing the input files / code. 

- Commit after completing a specific task (hour or two of coding). If you
would describe your work with a commit message of "made various changes" then
that commit should be broken across multiple commits where each commit should
describe one and only one of the changes made. Always check if your code compiles
without any errors before pushing.

- Use branches when developing prospective features or implementing breaking
changes. Only merge these branches into `master` after the changes have been
accepted for production and due notice has been provided to users.

- Projects must have a `.gitignore` file, which should include standard temporary files.
Customise your ignore file from a list of sample `.gitignore` file suitable for your project.
[A collection of useful gitignore](https://github.com/github/gitignore). A typical example of
a `.gitignore` file:
  ```
  *~*
  *~*
  *.DS_Store*
  *.swp*
  *.bak*
  ```
  
- Avoid `.gitkeep` (which is not a git feature).

- Avoid hosting large files in your git repository as it increases the time to download
the repo. To remove any large files / bad data accidentally commited to the repo use
[BFG repo cleaner](https://rtyley.github.io/bfg-repo-cleaner/). This is for cleansing
`bad data` from your repository, such as large files and personal credentials.

- Projects are encouraged to have unit tests and continous integrations: CircleCI, Travis CI or Jenkins.

## Git Commit Messages

- Commit messages should be short and to the point. Prefer specific descriptions
over general ones. To reduce boiler plate text such as "bug fix" prefer the use
of an emoji such as :bug:. A list of useful emojis and what they mean are
provided [here](https://cb-geo.github.io/git-course/#/adv/emojis).

- Use the present tense ("Add feature" not "Added feature")

- Use the imperative mood ("Move cursor to..." not "Moves cursor to...")

- Limit the first line to 72 characters or less

- Reference issues and pull requests liberally

- Consider starting the commit message with an applicable emoji :smiley: :


| Commit type                | Emoji                        | Syntax                        |
|:---------------------------|:----------------------------:|:-----------------------------:|
| Initial commit             | :tada:                       | `:tada:`                      |
| Version tag                | :bookmark:                   | `:bookmark:`                  |
| New feature                | :sparkles:                   | `:sparkles:`                  |
| Bugfix                     | :bug:                        | `:bug:`                       |
| Documentation              | :pencil:                     | `:pencil:`                    |
| References                 | :books:                      | `:books:`                     |
| Performance                | :racehorse:                  | `:racehorse:`                 |
| Format changes             | :art:                        | `:art:`                       |
| Tests                      | :rotating_light:             | `:rotating_light:`            |
| Adding a test              | :dart:                       | `:dart:`                      |
| Make a test pass           | :heavy_check_mark:           | `:heavy_check_mark:`          |
| Refactor code              | :hammer:                     | `:hammer:`                    |
| Adding CI build system     | :construction_worker:        | `:construction_worker:`       |
| Continuous Integration     | :dart:                       | `:dart:`                      |
| Security                   | :lock:                       | `:lock:`                      |
| Work in progress           | :construction:               | `:construction:`              |
| Removing a feature         | :heavy_minus_sign:           | `:heavy_minus_sign:`          |
| Adding a feature           | :heavy_plus_sign:            | `:heavy_plus_sign:`           |
| Upgrading dependencies     | :arrow_up:                   | `:arrow_up:`                  |
| Downgrading dependencies   | :arrow_down:                 | `:arrow_down:`                |
| Configuration files        | :wrench:                     | `:wrench:`                    |
| Merging branches           | :twisted_rightwards_arrows:  | `:twisted_rightwards_arrows:` |
| Reverting changes          | :rewind:                     | `:rewind:`                    |
| Breaking changes           | :boom:                       | `:boom:`                      |
| Removing code/files        | :fire:                       | `:fire:`                      |
| Move/rename files/repo     | :truck:                      | `:truck:`                     |
| New idea                   | :bulb:                       | `:bulb:`                      |
| Performance improvements   | :rocket:                     | `:rocket:`                    |
| Memory leaks               | :non-potable_water:          | `:non-potable_water:`         |
| Closing issues/PRs         | :checkered_flag:             | `:checkered_flag:`            |
| Security issue             | :lock:                       | `:lock:`                      |
| Adding logging             | :speaker:                    | `:speaker:`                   |
| Remove logging             | :mute:                       | `:mute:`                      |
| Remove linter warnings     | :shirt:                      | `:shirt:`                     |

## Issues and PRS

* Always use GitHub issues and PR templates, **do not skip** to a blank template.


| Template type              | Purpose                      |
|:---------------------------|:----------------------------:|
| Bug report                 | Filing a bug report / issue  |
| Feature request            | Request to add a new feature |
| Request for comments       | For new ideas / discussions  |


* Describe your feature / issue in as much detail as possible. Do not leave the description blank. 
_Title says it all_ is not a useful description. Explain the context and give additional details. 

* When asking a question follow [guidelines on good practices](https://stackoverflow.com/help/how-to-ask)

* Never create a PR before it is feature complete and passes the CI system.

* Use draft PRs to have discussions on design/architecture. Add label as `discussions` in creating draft PRs.

* Issues and PRs will be automatically closed after 90 days of inactivity.