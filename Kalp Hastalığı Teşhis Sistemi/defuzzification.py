import numpy as np


class Defuzzification:
    def __init__(self, fuzzification):
        
        self.fuzzification = fuzzification


    def get_center_of_mass(self, health):
      
        points = np.linspace(0, 4, 1000)
        
        sigma_mu_x = 0.0
        sigma_mu = 0.0
     
        for i in range(len(points)):
            fuzzy_values_of_point = self.fuzzification.get_fuzzy_value('health', points[i])
            healthy = min(health['healthy'], fuzzy_values_of_point['healthy'])
            sick_1 = min(health['sick_1'], fuzzy_values_of_point['sick_1'])
            sick_2 = min(health['sick_2'], fuzzy_values_of_point['sick_2'])
            sick_3 = min(health['sick_3'], fuzzy_values_of_point['sick_3'])
            sick_4 = min(health['sick_4'], fuzzy_values_of_point['sick_4'])
            overall_health = max(healthy, sick_1, sick_2, sick_3, sick_4)
            
            sigma_mu_x += overall_health * points[i]
            sigma_mu += overall_health

        
        if sigma_mu == 0:
            return 0
       
        else:
            return sigma_mu_x / sigma_mu

   
    def get_health_status(self, inference_result):
        health_status = []
        center_of_mass = self.get_center_of_mass(inference_result)
        if center_of_mass < 1.78:
            health_status.append("healthy")
        if 1 <= center_of_mass <= 2.51:
            health_status.append("sick1")
        if 1.78 <= center_of_mass <= 3.25:
            health_status.append("sick2")
        if 1.5 <= center_of_mass <= 4.5:
            health_status.append("sick3")
        if 3.25 < center_of_mass:
            health_status.append("sick4")

        
        return ' & '.join(health_status) + ": " + str(center_of_mass)
