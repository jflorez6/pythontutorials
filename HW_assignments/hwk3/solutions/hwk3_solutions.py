## HW 3 solutions for AST 376R
## by Jonathan Florez 03/30/21
import numpy as np

## Problem 1
whmips = np.genfromtxt('hwk3-catalog.txt',unpack=True,dtype=int,usecols=(11)) ## Read in integer types
ID, SExtractor_ID, x_pos, y_pos, phot_z, r_mag, Mstar, SFR_UV, SFR_IR = np.genfromtxt('hwk3-catalog.txt',unpack=True,dtype=float,usecols=(0,1,3,4,7,8,9,10,12)) ## Read in float types
str_ID, ACS_F606W, ACS_F850LP = np.genfromtxt('hwk3-catalog.txt',unpack=True,dtype=str,usecols=(2,5,6)) ## Read in strings

## First things first: print the last row of the catalog we just read in to make sure ALL rows have been read in correctly:
#print(ID[-1], str_ID[-1], x_pos[-1], y_pos[-1], phot_z[-1], r_mag[-1], Mstar[-1], SFR_UV[-1], SFR_IR[-1], whmips[-1], ACS_F606W[-1], ACS_F850LP[-1]) 

print("1. Number of galaxies:", len(ID)) ## Number of galaxies we successfully read in

## Problem 2

p2 = np.where((0.55 < phot_z) & (phot_z < 0.60))

print("2. Number of galaxies with 0.55 < z < 0.60:", len(p2[0]))

'''
You can check to see if this worked by creating a subarray. You can define a new array, new_z, 
as new_z = phot_z[p2]. Now if you print new_z with print(new_z), all values will be
between 0.55 < z < 0.6.
'''

## Problem 3

p3 = np.where(Mstar[p2] > 1e10)  ## Select all galaxies with M > 1e10 and 0.55 < z < 0.6 

print("3. Number of galaxies with 0.55 < z < 0.60 and M* > 1e10 Msol:", len(p3[0]))

## Problem 4

p4 = np.where(whmips[p2][p3] == 1.0) 

print("4. Number of galaxies from Problem 3 with WHMIPS Detection:", len(p4[0]))

## Problem 5

np.savetxt('hwk3-sol-sample.txt', np.c_[str_ID[p2][p3][p4], Mstar[p2][p3][p4], phot_z[p2][p3][p4], whmips[p2][p3][p4]], fmt='%s')
