# Last updated: 8/4/2026, 5:52:11 PM
1class Solution(object):
2    def dayOfYear(self, date):
3        from datetime import datetime
4        date_object = datetime.strptime(date, '%Y-%m-%d')
5        day_of_year = date_object.timetuple().tm_yday
6        return(day_of_year)