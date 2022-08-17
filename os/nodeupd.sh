clear
rm -rf apps

echo Downloading...

#git clone https://github.com/Leafboi111/LeafOS
git clone --quiet https://github.com/SwiftyProgrammer690/MochaOS > /dev/null

echo Installing...
sleep 0.1

rm -rf apps

cp -r MochaOS/apps apps

rm -rf MochaOS

chmod 777 apps/*
chmod 777 os/*

echo Done!
sleep 0.1