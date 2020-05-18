# Onboarding CB-Geo MPM developer 

## Code repository
The primary CB-Geo code repository is on [GitHub](https://github.com/cb-geo/). There are following code repositories related to CB-Geo MPM.

[MPM Code base](https://github.com/cb-geo/mpm/)

[MPM Benchmarks file for simple test cases](https://github.com/cb-geo/mpm-benchmarks)

[MPM Container for reproducible builds](https://github.com/cb-geo/mpm-container/)

[MPM User and developer documentation](https://github.com/cb-geo/mpm-doc/)

## Operating systems and build environment

The recommended and supported Linux OS for building CB-Geo code base is [Fedora](https://getfedora.org/) to work on the latest compiler environment. You may choose to use Ubuntu, but is known to have broken VTK libraries. [Install prerequisites](https://mpm.cb-geo.com/#/user/compile/compile?id=fedora-installation) following the guidelines.

There is no-recommended IDE, you may choose to use EMACS, VIM or VS Code.

Our recommended compiler is GCC/g++. Clang++ is also supported on our container. Currently, `ninja` seems to be the fastest and preferred for compiling the code.

## Code development and style guide

Familiarize yourself with the style of CB-Geo MPM code base. Please follow [CB-Geo style guide](https://cb-geo.github.io/cpp-guide/#/) when developing your code. This helps the codebase to have consistent styling and naming. 

When in doubt, always refer to [ISO C++ Core Guidelines](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines) for best practices in C++. 

Always use `clang-format` to format your code. Runnning `sh ../clang-tools/format.sh` script from `build` directory will automatically format your code. Always format before pushing your code to GitHub.

## Code documentation

**Documentation is an integral part of code development and must go in-sync with feature development and bug fixes. Documentation is always more important than the facy new feature** Always add in-code docuemntation using Doxygen. 

To document a C++ class:

```
  //! Mesh class
  //! \brief Base class that stores the information about meshes
  //! \details Mesh class which stores the particles, nodes, cells and neighbours
  //! \tparam Tdim Dimension
  template <unsigned Tdim>
  class Mesh
```

For a C++ function:

```
  //! Create nodes from coordinates
  //! \param[in] gnid Global node id
  //! \param[in] node_type Node type
  //! \param[in] coordinates Nodal coordinates
  //! \param[in] check_duplicates Parameter to check duplicates
  //! \retval status Create node status
  bool create_nodes(mpm::Index gnid, const std::string& node_type,
                    const std::vector<VectorDim>& coordinates,
                    bool check_duplicates = true);
```                  

In addition to in-line documentation, please create [user documentation](https://mpm.cb-geo.com) on how to use the feature you have developed. Features without documentation are not useful, and does not help others. Always write documentation along with your feature development. This should happen in tandem.

## Code workflow

Please refer to [developer workflow doc](https://mpm.cb-geo.om) on how to create a new feature or fix bugs.

## Continuous Integration and testing

Continous Integration is an integral part of our code development. CI automatically tests every push for successful builds, unit tests and code coverage. Always check CI [build status](https://circleci.com/gh/cb-geo/mpm) when pushing your code. 

CircleCI also does a nightly build to ensure the `develop` version of the code every night at midnight UTC. **This should NOT break!**

Every function should have a unit test. **Always write tests, when developing, not after**. Scientific accuracy and consistency is an integral part to our philosophy. __Code without tests will not be merged.__

[Code Coverage](https://codecov.io/gh/cb-geo/mpm) is a useful metric on coverage of test cases over the entire code base. We have almost twice as many lines in tests as feature codes. We are proud of our unit tests and coverage. Your value as a developer is directly proportional to the number of unit tests and benchmark tests you write. 

[Benchmarks](https://github.com/cb-geo/mpm-benchmarks) are useful to test the full functionality of different parts acting together. Write benchmarks as much as possible, this will ensure your functionality is not broken. Always create `ipynb` files with post-processing results. Do not store result files in benchmarks. Always include mesh generation and particle generation scripts. 


## Usage errors and bugs

If you encounter an error when running a simulation, start by opening a error discussion on our [Discourse Group](https://cb-geo.discourse.group/c/mpm/). Discourse should be your first starting point for error related discussions. If it is established that there is in fact a bug then open a bug report on GitHub using issues. 

## Issues Features and PRS

Every repository have their own bug reporting tool. The bug reports for the CB-Geo MPM code should be filed in [CB-Geo MPM GitHub issues](https://github.com/cb-geo/mpm/issues). All code development discussions should happen on GitHub Issues (Issue/Feature Request/Request for comments). You can view the current progress of all issues related to MPM in the [Project view](https://github.com/orgs/cb-geo/projects/1). 

For a view of our road map see [Trello CB-Geo MPM Roadmap](https://trello.com/b/Jd9XHHVI/cb-geo-mpm-roadmap).

* Always use GitHub issues and PR templates, **do not skip** to a blank template.


| Template type              | Purpose                      |
|:---------------------------|:----------------------------:|
| Bug report                 | Filing a bug report / issue  |
| Feature request            | Request to add a new feature |
| Request for comments       | For new ideas / discussions  |


* Describe your feature / issue in as much detail as possible. Do not leave the description blank. 
_Title says it all_ is not a useful description. Explain the context and give additional details. 

* When asking a question follow [guidelines on good practices](https://stackoverflow.com/help/how-to-ask)

* Choose the labels appropriately. Select `priority`, `type`, and `status` label for each issue/PR.

* Never create a PR before it is feature complete and passes the CI system.

* Use draft PRs to have discussions on design/architecture. Add label as `discussions` in creating draft PRs.

* Issues and PRs will be automatically closed after 90 days of inactivity.

* When you have an idea for a new feature, start with a [Request For Comments](https://github.com/cb-geo/mpm/issues/new?template=request_for_comments.md). 

* RFC is essential before creating a new branch on the repo.

* Documentation is key for good development, make sure to provide as much detail as possible, no detail is trivial to not include. 

## Static analysis

Static analysis aids with testing your code for possible bugs, we have a few ways to do static analysis. The Static Analysis tool in Clang compiler tool chain is automatically used in CircleCI when your code is pushed to MPM GitHub repo. In addition, we also use `cppcheck` to do static analysis. In addition, you can use [Coverity](https://scan.coverity.com/projects/cb-geo-mpm?tab=overview) to perform more thorough static analysis. [PVS Studio] is another good alternative for Open Source code.

Download and install PVS studio: [https://www.viva64.com/en/pvs-studio-download/](https://www.viva64.com/en/pvs-studio-download/)

```
for i in $(find . -iname *.cc); do sed  -i '1i// This is an open source non-commercial project. Dear PVS-Studio, please check it.\n// PVS-Studio Static Code Analyzer for C, C++, C#, and Java: http://www.viva64.com' $i; done
for i in $(find . -iname *.h); do sed  -i '1i// This is an open source non-commercial project. Dear PVS-Studio, please check it.\n// PVS-Studio Static Code Analyzer for C, C++, C#, and Java: http://www.viva64.com' $i; done
for i in $(find . -iname *.tcc); do sed  -i '1i// This is an open source non-commercial project. Dear PVS-Studio, please check it.\n// PVS-Studio Static Code Analyzer for C, C++, C#, and Java: http://www.viva64.com' $i; done
mkdir -p build && cd build
cmake -GNinja -DCMAKE_BUILD_TYPE=Release -DCMAKE_CXX_COMPILER=mpicxx -DKAHIP_ROOT=~/workspace/KaHIP/ -DMPM_BUILD_LIB=Off -DHALO_EXCHANGE=On  .. 
pvs-studio-analyzer trace -- ninja -j12
pvs-studio-analyzer analyze -j -o PVS-Studio.log
plog-converter -t html -o PVS-Studio.html PVS-Studio.log
```
View `PVS-Studio.html` for errors.


## Communication

**Always prefer asynchronous team communication over private messages or synchronous calls.** This will benefit everyone in the team, who may not be in synchronous meetings. 

Use [Discourse](https://cb-geo.discourse.group/c/mpm) when your code fails to compile or you have a usage related error. 

To discuss bugs and new features open an appropriate [GitHub issue](https://github.com/cb-geo/mpm/issues). RFCs are for new development plans, before you start implementing features. Feature Request are for expressing interest in a feature. This will be voted on in [Trello Roadmap](https://trello.com/b/Jd9XHHVI/cb-geo-mpm-roadmap).

Use [Slack](https://cb-geo.slack.com) to get notifications on MPM code developments, new issues and user problems. Use Slack sparringly, as we can't have a record of the discussion. Always prefer asynchronous GitHub issues and Discourse channels over slack. Do not use Slack to ask questions or discuss ideas. Asynchronous communication may feel a bit slow initially, but is more thorough and useful in the long run.

Always use inclusive and encouraging language. Please refer to our [Code of Conduct](https://github.com/cb-geo/mpm/blob/develop/CODE_OF_CONDUCT.md). **Always create an environment to foster new talents**.

### Developer Meetings

We have a 30-minutes weekly developer meetings on Tuesdays at 11:30 AM Central US time (9:30 AM Pacific Time / 5:30 PM UK time). The meeting is on https://whereby.com/cb-geo. Please update [Trello weekly meeting](https://trello.com/b/fU8TDAb8/cb-geo-mpm-weekly-team-meetings) minutes the Monday prior to the weekly meeting. Let us know before hand if you can make it to the meeting, by filling the commitment to attend card. Slack will automatically remind you at 8 AM Central Time on Monday to update the Trello page. Please make your updates by 5 PM on Monday (local time).

Updates should be detailed or should point to a documentation somewhere. Avoid bringing up issues, which are not written in the agenda, when you have something to report, its better to document it on GitHub/Discourse/Trello than to update a few of us. Please review others' comments on Trello before the start of the meeting.  As an indication that you have read please use :+1:  emoji on each card you have reviewed, so we know you had a look. If you disagree feel free to use :-1: . It's important you review the updates, as we want to only discuss critical issues during this in-person meeting. There won't be a repeat of oral updates of information on the card. The idea is to entertain discussions and questions on the updates.

In our weekly meetings, please don't send emails or conduct other activities. Our meetings are only 30 minutes, it's not fair to others if you are working on a computer. It means you don't want to be part of our meeting, you would rather be somewhere else. If you need to be somewhere else, that's perfectly OK, please feel free to skip our group meeting that week. We have an agenda for each meeting, if you like to only attend a part of our meeting that's interesting to you, that's perfectly reasonable.

