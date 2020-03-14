from Buttons import GreenButton, BlueButton, RedButton

class AbstractFactory:

    @staticmethod
    def CreateGreenButton():
        return GreenButton()
    
    @staticmethod
    def CreateBlueButton():
        return BlueButton()
    

    @staticmethod
    def CreateRedButton():
        return RedButton()
