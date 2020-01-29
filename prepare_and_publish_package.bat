echo "Did you change git action and updated the package?"
pause
git pull
move /-Y dist\*.* dist_old_versions\
C:\Users\tikho\Anaconda3\python.exe setup_version.py
pause
C:\Users\tikho\Anaconda3\python.exe setup.py sdist
pause
git add --all
git status
pause
set /P commit_name="Please, make up the commit name:"
set /p tag=<tag_name
git commit -m %commit_name%
git tag %tag%
git push
git push --tags
"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" https://github.com/bobeobibo/phigaro/actions
pause