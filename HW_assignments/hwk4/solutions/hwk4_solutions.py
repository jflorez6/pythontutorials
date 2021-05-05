## HW 4 solutions for AST 376R
## by Jonathan Florez 04/09/21
import numpy as np
import matplotlib.pyplot as plt

## Problem 1
whmips = np.genfromtxt('hwk4-catalog.txt',unpack=True,dtype=int,usecols=(11)) ## Read in integer types
ID, SExtractor_ID, x_pos, y_pos, phot_z, r_mag, Mstar, SFR_UV, SFR_IR = np.genfromtxt('hwk4-catalog.txt',unpack=True,dtype='f8',usecols=(0,1,3,4,7,8,9,10,12)) ## Read in float types
str_ID, ACS_F606W, ACS_F850LP = np.genfromtxt('hwk4-catalog.txt',unpack=True,dtype=str,usecols=(2,5,6))

# Optional Best Practices Test
print("Number of elements read in:", len(ID))
print("First row elements:", ID[0], SExtractor_ID[0], str_ID[0], x_pos[0], y_pos[0], ACS_F606W[0], ACS_F850LP[0], phot_z[0], r_mag[0], Mstar[0], SFR_UV[0], whmips[0], SFR_IR[0])
print("Last row elements:", ID[-1], SExtractor_ID[-1], str_ID[0], x_pos[-1], y_pos[-1], ACS_F606W[-1], ACS_F850LP[-1], phot_z[-1], r_mag[-1], Mstar[-1], SFR_UV[-1], whmips[-1], SFR_IR[-1])


p1_index = np.where((0.47 < phot_z) & (phot_z <= 0.62) & (Mstar > 5e9))[0]

logMstar = np.log10(Mstar)
logSFR_UV = np.log10(SFR_UV) 

plt.plot(logMstar[p1_index], logSFR_UV[p1_index], '*k', label='$z=0.47-0.62$')
plt.xlabel(r'$\log(M/M_{\odot})$',fontsize=16)
plt.ylabel(r'$\log$(SFR$_{\rm UV}$)',fontsize=16)
plt.legend()
plt.savefig('hwk4_fig1.pdf')
plt.close()

## Problem 2
print("2. The minimum SFR_UV from galaxies selected in 1.) is:", np.min(SFR_UV[p1_index]), "solar masses per year")
print("2. The maximum SFR_UV from galaxies selected in 1.) is:", np.max(SFR_UV[p1_index]), "solar masses per year")
print("2. The median SFR_UV from galaxies selected in 1.) is:", np.median(SFR_UV[p1_index]), "solar masses per year")

## Problem 3
SFR_tot = SFR_UV + SFR_IR

logSFR_tot = np.log10(SFR_tot)

p2_index = np.where(whmips[p1_index] == 1)[0]

plt.plot(logMstar[p1_index][p2_index][np.where(SFR_tot[p1_index][p2_index] >= 3.)], logSFR_tot[p1_index][p2_index][np.where(SFR_tot[p1_index][p2_index] >= 3.)], '*r',
         label=r'SFR$_{\rm tot} \geq 3.0 M_{\odot}$ yr$^{-1}$')
plt.plot(logMstar[p1_index][p2_index][np.where(SFR_tot[p1_index][p2_index] < 3.)], logSFR_tot[p1_index][p2_index][np.where(SFR_tot[p1_index][p2_index] < 3.)], '*k',
         label=r'SFR$_{\rm tot} < 3.0 M_{\odot}$ yr$^{-1}$')

plt.xlabel(r'$\log(M/M_{\odot})$',fontsize=16)
plt.ylabel(r'$\log$(SFR$_{\rm tot}$)',fontsize=16)
plt.legend()
plt.savefig('hwk4_fig2.pdf')
plt.close()

## Problem 4

print("4. The minimum SFR_tot from galaxies selected in 3.) is:", np.min(SFR_tot[p1_index][p2_index]), "solar masses per year")
print("4. The maximum SFR_tot from galaxies selected in 3.) is:", np.max(SFR_tot[p1_index][p2_index]), "solar masses per year")
print("4. The median SFR_tot from galaxies selected in 3.) is:", np.median(SFR_tot[p1_index][p2_index]), "solar masses per year")
print("4. The median SFR_UV from galaxies selected in 3.) is:", np.median(SFR_UV[p1_index][p2_index]), "solar masses per year")

R = np.median(SFR_tot[p1_index][p2_index]) / np.median(SFR_UV[p1_index][p2_index])

print("4. The ratio R is:", R)

## Problem 5

plt.hist(SFR_UV[p1_index][p2_index], bins=20, density=True, linestyle='--', histtype='step',label=r'SFR$_{\rm UV}$')
plt.hist(SFR_tot[p1_index][p2_index], bins=20, density=True, histtype='step',label=r'SFR$_{\rm tot}$')
plt.legend()
plt.ylabel('Fraction of Galaxies')
plt.xlabel(r'SFR ($M_{\odot}$ yr$^{-1}$)')
plt.savefig('hwk4_fig3.pdf')
plt.close()

## Problem 6

p31_index = np.where(Mstar[p1_index][p2_index] > 4.3e10)
p32_index = np.where(SFR_tot[p1_index][p2_index] > 3)

print("p31_indices:", p31_index)
print("p32_indices:", p32_index)
print("Elements of Mstar selected from p31_index:", Mstar[p1_index][p2_index][p31_index])

print("6. The number of galaxies selected in 3.) with M* greater than MW is:", len(p31_index[0]))
print("6. The number of galaxies selected in 3.) with SFR greater than MW is:", len(p32_index[0]))

## Problem 7

mass_sorted_ind = np.argsort(Mstar[p1_index][p2_index])

mass_top_30 = mass_sorted_ind[-30:]

print("length of sorted indices array:", len(mass_sorted_ind))
print("elements of sorted Mass array:", Mstar[p1_index][p2_index][mass_top_30])

np.savetxt('list.massive.hwk4.txt',np.c_[ID[p1_index][p2_index][mass_top_30], SExtractor_ID[p1_index][p2_index][mass_top_30], str_ID[p1_index][p2_index][mass_top_30], \
                                            x_pos[p1_index][p2_index][mass_top_30], y_pos[p1_index][p2_index][mass_top_30], ACS_F606W[p1_index][p2_index][mass_top_30], \
                                            ACS_F850LP[p1_index][p2_index][mass_top_30], phot_z[p1_index][p2_index][mass_top_30], r_mag[p1_index][p2_index][mass_top_30], \
                                            Mstar[p1_index][p2_index][mass_top_30], SFR_UV[p1_index][p2_index][mass_top_30], whmips[p1_index][p2_index][mass_top_30], \
                                            SFR_IR[p1_index][p2_index][mass_top_30]], fmt='%18s')

## Problem 8

sfr_sorted_ind = np.argsort(SFR_tot[p1_index][p2_index])

sfr_top_30 = sfr_sorted_ind[-30:]

np.savetxt('list.sfr.hwk4.txt',np.c_[ID[p1_index][p2_index][sfr_top_30], SExtractor_ID[p1_index][p2_index][sfr_top_30], str_ID[p1_index][p2_index][sfr_top_30], \
                                            x_pos[p1_index][p2_index][sfr_top_30], y_pos[p1_index][p2_index][sfr_top_30], ACS_F606W[p1_index][p2_index][sfr_top_30], \
                                            ACS_F850LP[p1_index][p2_index][sfr_top_30], phot_z[p1_index][p2_index][sfr_top_30], r_mag[p1_index][p2_index][sfr_top_30], \
                                            Mstar[p1_index][p2_index][sfr_top_30], SFR_UV[p1_index][p2_index][sfr_top_30], whmips[p1_index][p2_index][sfr_top_30], \
                                            SFR_IR[p1_index][p2_index][sfr_top_30]], fmt='%18s')
