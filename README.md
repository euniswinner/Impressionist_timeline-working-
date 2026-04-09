Language:Python 3.14
source: Matplotlib Tutorial (Part 2): Bar Charts (Youtuber: Corey Schafer)
I used visual studio for coding. 

This is a Python based timeline that visualizes the active years of Impressionist painters in a chart.
Note about my code:
Painter is list of names for the Y-axis.
ST_Y is the starting year of their career (used as the left offset).
durations is the length of the bar (how many years they were active).
plt.barh is draws horizontal bars. By setting left=ST_Y, the bars "float" to start at the correct historical year instead of zero.
Result is a clean chart showing exactly when each artist's career overlapped throughout history.
