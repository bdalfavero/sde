set datafile separator ","
set key autotitle columnhead
set terminal png
set output "position.png"

set title "Particle trajectory"
set xlabel "x"
set ylabel "y"
set grid

plot "data.csv" using 4:5 