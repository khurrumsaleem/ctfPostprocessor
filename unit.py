#/usr/bin/python
#> Conversion factors and procedures used to convert between SI and
## US units.
## Example:
##   m  --> ft :  multiply with the factor 't_m_ft'
##   ft --> m  :  multiply with the factor 't_ft_m'

#icobra
#  This file is a raw file, variable names will be changed DO NOT FORGET.

                                                    
t_ft_in=12.0
t_in_ft=1./t_ft_in
t_in_m = 0.0254
t_ft_m = t_ft_in * t_in_m
t_ft_micron=t_ft_m*1E6
t_m_micron=1.0E6
t_micron_ft=1.0/t_ft_micron
t_m_ft = 1. / t_ft_m
t_m_in = 1. / t_in_m
t_ft_cm = 100. * t_ft_m
t_cm_ft = 1.0/t_ft_cm
t_m_um = 1.0E6
#---------------------------------------------------
# Mass (SI --> US)
t_kg_lbm=2.20462
t_lbm_kg=1.0/t_kg_lbm
t_oz_kg = t_lbm_kg / 16.
t_kg_oz = 1. / t_oz_kg
t_lbm_g = 1000. * t_lbm_kg
t_kg_mg = 1000000.0
t_mg_kg = 1.0/t_kg_mg
t_Mlbm_lbm = 1.0E6
t_lbm_Mlbm = 1.0/t_Mlbm_lbm
#--------------------------------------------------
# Force (SI --> US)
t_lbf_N = 4.4482216152605
t_N_lbf = 1. / t_lbf_N
#---------------------------------------------------
# Temperature differences (SI --> US)
t_K_F = 1.8
t_F_K = 1. / t_K_F
t_F_R = 459.67
t_C_K = 273.15
#---------------------------------------------------
# Pressure (SI --> US)
t_psi_Pa  = t_lbf_N / t_in_m**2
t_psi_atm = t_psi_Pa / 101325.
t_psi_MPa = t_psi_Pa / 1000000.
t_psi_bar = t_psi_Pa / 100000.
t_Pa_psi  = 1. / t_psi_Pa
t_bar_psi = 1. / t_psi_bar
t_MPa_psi = 1. / t_psi_MPa
t_MPa_Pa = 1.0E6
t_MPa_kPa = 1.0E3
t_Pa_MPa = 1./t_MPa_Pa
#---------------------------------------------------
# Energy / Heat  (SI --> US)
#---------------------------------------------------
t_btu_kJ = 1.05505585262
t_btu_J = 1055.05585262
t_kJ_btu = 1. / t_btu_kJ
t_J_btu = 1. / t_btu_J
t_MW_W = 1.0E6
t_kW_W = 1.0E3
t_W_MW = 1./t_MW_W
# Heat Transfer Coefficient (SI --> US)
# [W/(m^2 K)] <--> [btu/(h ft^2 F]
htc_US_SI = t_btu_kJ*1E3/(3.6E3*t_ft_m**2*t_F_K)
htc_SI_US = 1. / htc_US_SI
#---------------------------------------------------
# Thermal Conductivity (SI --> US)
# [W/(m K)] <--> [btu/(h ft F)]
tc_US_SI = t_btu_kJ * 1E3/(3.6E3 * t_ft_m * t_F_K)
tc_SI_US = 1. / tc_US_SI
#---------------------------------------------------
# Specific Heat Capacity (SI --> US)
# [kJ/(kg K)] <--> [btu/(lbm F)]
# Heat Capacity (US --> SI)
shc_US_SI = t_btu_kJ / (t_lbm_kg * t_F_K)
shc_SI_US = 1. / shc_US_SI
t_hr_s=3600.0
t_s_hr=1./t_hr_s
t_day_hr=24.0
t_day_s=t_day_hr*t_hr_s
#> Percent conversion
t_fraction_percent=100.0
t_percent_fraction=1.0/t_fraction_percent

# Temperature conversion function
def C_to_F(tempC):
    C_to_F = 1.8*tempC+32.0
    return C_to_F
                                                         
def F_to_C(tempF):
    F_to_C = (tempF-32.0)/1.8
    return F_to_C
                                                         
def F_to_K(tempF):
    F_to_K = (tempF-32.0)/1.8+273.15
    return F_to_K
                                                         
def K_to_F(tempK):
    K_to_F = 1.8*(tempK-273.15)+32.0
    return K_to_F
                                                         
def C_to_K(tempC):
    C_to_K=tempC+273.15
    return C_to_K
                                                         
def K_to_C(tempK):
    K_to_C=tempK-273.15
    return K_to_C
                                                         
def Convert_pressure_to_psf_rel(psia):
    psfrel=(psia-pref)*t_ft_in**2
    return psfrel


def Convert_pressure_to_psia(psfrel,psia):
    psia=psfrel/t_ft_in**2+pref
    return psia
                                                         
def Psfrel2psia(psfrel):
    Psfrel2psia=psfrel/t_ft_in**2+pref
    return Psfrel2psia
                                                         
def psia2psfrel(psia):
    psia2psfrel = (psia-pref)*t_ft_in**2
    return psia2psfrel
