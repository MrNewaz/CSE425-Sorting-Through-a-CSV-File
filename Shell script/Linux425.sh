#!/bin/bash
searchByAge()
{
    echo "Enter the Age to search: "
    read age
    grep $age heart.csv
}

searchBySex(){
echo "Enter the Sex to search: "
read sex
grep $sex heart.csv
}

searchByCp(){
echo "Enter the Cp to search: "
read cp
grep $cp heart.csv
}

searchByTrtbps(){
echo "Enter the Trtbps to search: "
read trtbps
grep $trtbps heart.csv
}

searchByFbs(){
echo "Enter the Fbs to search: "
read fbs
grep $fbs heart.csv

}

searchByRestecg(){
echo "Enter the Restecg to search: "
read restecg
grep $restecg heart.csv
}

searchByThalachh(){
echo "Enter the Thalachh to search: "
read thalachh
grep $thalachh heart.csv
}

searchByExng(){
echo "Enter the Exng to search: "
read exng
grep $exng heart.csv
}

searchByOldpeak(){
echo "Enter the Oldpeak to search: "
read oldpeak
grep $oldpeak heart.csv
}

searchBySlp(){
echo "Enter the Slp  to search: "
read slp
grep $slp heart.csv
}

searchByCaa(){
echo "Enter the Caa to search: "
read caa
grep $caa heart.csv
}

searchByThall(){
echo "Enter the Thall to search: "
read thall
grep $thall heart.csv
}

searchByOutput(){
echo "Enter the Output to search: "
read output
grep $output heart.csv
}


echo "Enter 1 to search by Age of the person"
echo "Enter 2 to search by Gender of the person"
echo "Enter 3 to search by Chest Pain type chest pain type"
echo "Enter 4 to search by Resting blood pressure (in mm Hg)"
echo "Enter 5 to search by Cholestoral in mg/dl fetched via BMI sensor"
echo "Enter 6 to search by fasting blood sugar"
echo "Enter 7 to search by resting electrocardiographic results"
echo "Enter 8 to search by maximum heart rate achieved"
echo "Enter 9 to search by exercise induced angina (1 = yes; 0 = no)"
echo "Enter 10 to search by Previous peak"
echo "Enter 11 to search by Slp"
echo "Enter 12 to search by Caa"
echo "Enter 13 to search by Thall"
echo "Enter 14 to search by Output"

read choice

if [ "$choice" -eq 1  ];then
    searchByAge
elif [ "$choice" -eq 2 ];then
    searchBySex
elif [ "$choice" -eq 3 ];then
    searchByCp
elif [ "$choice" -eq 4 ];then
    searchByTrtbps
elif [ "$choice" -eq 5 ];then
searchByChol
elif [ "$choice" -eq 6 ];then
searchByFbs
elif [ "$choice" -eq 7 ];then
searchByRestecg
elif [ "$choice" -eq 8 ];then
searchByThalachh
elif [ "$choice" -eq 9 ];then
searchByExng
elif [ "$choice" -eq 10 ];then
searchByOldpeak
elif [ "$choice" -eq 11 ];then
searchBySlp
elif [ "$choice" -eq 12 ];then
searchByCaa
elif [ "$choice" -eq 13 ];then
searchByThall
elif [ "$choice" -eq 14 ];then
searchByOutput
else
echo "Please enter number between 1 to 14"
fi



