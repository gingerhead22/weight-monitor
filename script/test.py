import matplotlib.pyplot as plt 

ax1 = plt.subplot(212)
ax1.set_title("Weight Progress")
ax1.set_xlabel("time")
ax1.set_ylabel("weight")
ax1.grid(True)
plt.setp(ax1.get_xticklabels(), fontsize=6)

ax2 = plt.subplot(211, sharex = ax1)
ax2.set_title("Fat Percentage Progress")
ax2.set_ylabel("fat percentage")
ax2.grid(True)
plt.setp(ax2.get_xticklabels(), visible=False)
plt.show()