_now=$(date +"%m_%d_%Y")
_file="$_now.dat"
python testTickets/manage.py printallmodels 2> "$_file"
