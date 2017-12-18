#! /bin/sh
echo "input img url"
read IMG
curl $IMG | imgcat
clear
echo "showed"