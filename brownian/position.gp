set datafile separator ","
set key autotitle columnhead
set terminal png
set output "position.png"

set title "position vs time"
set xlabel "time"
set ylabel "position"
set grid

plot "data.csv" using 1:5 
plot "data.csv" using 1:4