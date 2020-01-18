#task is to defang IP adresses
#easily done with python's ability
#to solve tasks with one liners
#such as the .replace()

class Solution:
    def defangIPaddr(self, address: str) -> str:
            return address.replace(".","[.]")
