set terminal postscript eps enhanced color font 'Helvetica,22'
set output 'apple_time_cdf.eps'
##
##
#set key at 5,19,2
set datafile missing '-'
set style data lines

set xtics border in scale 1,0.5 nomirror offset character 0, 0, 0 autojustify
set xtics  norangelimit
set xtics   ()
set grid ytics lc rgb "#C0C0C0"
set ylabel "CDF"
set xlabel "Solution Time (seconds)"
set yrange [0:1]
set xrange [0.1:55]

#set xlabel  offset character 0, -1.2, 0
grid_color = "#d5e0c9"

set key top left
plot 'AppleIBMUs.cdf' u 1:2   lw 2 lt 2 lc rgb '#E62B17'  title "IBM (US)",\
'AppleIBMUk.cdf' u 1:2  lw 2 lt 1 lc rgb "#11AD34" title "IBM (UK)",\
'AppleGoogleUs.cdf' u 1:2  lw 2 lt 1 lc rgb "black" title "Google (US)",\
'AppleGoogleUk.cdf' u 1:2  lw 2 lt 1 lc rgb "yellow" title "Google (UK)",\
'AppleWit.cdf' u 1:2  lw 2 lt 1 lc rgb "blue" title "Wit"
#plot 'time_process.cdf' u 1:2  lw 2 lc rgb '#00ad31' title "Process",\
#'time_history.cdf' u 1:2  lw 2  lt 2 lc rgb "red" title "History",\
#'time_module.cdf' u 1:2  lw 2  lt 2 lc rgb "gray" title "Module",\
#'time_solution.cdf' u 1:2  lw 2  lt 2 lc rgb "green" title "Solution",\
