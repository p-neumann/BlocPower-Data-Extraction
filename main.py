from Utils.NetworkManager import NetworkManager
from Utils.WorkSheetWriter import WorksheetWriter
import constants

def main():
    networkManager = NetworkManager(constants.OPEN_BALTIMORE_URL_GENERAL)
    worksheetWriter = WorksheetWriter()
    
    networkManager.fetchData()
    extractedData = networkManager.processExtractedData()

    worksheetWriter.writeDataToWorksheet(extractedData)

if __name__ == "__main__":
    main()
    
    
    
    



