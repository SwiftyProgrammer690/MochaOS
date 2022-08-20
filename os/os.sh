#!/bin/bash

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

clear

function cmpio {
  if [ "$1" == "devrun" ];
  then
    ls devapps
    read -p ">" appin
    ./"devapps/$appin.*"
  elif [ "$1" == "" ];
  then
    break
  else
    ./*/$input.* || python3 apps/$input.py
    #sleep 5 # for debugging
  fi
}

#main function
function main {

  while true
  do
    tput setaf 250
    select input in about mochaupd devrun 2048 mocalender nodecalc terminal mochapad One_Strike_And_You\'re_Out tetris moquiz clock
    do
      cmpio "$input"
      clear
      tput setaf 180
      echo "☕☕☕";
      echo "Welcome to MochaOS!"; echo
      tput setaf 45
      date +"%D %T"
      break
    done
  done
}

tput setaf 180
echo "☕☕☕";
echo "Welcome to MochaOS!"; echo

tput setaf 45
date +"%D %T"

main