counter=1
day=0
mon=1

while [ $counter -le 372 ]
do
if [ $day -ge 31 ]
then
((day = 0))
((mon++))
fi
((day++))
python POTD.py $mon $day
done