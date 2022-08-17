# MochaOS
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

echo "$(tput setaf 180)_    _ ______ _____ |   |   /\     ______  _____"
echo "$(tput setaf 180)|\  /| |    | |     |---|  /--\    |    |  |____"
echo "$(tput setaf 180)| \/ | |____| |____ |   | /    \   |____|  _____|"

rm -rf apps

echo "$(tput setaf 46)Booting Up..."

git clone --quiet https://github.com/SwiftyProgrammer690/MochaOS > /dev/null

rm -rf apps

cp -r MochaOS/apps apps

rm -rf MochaOS

chmod 777 os/*
chmod 777 apps/*

./os/os.sh