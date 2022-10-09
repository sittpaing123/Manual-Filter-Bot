if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/Hansaka-Anuhas-1/Manual-Filter-Bot.git /Manual-Filter-Bot
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /Manual-Filter-Bot
fi
cd /Manual-Filter-Bot
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 bot.py
