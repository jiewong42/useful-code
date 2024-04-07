git config --global user.name "jiewong42"
git config --global user.email "mail"

git init
git add . /win报错输入git config core.autocrlf false  //禁用自动转换 
git commit -m "提交"
git remote add origin https://github.com/jiewong42/useful-code.git

git push origin master
//报错refusing to merge unrelated histories输入git pull origin master --allow-unrelated-histories

git pull origin master/远程仓库于本地合并