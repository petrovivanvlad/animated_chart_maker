import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pandas as pd

# Initialization:

def read(countries):
	data = pd.read_csv('WPP2019_TotalPopulationBySex.csv')
	year, population, variant = [], [], []
	for country in countries:
		country_data = data[data.Location == country]
		year.append(pd.Series.tolist(country_data.Time))
		population.append(pd.Series.tolist(country_data.PopTotal))
		variant.append(pd.Series.tolist(country_data.Variant))
	return year, population, variant

#countries = ['Russian Federation', 'Ukraine', 'Kazakhstan', 'Belarus', 'Azerbaijan', 'Kyrgyzstan', 'Armenia', 'Tajikistan']
#countries = ['Russian Federation']
countries = ['Russian Federation', 'Ukraina', 'Uzbekistan', 'Kazakhstan', 'Tajikistan', 'Kyrgyzstan', 'Azerbaijan', 'Turkmenistan', 'Armenia']
#countries = ['Afghanistan', 'Albania', 'United States', 'Turkey']

axis_x, axis_y, variant = read(countries)

# MatPlotLib:

plt.style.use('bmh')
fig, ax = plt.subplots(figsize=(10, 8))
line, = ax.plot(axis_x[0], axis_y[0])

temp_x, temp_y = [], [] # Для возобновления анимации

def update(i):
	if (variant[0][i] == 'Medium' and i < len(variant[0]) and int(axis_x[0][i]) < 2078):
		if (i == 0):
			temp_x.clear()
			temp_y.clear()
			for j in range(len(countries)):
				temp_x.append([])
				temp_y.append([])
		for j in range(len(axis_x)):
			temp_x[j].append(axis_x[j][i])
			temp_y[j].append(axis_y[j][i])
			#plt.plot(temp_x[j], temp_y[j]) # Почему-то не работает...
		ax.cla()
		ax.plot(temp_x[0], temp_y[0], color='crimson', linewidth=3)
		ax.plot(temp_x[1], temp_y[1], color='lightskyblue', linewidth=3)
		ax.plot(temp_x[2], temp_y[2])
		ax.plot(temp_x[3], temp_y[3])
		ax.plot(temp_x[4], temp_y[4])
		ax.plot(temp_x[5], temp_y[5])
		ax.plot(temp_x[6], temp_y[6])
		ax.plot(temp_x[7], temp_y[7])
		ax.plot(temp_x[8], temp_y[8])

	countries_legend = []
	if (variant[0][i] == 'Medium' and i < len(variant[0]) and int(axis_x[0][i]) < 2078):
		plt.title('Россиа ' + str(int(temp_x[0][i])))
		for c in range(len(countries)):
			countries_legend.append(f'{int(temp_y[c][i]):,}' + ',000 - ' + countries[c])	

	ax.legend(countries_legend)
	countries_legend.clear()

	plt.xlabel('year')
	plt.ylabel('population')
	#plt.xticks([1950, 1960, 1970, 1980, 1990, 2000, 2010, 2020, 2030, 2040, 2050, 2060, 2070, 2080, 2090, 2100])
	plt.xticks([1950, 1960, 1970, 1980, 1990, 2000, 2010, 2020, 2030, 2040, 2050, 2060, 2070, 2080])
	return line,

anime = animation.FuncAnimation(fig, update, frames=len(axis_x[0]), interval=100, save_count=50)

anime.save('raw.gif', fps=60)

import gif_to_mp4_converter as idk
idk.convert("raw.gif")

plt.show()