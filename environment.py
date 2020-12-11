# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 10:02:58 2020

@author: sattwik
"""

import numpy as np

#BUILDING THE ENVIRONMENT

class Environment(object):
    
    #INTRODUCING AND INITIALIZING ALL THE PARAMETERS AND VARIABLES OF THE ENVIRONMENT
    def __init_(self, optimal_temperature =(18.0, 24.0), initial_month=0, initial_number_users = 10, initial_rate_data = 60):
        self.monthly_atmostpheric_temperature=[1.0, 5.0, 7.0, 10.0, 11.0, 20.0, 23.0, 24.0, 22.0, 10.0, 5.0, 1.0]
        self.initial_month=initial_month
        self.atmospheric_temperature=self.monthly_atmostpheric_temperature[initial_month]
        self.optimal_temperature = optimal_temperature
        self.min_temperature=-20
        self.max_temperature = 80
        self.min_number_users = 10
        self.max_number_users = 100
        self.max_update_users = 5
        self.min_rate_data = 20
        self.max_rate_data = 300
        self.max_update_data = 10
        self.initial_number_users = initial_number_users
        self.current_number_users = initial_number_users
        self.initial_rate_data =initial_rate_data
        self.current_rate_data =initial_rate_data
        
        self.intrinsic_temperature = self.atmospheric_temperature + 1.25*self.current_number_users + 1.25*self.current_rate_data
        self.temperature_ai = self.intrinsic_temperature
        self.temperature_noai = self.optimal_temperature[0]+self.optimal_temperature[1]/2.0
        
        self.total_energy_ai = 0.0
        self.total_energy_noai = 0.0
        
        self.reward = 0.0
        self.game_over = 0
        self.train = 1
    
    
    #MAKING A METHOD TO UPDATE THE ENVIRONMENT RIGHT AFTER THE AI PLAYS AN ACTION
    
    
    
    #MAKING A METHOD TO RESET THE ENVIRONMENT
    
    
    
    #MAKING A METHOD TO RETURN THE CURRENT STATE; LAST REWARD AND WHETHER THE GAME 