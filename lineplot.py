import matplotlib.pyplot as plt

with open("Goals.txt","r") as f:
    #list of strings corresponding to home team goals for soccer game
    # x goes through list and converts string to int
    homeTeamGoals = [int(x) for x in f.readline().strip("\n").strip(" ").split(" ")]
    awayTeamGoals= [int(x) for x in f.readline().strip("\n").strip(" ").split(" ")]

xVars = []
ticks = ["Game One","Game Fifty","Game 100"]
for i in range(len(homeTeamGoals)):
    xVars.append(i)

plt.figure(figsize=(10,10))
plt.plot(xVars, awayTeamGoals, c = "green", ls="--",label="Away Team Goals")
# plt.show() or plot or scatter
# enter math mode add r.. latex
plt.title(r"Our first plot $\frac{1}{2}$")
plt.plot(xVars, homeTeamGoals, c = "red",ls=":",label="Home Team Goals")
plt.legend(loc = "upper right")
plt.xlim(0,145)
plt.ylim(-.5,6.5)
plt.xlabel("Game #")
plt.ylabel(r"Goals Scored$_5$")
plt.xticks([49],["Fourty Nine"],rotation=45)
plt.yticks([3],["Three Goals"],rotation=90)
plt.text(50,4,r"Hey hoss$^3$",fontsize=20,color="blue")
plt.annotate("text lalala", xy=(30,5),xytext=(65,5), arrowprops=dict(facecolor="red",shrink=25))

plt.savefig("figure.pdf")
plt.show()
