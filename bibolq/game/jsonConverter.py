import json

data = "1 Pablo, apóstol (no de hombres ni por hombre, sino por Jesucristo y por Dios el Padre que lo resucitó de los muertos), " \
            "2 y todos los hermanos que están conmigo, a las iglesias de Galacia: " \
            "3 Gracia y paz sean a vosotros, de Dios el Padre y de nuestro Señor Jesucristo, " \
            "4 el cual se dio a sí mismo por nuestros pecados para librarnos del presente siglo malo, conforme a la voluntad de nuestro Dios y Padre, " \
            "5 a quien sea la gloria por los siglos de los siglos. Amén."

 

class chapter:
    def __init__(self, data):
        self.data = data
        self.verseFlag = 0
        self.verseNum = 0
        self.actualVs = ""
        self.digits = "0123456789"
        self.dictVs = {}
    

    def separateChapter(self):
        for ch in self.data:
            if ch in self.digits:

                if self.verseFlag == 1:
                    self.verseNum += 1
                    self.dictVs.update({self.verseNum:self.actualVs})
                    self.actualVs = ""
                else:
                    self.verseFlag = 1
            else:
                try:
                    self.actualVs = self.actualVs + ch 
                except:
                    self.actualVs = ch
        self.verseNum += 1
        self.dictVs.update({self.verseNum:self.actualVs})

        return(self.dictVs)


Galatas1 = chapter(data)
Galatas1.separateChapter()
print(Galatas1.dictVs)


