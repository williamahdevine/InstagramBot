#!/bin/bash
pwd=`pwd`

echo "Configuring credentials. Enter your Username:"
read username

echo "Enter your password. This will be stored locally"
read password

echo "#!/bin/bash" > runner.sh
echo "export DISPLAY=:0" > runner.sh
echo "export PATH=$pwd/bin" > runner.sh
echo "cd $pwd" > runner.sh
echo "python3 main.py $username $password $pwd" >> runner.sh

echo "#! /bin/bash" > stop.sh
echo "\`crontab -l > tempfile\`" >> stop.sh
echo "\`sed -i '' -e '/runner.sh/d' ./tempfile\`" >> stop.sh
echo "\`crontab -r\`" >> stop.sh
echo "\`crontab tempfile\`" >> stop.sh
echo "\`rm tempfile\`" >> stop.sh
echo "echo \"Removed process from crontab.\"" >> stop.sh


chmod 777 ./runner.sh
chmod 777 ./stop.sh

crontab -l > tempfile

echo "0 8-22/2 1-31/2 * * $pwd/runner.sh" >> tempfile
echo "" >> tempfile
crontab tempfile
rm tempfile

echo "Configured to run every 2nd hour, between 8am-10pm, every second day."
echo "Cancel it by running stop.sh"

