# 1	D	days	MJD_u	Modified Julian Date for u-band observation
# 2	F6.3	mag	u	Apparent u-band magnitude (1)
# 3	F5.3	mag	u_err	u-band error
# 4	D	days	MJD_g	Modified Julian Date for g-band observation
# 5	F6.3	mag	g	Apparent g-band magnitude (1)
# 6	F5.3	mag	g_err	g-band error
# 7	D	days	MJD_r	Modified Julian Date for r-band observation
# 8	F6.3	mag	r	Apparent r-band magnitude (1)
# 9	F5.3	mag	r_err	r-band error
# 10	D	days	MJD_i	Modified Julian Date for i-band observation
# 11	F6.3	mag	i	Apparent i-band magnitude (1)
# 12	F5.3	mag	i_err	i-band error
# 13	D	days	MJD_z	Modified Julian Date for z-band observation
# 14	F6.3	mag	z	Apparent z-band magnitude (1)
# 15	F5.3	mag	z_err	z-band error
# 16	D	deg	ra_median	Median Right Ascension in decimal degrees (J2000, 360° is subtracted from all RA values > 300°)
# 17	D	deg	decl_median	Median Declination in decimal degree
import astropy
from astropy.io import fits
import os, sys
from astropy.table import Table
import pandas as pd
from skimage.transform import resize
import csv
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from astropy.coordinates import search_around_sky, SkyCoord
from astropy import units as u
import seaborn as sns
#
file_name = "/Users/SnehPandya/Desktop/Black_Hole_NN/raw_data/original_LC/7838"

with open(file_name,'r') as f:
    next(f) # skip first row
    df = pd.DataFrame(l.rstrip().split() for l in f)

for i in range(14):
    df[i] = pd.to_numeric(df[i])

df_u = df[df[1]>1]
df_g = df[df[4]>1]
df_r = df[df[7]>1]
df_i = df[df[10]>1]
df_z = df[df[13]>1]

def plot_light_curve(df):
    sns.set(font = 'sans serif')
    sns.set_context('paper')
    sns.regplot(df_u[0], df_u[1], scatter=True, marker='*', label = 'u',fit_reg=False, color='purple')
    sns.regplot(df_g[3], df_g[4], scatter=True, marker='*', label = 'g',fit_reg=False, color='green')
    sns.regplot(df_r[6], df_r[7], scatter=True, marker='*', label = 'r',fit_reg=False, color='red')
    sns.regplot(df_i[9], df_i[10], scatter=True, marker='*', label = 'i',fit_reg=False, color='black')
    sns.regplot(df_z[12], df_z[13], scatter=True, marker='*', label = 'z',fit_reg=False, color='blue')
    # sns.pointplot(x=df_u[0],y=df_u[1], ci = sd_u, join = False)
    # sns.pointplot(df_g[3],df_g[4], ci = df_g[5], join = False)
    # sns.pointplot(df_r[6],df_r[7], ci = df_r[8], join = False)
    # sns.pointplot(df_i[9],df_i[10], ci = df_i[11], join = False)
    # sns.pointplot(df_z[12],df_z[13], ci = df_z[14], join = False)
        # plt.plot(df_u[0], df_u[1], label = 'u',ls ='',marker='*')
        # plt.plot(df_g[3], df_g[4], label = 'g',ls ='',marker='*')
        # plt.plot(df_r[6], df_r[7], label = 'r',ls ='',marker='*')
        # plt.plot(df_i[9], df_i[10], label = 'i',ls ='',marker='*')
        # plt.plot(df_z[12], df_z[13], label = 'z',ls ='',marker='*')
    # plt.errorbar(df_u[0], df_u[1], yerr=df_u[2], fmt='.b')
    # plt.errorbar(df_g[3], df_g[4], yerr=df_g[5], fmt ='.y')
    # plt.errorbar(df_r[6], df_r[7], yerr=df_r[8], fmt ='.g')
    # plt.errorbar(df_i[9], df_i[10], yerr=df_i[11], fmt ='.r' )
    # plt.errorbar(df_z[12], df_z[13], yerr=df_z[14], fmt = '.m')
    plt.xlabel('Modified Julian Day [MJD]')
    plt.ylabel('Magnitude')
    plt.title('Light Curve')
    plt.gca().invert_yaxis()
    plt.legend()
    plt.show()


fig=plt.figure(figsize=(10, 7), dpi= 80, facecolor='w', edgecolor='k')
plot_light_curve(df)
# fig=plt.figure(figsize=(10, 7), dpi= 80, facecolor='w', edgecolor='k')
# plot_light_curve(df)
