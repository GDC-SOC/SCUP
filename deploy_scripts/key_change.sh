# This script is meant to be used when the keys need changed on your instance. 
#For RDS Management reference the AWS Secrets manager.
#=====================================================
# User                      Last Edit       Ticket #
# Mark Leadingham           02/29/2024      GDCG-383
#=====================================================
#
### Update Secret Keys ###
new_key=$(python3 -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())') #Generate new key
new_key_escaped=$(printf '%q\n' "$new_key") #need to avoid the "&" character, sed is unhappy, so we escape all special characters with printf
sed -i "s/\(\"SECRET_KEY\"\:\).*\(\,\)/\1 \"$new_key_escaped\"\2/g" /home/bitnami/SCUP/SCUP/settings/settings_new.json #replace settings key with new key
/opt/bitnami/projects/SCUP/deploy_scripts/restart.sh #restart apache