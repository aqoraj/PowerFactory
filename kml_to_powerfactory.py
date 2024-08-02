# Copyright 2024 by Adem Qoraj.
# All rights reserved.
# This file is part of the PowerFactory Repository, and is released under the "GPL-3.0 license".

import powerfactory
import xml.etree.ElementTree as ET

app = powerfactory.GetApplication() # Calling app Application object

app.SetUserBreakEnabled(0)	#Disable the user break
app.ClearOutputWindow()

# Get filename and identifier for the match
script = app.GetCurrentScript()
filename = script.filename.replace('\\','/')
filename = filename.replace('"','')
identifier = script.identifier


# Function to collect data from KML and update ElmLne coordinates
def kml_to_coordinates(filename: str) -> dict:
    coordinates = {"paths": {}, "points": {}}
    tree = ET.parse(filename)
    root = tree.getroot()

    for placemark in root.findall(".//{http://www.opengis.net/kml/2.2}Placemark"):
        name = placemark.find(".//{http://www.opengis.net/kml/2.2}name").text
        coords = placemark.find(".//{http://www.opengis.net/kml/2.2}coordinates").text
        coords_list = [tuple(map(float, coord.split(","))) for coord in coords.split()]

        if len(coords_list) > 1:
            # Path
            coordinates["paths"][name] = [(lon, lat) for lat, lon, _ in coords_list]
        else:
            # Point
            coordinates["points"][name] = (coords_list[0][1], coords_list[0][0])
            
    return coordinates
    
# Get all lines and update ElmLne coordinates
kml_data = kml_to_coordinates(filename)

for name, coords in kml_data["paths"].items():
    try:
        all_elms = app.GetCalcRelevantObjects('ElmLne')
        dictionary = {getattr(elm, identifier): elm for elm in all_elms}
        element = dictionary.get(name)
        if element:
            # Convert tuples to lists
            coords_list = [list(coord) for coord in coords]
            element.GPScoords = coords_list
            app.PrintPlain(f"Updated coordinates for ElmLne '{name}'.")
        else:
            app.PrintPlain(f"No ElmLne found for path '{name}'.")
    except Exception as e:
        app.PrintPlain(f"Error updating ElmLne coordinates for '{name}': {str(e)}")

app.PrintPlain('ElmLne coordinates updated successfully.')

for name, coords in kml_data["points"].items():
    try:
        all_elms = app.GetCalcRelevantObjects('*.ElmTrfstat,*.ElmSubstat,*.ElmSite')
        dictionary = {getattr(elm, identifier): elm for elm in all_elms}
        element = dictionary.get(name)
        if element:
            element.GPSlat, element.GPSlon = coords
            app.PrintPlain(f"Updated coordinates for: '{name}'.")
        else:
            app.PrintPlain(f"No ElmTrfstat/ElmSubstat/ElmSite found for Point '{name}'.")
    except Exception as e:
        app.PrintPlain(f"Error updating ElmTrfstat/ElmSubstat/ElmSite coordinates for '{name}': {str(e)}")

app.Rebuild()
