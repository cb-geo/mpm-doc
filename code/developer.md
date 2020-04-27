# Developer guidelines

## Guidelines

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

