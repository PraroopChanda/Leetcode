class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        hour_angle=360/12 
        minute_angle=360/60
        hour_minute_angle=(360)/(12*60)

        hour_angle_with_12=(hour % 12) * hour_angle + (minutes) * hour_minute_angle ## compute the angle of both with respect to 12
        minutes_angle_with_12= (minutes * minute_angle)

        angle_difference=abs(minutes_angle_with_12-hour_angle_with_12)
        return min(angle_difference,360-angle_difference)





        