clear
#rm -rf apps

read -p "App to install: " $input

echo Downloading...

#git clone https://github.com/Leafboi111/LeafOS
git clone --quiet https://github.com/Leafboi111/LeafOS > /dev/null

echo Installing...
sleep 0.1

cp -r LeafOS/apps devapps

rm -rf LeafOS

chmod 777 apps/*
chmod 777 os/*

echo Done!
sleep 0.1