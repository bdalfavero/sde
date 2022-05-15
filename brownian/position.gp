set datafile separator ","
set title "position vs time"
set xlabel "time"
set ylabel "position"
set grid
plot "data.csv"
save "position.png"