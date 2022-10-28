


Blue=$'\033[1;34m'
Green=$'\033[1;32m'
Red=$'\033[1;31m'
Yellow=$'\033[1;33m'
Noc=$'\033[0m'

clear
sleep 1s

if [[ $1 == run ]]
then
    echo "${Blue}Running: python manage.py runserver"
    echo ${Noc}
    python manage.py runserver
elif [[ $1 == migrations ]]
then
    echo "${Blue}Running: python manage.py makemigrations"
    echo ${Noc}
    python manage.py makemigrations
    echo "${Green}Success: Migration created."
    echo ${Noc}
    echo "${Yellow}Do you want to migrate to the database(y/Y for YES): " 
    read decision
    if [[ $decision == Y || $decision == y ]]
    then
        echo "${Blue}Running: python manage.py migrate"
        echo ${Noc}
        python manage.py migrate
        echo "${Green}Success: Model migrated to the database."
        echo ${Noc}
    else
        echo "${Red}Couldn't migrate models to database."
        echo ${Noc}
    fi
elif [[ $1 == push ]]
then
    message=$2
    echo "${Blue}Running: git add ."
    git add .
    echo "${Blue}Running: git status"
    git status
    echo "${Blue}Running: git commit -m \"$message\"" 
    git commit -m "$message"
    echo "${Blue}Running: git push" 
    git push
    echo "${Green}Success: Pushed to git."
fi
echo ${Noc}