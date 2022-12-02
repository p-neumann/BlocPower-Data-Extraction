from typing import List
import requests

class NetworkManager:

    def __init__(self, url: str):
        self.url = url
        self.data = None

    def fetchData(self) -> None:
        self.performRequest(self.url)

    def performRequest(self, url: str) -> None:

        response = requests.get(url)
        if response.status_code == 200:
            self.handleRequestSuccess(response)
        else:
            self.handleRequestFailure()
    
    def handleRequestSuccess(self, response) -> None:
        self.data = response.json()
    
    def handleRequestFailure(self) -> None:
        print("Response status was not ok")

    def processExtractedData(self) -> List[str]:

        if not self.data:
            print("No data to process")
            return
        
        dataList = []
        for object in self.data["features"]:
            row = []
            for key, value in object["attributes"].items():
                row.append((key, value))
            row.sort()

            arr = []
            for c in row:
                arr.append(c[1])
            dataList.append(arr)

        return dataList