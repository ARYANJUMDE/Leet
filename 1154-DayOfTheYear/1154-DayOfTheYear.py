# Last updated: 9/9/2026, 10:14:47 PM
class Solution(object):
    def dayOfYear(self, date):
        from datetime import datetime
        date_object = datetime.strptime(date, '%Y-%m-%d')
        day_of_year = date_object.timetuple().tm_yday
        return(day_of_year)