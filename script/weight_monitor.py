import matplotlib.pyplot as plt 
import numpy as np 
import pickle
import os 
import time 
import sys
import datetime
import pandas as pd

LOG_DICT_PATH = "../logs.pickle"



def is_first_time(log_dict_path):
	return not os.path.isfile(log_dict_path)

def set_goal():
	
	LOG_DICT = {"goal":{}, "logs":[]}

	goal_date_str = input("Please input your goal date(YYYYMMDD)")
	goal_date = pd.to_datetime(goal_date_str)
	
	goal_weight = input("Please input your goal weight")
	'''
	track_fat_perc_str = input("Do you want to track your fat percentage? [Y/N]")
	if track_fat_perc_str in ["Y", "y", "yes"]:
		track_fat_perc = True
	elif track_fat_perc_str in ["N", "n", "No"]:
		track_fat_perc = False
	if track_fat_perc:
	'''
	goal_fat_perc = input("Please input your goal of fat percentage(%)")

	LOG_DICT["goal"]["date"] = goal_date
	LOG_DICT["goal"]["weight"] = goal_weight
	LOG_DICT["goal"]["fat_perc"] = goal_fat_perc
	return LOG_DICT

def load_dict(log_dict_path):
	with open(log_dict_path, "rb") as handle:
		log_dict = pickle.load(log_dict)
	return log_dict 

def input_progress():

	ctime = datetime.datetime.now()
	weight = input("input your current weight")
	fat_perc = input("input your current fat percentage")

	state = {"datetime": ctime, "weight": weight, "fat_perc": fat_perc}
	print(state)
	return state

def plot_progress(log_dict):
	goal = log_dict["goal"]
	goal_date = pd.to_datetime(goal["date"])
	print(goal_date)
	goal_weight = goal["weight"]
	goal_fat_perc = goal["fat_perc"] 

	logs = log_dict["logs"]

	dates = []
	weights = []
	fat_percs = []

	for log in logs:
		dates.append(pd.to_datetime(log["datetime"]))
		print(dates[0])
		weights.append(log["weight"])
		fat_percs.append(log["fat_perc"])
	dates = np.array(dates)
	weights = np.array(weights)
	fat_perc = np.array(fat_perc)

	ax1 = plt.subplot(212)
	ax1.set_title("Weight Progress")
	ax1.set_xlabel("time")
	ax1.set_ylabel("weight")
	ax1.grid(True)
	ax1.plot((dates[0], goal_date), (weights[0], goal_weight), "r")
	ax1.plot(dates, weights, "b")
	plt.setp(ax1.get_xticklabels(), fontsize=6)

	ax2 = plt.subplot(211, sharex = ax1)
	ax2.set_title("Fat Percentage Progress")
	ax2.set_ylabel("fat percentage")
	ax2.grid(True)
	ax2.plot((dates[0], goal_date), (fat_percs[0], goal_fat_perc), "r")
	ax2.plot((dates, fat_percs, "b"))
	plt.setp(ax2.get_xticklabels(), visible=False)
	plt.savefig("../plots/plot.png")
	plt.show()

def save_progress(log_dict):
	with open("../logs.pickle", "wb") as handle:
		pickle.dump(log_dict)
	return True

def main():
	
	if is_first_time(LOG_DICT_PATH):
		log_dict = set_goal()
	else:
		log_dict = load_dict(LOG_DICT_PATH)

	state = input_progress()
	log_dict["logs"].append(state)

	plot_progress(log_dict)

	save_progress(log_dict)



if __name__ == "__main__":
	main()