# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 19:00:51 2020

@author: Matt
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Arc#
from mplsoccer.pitch import Pitch

%matplotlib inline

data = pd.read_csv("Poch First Match.csv")

data.head()

passes = data['type/value']==1

passesdf = data[passes]

adebayorpass = passesdf['playerId']==6363

df = passesdf[adebayorpass]

df2 = df.reset_index()

df2['x']=df2['x']*1.2
df2['endX']=df2['endX']*1.2
df2['y']=df2['y']*0.8
df2['endY']=df2['endY']*0.8

fig, ax = plt.subplots(figsize = (13.5,8))
fig.set_facecolor('#36454f')
ax.patch.set_facecolor('#36454f')
plt.text(2, 2, "@trevillion_", color = "#FFFFFF", fontsize = 30)

pitch = Pitch(pitch_type='statsbomb', orientation='horizontal',
              pitch_color='#36454f', line_color='#FFFFFF', figsize=(16, 11),
              constrained_layout=True, tight_layout=False)

pitch.draw(ax=ax)

plt.gca().invert_yaxis()

for x in range(len(df2['x'])):
    if df2['Outcome'][x] == 'Successful':
        plt.plot((df2['x'][x],df2['endX'][x]),(df2['y'][x],df2['endY'][x]),color='#0066CC')
        plt.scatter(df2['x'][x],df2['y'][x],color='#0066CC')
    if df2['Outcome'][x] == 'Unsuccessful':
        plt.plot((df2['x'][x],df2['endX'][x]),(df2['y'][x],df2['endY'][x]),color='#99FFFF')
        plt.scatter(df2['x'][x],df2['y'][x],color='#99FFFF')

plt.title("Adebayor Pass Map vs. West Ham (A) 16/08/14", fontsize = 25, color = "#FFFFFF")


plt.show()
    