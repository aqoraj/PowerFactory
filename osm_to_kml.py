import osmnx as ox
import geopandas as gpd
from shapely.geometry import Point, LineString
from fastkml import kml

def get_power_grid_elements(country_name):
    # Define the tags for power grid elements
    tags = {
        'power': ['line', 'minor_line', 'cable', 'substation', 'tower', 'pole', 'generator']
    }

    # Get the geometries for the specified country
    gdf = ox.geometries_from_place(country_name, tags)

    return gdf

def export_to_kml(gdf, output_file):
    # Create a KML object
    k = kml.KML()
    ns = '{http://www.opengis.net/kml/2.2}'

    # Create a KML document
    doc = kml.Document(ns, 'docid', 'Power Grid Elements', 'Power grid elements from OSM')

    # Add the geometries to the KML document
    for idx, row in gdf.iterrows():
        if isinstance(row.geometry, (Point, LineString)):
            placemark = kml.Placemark(ns, str(idx), row['power'], '')
            placemark.geometry = row.geometry
            doc.append(placemark)

    # Append the document to the KML object
    k.append(doc)

    # Write the KML object to a file
    with open(output_file, 'w') as f:
        f.write(k.to_string(prettyprint=True))

if __name__ == "__main__":
    country_name = "Albania"  # Change this to the desired country
    output_file = "power_grid_elements.kml"

    # Get power grid elements
    gdf = get_power_grid_elements(country_name)

    # Export to KML
    export_to_kml(gdf, output_file)

    print(f"Exported power grid elements to {output_file}")
