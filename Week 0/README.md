# **Week 0 : Getting started with Git!**

## *Resources*

1. Git

    Go through one of the first two links, shouldn't take more than an hour. Make sure you cover atleast add, commit, push, pull, status, config and branch. The third link is a good animation of Git workflow. Last two links are just for referring syntax.

    - This video is all you need to get along with Git ...atleast it's basics : <https://youtu.be/8JJ101D3knE>
    - In case you're more of a reader follow this : <https://www.w3schools.com/git/>
    - This is also a small playlist which will help you understand some advanced git concepts like Merging, Rebasing, Git Flow : <https://www.youtube.com/playlist?list=PLqTmkYd8_EoJM77eZDFHAS-2Z2rxEmyOP>
    - Official Git docs (Cover everything here before the weekend, ||Just kidding :0||) : <https://git-scm.com/docs>
    - Git cheat-sheet for quick reference : <https://training.github.com/downloads/github-git-cheat-sheet.pdf>

2. GitHub

    - Cover from GitHub GET STARTED upto GitHub SEND PULL REQUEST : <https://www.w3schools.com/git/git_remote_getstarted.asp?remote=github>

## *Assignment*

1. First things first, configure git with your name and email id. We recommend using Visual Studio Code (VSC) editor and config it as your default editor.
2. (Optional cool commit messages) Append these lines at the end of your ~/.gitconfig file.

    ```bash
    [alias]
        cap = "!f() { git add .; git commit -m "$@"; git push; }; f"
        new = "!f() { git commit -m "📦 NEW: $@"; }; f"        # NEW.
        imp = "!f() { git commit -m "👌 IMPROVE: $@"; }; f"    # IMPROVE.
        fix = "!f() { git commit -m "🐛 FIX: $@"; }; f"        # FIX.
        rlz = "!f() { git commit -m "🚀 RELEASE: $@"; }; f"    # RELEASE.
        doc = "!f() { git commit -m "📖 DOC: $@"; }; f"        # DOC.
        tst = "!f() { git commit -m "✅ TEST: $@"; }; f"    # TEST.
        publish = "!git push origin $(git branch --show-current)"
    ```

3. You have to now fork the project repository and clone it to your local system. Checkout the material branch and copy this week's resources message to the README.md file. Add, commit and push those changes to the material branch of your fork. Finally create a pull request from your fork's material branch to the main repo's material branch.
Repo link : <https://github.com/adityakadoo/MiniMotorwaysSolver>
