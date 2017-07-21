set terminal postscript eps enhanced color font 'Helvetica,22'
set output 'captcha_length.eps'
##
##
#set key at 5,19,2
set datafile missing '-'
#set style linespoints 
#set style fill solid 1.0 border
set size 2,1
set xtics border in scale 1,0.5 nomirror offset character 0, 0, 0 autojustify
set xtics  norangelimit
#set xtics 1
set xdata time
set timefmt "%y%m%d-%H%M%S"
set format x "%H:%M"
set grid ytics lc rgb "#C0C0C0"
set grid xtics lc rgb "#C0C0C0"
set xtics font ", 18"
set ytics font ", 18"
set ylabel "Captcha Length (# of Digits)" offset 2
set xlabel "Time"
set yrange [4.5:10.5]
set ytics (5,6,7,8,9,10)
#set xrange ["17:00" : "17:10"]


#set xlabel  offset character 0, -1.2, 0
grid_color = "#d5e0c9"
set key top right
plot 'captcha_length.dat' using 1:2 w lp lt 2 lc rgb 'black' lw 2 pt 7 notitle
#pt 5 ps 0.5 lt rgb "red" notitle #3eaad6 
#'minstat_05_15_2015_1min.txt' using 1:3 pt 7 ps 1 lt rgb "#11AD34" notitle,\
#'minstat_04_30_2015_1min.txt' using 1:3 pt 2 ps 1 lt rgb "#406090" notitle,\
#'minstat_05_12_2015_1min.txt' using 1:3 pt 3 ps 1 lt rgb "black" notitle,\
#plot 'minstat/hourstat_04_30_2015.txt' u 1:2  lw 6 lt 4 ps 1 lc rgb '#11AD34'  title "Weekday",\
#'hourstat_05_07_2015.txt' u 1:2  lw 6 lt 4 ps 1 lc rgb '#11AD34'  title "Weekday",\
#'minstat/hourstat_05_03_2015.txt' u 1:2  lw 6 lt 4 ps 1 lc rgb 'red'  title "Weekend",\
#'rrr5' u 1:2  lw 6 lt 4 ps 1 lc rgb 'purple'  title "greedy",\
#'rrr2' u 1:2  lw 6 lt 4 ps 1 lc rgb 'red'  title "greedy",\
#'rrr3' u 1:2  lw 6 lt 4 ps 1 lc rgb 'blue'  title "greedy",\
#'rrr4' u 1:2  lw 6 lt 4 ps 1 lc rgb 'black'  title "greedy",\
#'hourstat_05_05_2015' u 1:2  lw 6 lt 4 ps 1 lc rgb 'blue'  title "Sunday",\
#'hourstat_sunday' u 1:2  lw 6 lt 4 ps 1 lc rgb 'blue'  title "Sunday",\
#'hourstat_monday' u 1:2  lw 6 lt 4 ps 1 lc rgb 'black'  title "Monday",\
#'hourstat' u 1:4 with boxes title "Total"
#'hourstat' u 1:3 lw 6 lt 1 lc rgb "#11AD34" title "Fail"
#plot 'time_process.cdf' u 2:1  lw 2 lc rgb '#00ad31' title "Process",\
#'time_history.cdf' u 2:1  lw 2  lt 2 lc rgb "red" title "History",\
#'time_module.cdf' u 2:1  lw 2  lt 2 lc rgb "gray" title "Module",\
#'time_solution.cdf' u 2:1  lw 2  lt 2 lc rgb "green" title "Solution",\
