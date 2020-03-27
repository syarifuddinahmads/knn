import math

listFeature = []
listClass = []
listDataTraining = []
listDataTesting = []
listOutputData = []
K = 5


class Knn:

    def setTypeData(self, arg):
        data = ''
        if arg is 1:
            data = 'Training'
        else:
            data = 'Testing'
        return data

    def inputFeature(self):
        inputJumlahFeature = int(input("Input Jumlah Feature : "))
        for f in range(inputJumlahFeature):
            feature = str(input('Input Feature : '))
            listFeature.append(feature)

    def showFeatureTraining(self):
        print("----- Data Feature -----")
        for ft in range(1, listFeature.__len__()):
            print((ft), ". ", listFeature[ft])
        print("------------------------")

    def inputClass(self):
        inputJumlahClass = int(input("Input Jumlah Class : "))
        for c in range(0, inputJumlahClass):
            classFeature = str(input('Input Class : '))
            listClass.append(classFeature)

    def showClass(self):
        print("----- Data Class -----")
        for lc in range(0, listClass.__len__()):
            print((lc + 1), ". ", listClass[lc])
        print("----------------------")

    def inputData(self):
        print("Pilih Data Input : \n1.Data Training\n2.Data Testing")
        data = int(input("Pilih Data : "))
        print("-----------------------")
        inputJumlahData = int(input("Input Jumlah Data " + Knn().setTypeData(data) + " : "))
        for dt in range(0, inputJumlahData):
            print("Data Ke -", (dt + 1), " : ")
            dataTemp = []
            for ft in range(0, listFeature.__len__()):
                feature = int(input("Input Feature " + listFeature[ft] + " : "))
                dataTemp.append(feature)
            print("Input Class ")
            Knn().showClass()
            classData = int(input("Pilih Class Data : "))
            dataTemp.insert(len(dataTemp), classData)
            if data is 1:
                listDataTraining.append(dataTemp)
            else:
                listDataTesting.append(dataTemp)
        Knn().proccessData()

    def proccessData(self):
        for dt in range(0, listDataTesting.__len__()):
            dataTempTraining = []
            for dtr in range(0, listDataTraining.__len__()):
                totalDataFeature = 0
                for df in range(0, listFeature.__len__()):
                    totalDataFeature += pow(listDataTraining[dtr][df] - listDataTesting[dt][df], 2)
                dataTotal = [dtr, round(math.sqrt(totalDataFeature), 2),
                             (listDataTraining[dtr][listFeature.__len__()] - 1)]
                dataTempTraining.append(dataTotal)
            listOutputData.append(sorted(dataTempTraining, key=lambda x: x[1]))
        Knn().showDataAfterProccess()

    def showDataAfterProccess(self):
        for lod in range(0, listOutputData.__len__()):
            print("Data Testing - ", (lod + 1))
            print("------------------------")
            print("No | Distance | Class")
            print("------------------------")
            for dtr in range(0, listDataTraining.__len__()):
                print((dtr + 1), " | ", listOutputData[lod][dtr][1], "   | ", listClass[listOutputData[lod][dtr][2]])
            print("------------------------")