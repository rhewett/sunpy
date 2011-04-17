"""SDO Map subclass definitions

Author: `Keith Hughitt <keith.hughitt@nasa.gov>`
"""
__author__ = "Keith Hughitt"
__email__ = "keith.hughitt@nasa.gov"

from sunpy.data.map import BaseMap
from datetime import datetime
import matplotlib.colors as colors
import matplotlib.cm as cm

# Note: Trailing "Z" in date was dropped on 2010/12/07
date_format = "%Y-%m-%dT%H:%M:%S.%f"

class AIAMap(BaseMap):
    """AIA Image Map definition"""
    def __new__(self, data, header):
        return BaseMap.__new__(self, data, header)

    @classmethod
    def get_properties(self, header):
        """Returns the default and normalized values to use for the Map"""
        properties = BaseMap.get_properties()
        properties.update({
            'date': datetime.strptime(header['date-obs'][0:22], date_format),
            'det': "AIA",
            'inst': "AIA",
            'meas': header['wavelnth'],
            'obs': "SDO",
            'name': "AIA %s" % header['wavelnth'],
            'r_sun': header['rsun_obs']
        })
        return properties
        
    @classmethod
    def is_datasource_for(self, header):
        """Determines if header corresponds to an AIA image"""
        return header['telescop'] == 'SDO/AIA'
        
class HMIMap(BaseMap):
    """HMI Image Map definition"""
    def __new__(self, data, header):        
        return BaseMap.__new__(self, data, header)
        
    @classmethod
    def get_properties(self, header):
        """Returns the default and normalized values to use for the Map"""
        meas = header['content'].split(" ")[0].lower()
        
        properties = BaseMap.get_properties()
        properties.update({
            "norm": None,
            "date": datetime.strptime(header['date-obs'][0:22], date_format),
            "det": "HMI",
            "inst": "HMI",
            "meas": meas,
            "obs": "SDO",
            "name": "HMI %s" % meas,
            "r_sun": header['rsun_obs']
        })
        return properties
        
    @classmethod
    def is_datasource_for(self, header):
        """Determines if header corresponds to an HMI image"""
        return header['instrume'][0:3] == 'HMI'
