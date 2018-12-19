pip3 uninstall nvhtml
git rm -r dist
git rm -r build
git rm -r nvhtml.egg-info
rm -r dist
rm -r build
rm -r nvhtml.egg-info
git add .
git commit -m "remove old build"
