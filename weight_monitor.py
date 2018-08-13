import matplotlib.pyplot as plt 
import numpy as np 
import pickle
import os 
import time 
import sys
import datetime
import pandas as pd
from matplotlib.dates import date2num
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import plotly.graph_objs as go
from plotly import tools

LOG_DICT_PATH = "logs.pickle"



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
		log_dict = pickle.load(handle)
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
		dates.append(log["datetime"])
		print(dates[0])
		weights.append(log["weight"])
		fat_percs.append(log["fat_perc"])
	dates = np.array(dates)
	weights = np.array(weights)
	fat_percs = np.array(fat_percs)
	
	goal_weight = go.Scatter(x = [dates[0], goal_date], y = [weights[0], goal_weight], line = dict(dash = "dash"), name = "weight goal")
	weight_progress = go.Scatter(x = dates, y = weights, name = "weight progress")

	goal_fat_perc = go.Scatter(x = [dates[0], goal_date], y = [fat_percs[0], goal_fat_perc], line = dict(dash = "dash"), name = "fat percentage goal")
	fat_perc_progress = go.Scatter(x = dates, y = fat_percs, name = "fat percentage progress")

	fig = tools.make_subplots(rows=2, cols=1, subplot_titles = ("Weight Progress", "Fat Percentage Progress"))
	fig.append_trace(goal_weight, 1, 1)
	fig.append_trace(weight_progress, 1, 1)

	fig.append_trace(goal_fat_perc, 2, 1)
	fig.append_trace(fat_perc_progress, 2, 1)

	fig['layout']['yaxis1'].update(title='Weight(kg)')
	fig['layout']['yaxis2'].update(title='Fat Percentage(%)')
	fig['layout']['xaxis2'].update(title='Date')

	plot(fig, filename = "plot.html")

def save_progress(log_dict):
	with open(LOG_DICT_PATH, "wb") as handle:
		pickle.dump(log_dict, handle)
	return True

def main():
	
	if is_first_time(LOG_DICT_PATH):
		log_dict = set_goal()
	else:
		log_dict = load_dict(LOG_DICT_PATH)
	print("DEBUG")
	state = input_progress()
	log_dict["logs"].append(state)

	plot_progress(log_dict)

	save_progress(log_dict)



if __name__ == "__main__":
	main()