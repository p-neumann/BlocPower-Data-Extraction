# Aggregation of Baltimore Housing Property Data
The initial phase of the project to collect important housing data within the city of Baltimore and store them in decentralized Solid pods for public view and ownership

## Overview
Dr. Terri Adams (Social Sciences with Howard University) did a whole IRB and is getting the households to agree to have sensors placed in the homes of Washington DC residents. Dr. Arial Saural (Tech side with Howard - Getting data out of the sensors). We wanted to replicate this community-style model and try to gather housing information from different houses in the community. Our goal was to want owner occupied buildings (not just units within buildings), but we may choose to ask for information about each unit as well.
As a pivot from the national scale, we were to limit this to a smaller area focusing on houses surrounding Morgan State University within a specific geographic area.

Our initial focus was to build a process to streamline and store this data somewhere. Ideally, utilizing Solid technology and storing them in pods. Once that data is the pod (Inrupt), we needed to build a dashboard on top of it. We will stand up pods in the area surrounding the Morgan campus, so BDC would request the data from these pods, and the owners of the pods would need to give access if they approve. After meeting with Inrupt, the focus was to shift to data aggregation and how to find useful data sets and extract from them.

With collaboration with Dr. Chouchane and Dr. Sakk from the Computer Science department, our direction was aligned and we had to solve three main problem statements with future implementation

Solid Technology - https://www.inrupt.com/solid

## Problem Statements
- How would we get residents to do anything or share their data to the pod?
- How would we build relationships with city officials so we can easily get this data?
- How would we aggregate this data and more importantly, what kind of analysis would be done on this data? How would we handle gaps in data, and what conclusions can we draw from the analysis?

## Approach
Researching different databases that are open to the public and seeing which house property attributes would be necessary for the overall 360 view of a home

A general data set with various attributes on visual data from the Open Baltimore website was found:

https://data.baltimorecity.gov/datasets/real-property-information-2/explore?location=39.284833%2C-76.620485%2C12.71&showTable=true

A second data set from Open Baltimore on geometry information for housing seemed to be important and was kept for future use:

https://data.baltimorecity.gov/datasets/baltimore::buildings-footprint/explore?location=39.321891%2C-76.597250%2C12.71&showTable=true

On seeing this, the task was then to retrieve the data from the database via the API. Open Baltimore made use of the ArcGIS REST API which allowed us to query for specific properties:

https://developers.arcgis.com/rest/services-reference/enterprise/query-feature-service-layer-.htm#

## Implementation

A Python script was used to network and interact with OpenBaltimore's API to get and migrate real-time data to an Excel spreadsheet.

## Running the Script

### Requirements
- Python (>= version 3.6.0)
  - openpyxl module installed
  - requests module installed
- Spreadsheet software (e.g. Mircosoft Excel)

Note: pip (Python package manager) comes installed automatically with Python, so to install each package with the command `pip install <package>`

After all the setup as been done, you can run the script and the corresponding excel file will be exported to the same directory as the script file.

## Next steps

- Data has to be cleaned to make sure that null values for attributes are taken care of
- Consecutive alignment meetings with Inrupt and Morgan State faculty
