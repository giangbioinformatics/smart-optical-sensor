import os
indir="/home/nguyen/Desktop/Projects/smart-optiocal-sensor/data/balance_image/CuSO4/raw_data"
outdir="/home/nguyen/Desktop/Projects/smart-optiocal-sensor/data/balance_image/CuSO4/"

os.system(f"python3 feature_extraction.py -i {indir}  -o {outdir} ")
cd /home/nguyen/Desktop/Projects/smart-optiocal-sensor/data/balance_image/CuSO4/

# for i in glob.glob("")
# for i in `ls *.jpg`
# do
# name=`basename ${i} .jpg`
# mv $i ${name}_batch1.jpg
# done