import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

quality = ctrl.Antecedent(np.arange(0, 11, 1), 'quality')
service = ctrl.Antecedent(np.arange(0, 11, 1), 'service')
wait_time = ctrl.Antecedent(np.arange(0, 61, 1), 'wait_time')  

tip = ctrl.Consequent(np.arange(0, 26, 1), 'tip')

quality.automf(3)  
service.automf(3)  

wait_time['long'] = fuzz.trimf(wait_time.universe, [30, 60, 60])  
wait_time['medium'] = fuzz.trimf(wait_time.universe, [15, 30, 45])  
wait_time['short'] = fuzz.trimf(wait_time.universe, [0, 0, 30])  

tip['none'] = fuzz.trimf(tip.universe, [0, 0, 0])  
tip['low'] = fuzz.trimf(tip.universe, [0, 0, 13])  
tip['medium'] = fuzz.trimf(tip.universe, [0, 13, 25])  
tip['high'] = fuzz.trimf(tip.universe, [13, 25, 25])  

rule1 = ctrl.Rule(quality['poor'] & service['poor'], tip['low'])

rule2 = ctrl.Rule(quality['good'] & service['good'], tip['high'])

rule3 = ctrl.Rule(wait_time['long'], tip['none'])

rule4 = ctrl.Rule((wait_time['medium'] | wait_time['short']) & (quality['average'] | service['average']), tip['medium'])

rule5 = ctrl.Rule(wait_time['short'] & service['good'], tip['high'])

tipping_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5])
tipping = ctrl.ControlSystemSimulation(tipping_ctrl)

tipping.input['quality'] = 7  
tipping.input['service'] = 10  
tipping.input['wait_time'] = 20  

tipping.compute()

print(f"O percentual de gorjeta sugerido é: {tipping.output['tip']}%")
