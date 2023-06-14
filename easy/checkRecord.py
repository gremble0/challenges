class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        days_absent = 0
        late_counter = 0

        for c in s:
            if c == 'A':
                days_absent += 1
                late_counter = 0
            elif c == 'L':
                if late_counter == 2:
                    return False
                late_counter += 1
            else:
                late_counter = 0

        if days_absent >= 2:
            return False 
        return True
