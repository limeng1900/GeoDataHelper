
class _const:
    class ConstError(TypeError): pass
    class ConstCaseError(ConstError): pass

    def __setattr__(self, name, value):
          if name in self.__dict__:
              raise self.ConstError("can't change const %s" % name)
          if not name.isupper():
              raise self.ConstCaseError('const name "%s" is not all uppercase' % name)
          self.__dict__[name] = value


CONST = _const()
CONST.EPSG = {
    'WGS84': 4326,
    'BJ54': 4214,
    'XIAN80': 4610,
    'CGCS2000': 4490
}
CONST.FILE_EXT = {
    'ESRI Shapefile': 'shp',
    'GeoJSON': 'json',
    'CSV': 'csv'
}
