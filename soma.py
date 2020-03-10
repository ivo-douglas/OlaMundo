x = int(input("entre a quantidade em horas deste exato momento: "))
                
y = int(input("entre a quantidade em horas que você quer esperar, antes do alarme tocar: "))
                  
hours_sum = x + y

hour_sum_to_alarm_ring_in_hours = hours_sum % 24

hour_sum_to_alarm_ring_in_days= hours_sum // 24

print("o alarme tocara daqui", hour_sum_to_alarm_ring_in_days, "dias e em", hour_sum_to_alarm_ring_in_hours, "horas")
