import os
import glob
from pkg_resources import resource_filename

# Update the current version when a new version of the forcefield is
# created.
CURRENT_VERSION = "1.0.0"

def get_ff_path(version=None):
    if version:
        return [resource_filename('perfluoroethers',
                                  'xml/versions/{}'.format(version))]
    else:
        return [resource_filename('perfluoroethers',
                                  'xml/current')]


def get_perfluoroether_forcefield_path(version=None):
    for dir_path in get_ff_path(version):
        file_pattern = os.path.join(dir_path, '*.xml')
        file_paths = [file_path for file_path in glob.glob(file_pattern)]
    return file_paths


def get_perfluoroether_forcefield(version=None):
    from foyer import Forcefield
    xml_path = get_perfluoroether_forcefield_path(version)
    ff = Forcefield(xml_path)
    if version:
        ff.version = version
    else:
        ff.version = CURRENT_VERSION
    ff.xml_path = xml_path
    return ff


load_PFE = get_perfluoroether_forcefield
