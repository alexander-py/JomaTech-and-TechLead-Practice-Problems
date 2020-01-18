#find how many stones are jewels
#easily and quickly solved with python

class Solution:
    def numJewelsInStones(self, J: 'str', S: 'str') -> 'int':
        counter = 0

        for i in J:
            counter += S.count(i)

        return(counter)
