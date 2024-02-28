# This script is meant to be used when the keys need changed on your instance. 

new_key=$(python3 -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())')
echo $new_key
#need to avoid the "&" character, sed is unhappy
sed -i "s/\(\"SECRET_KEY\"\:\).*\(\,\)/\1 \"$new_key\"\2/g" /home/bitnami/SCUP/SCUP/settings/settings_test.json
#/opt/bitnami/projects/SCUP/deploy_scripts/restart.sh #restart apache