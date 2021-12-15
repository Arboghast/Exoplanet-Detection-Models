import lightkurve as lk
import matplotlib.pyplot as plt
import numpy as np
from io import BytesIO
import os.path
import tensorflow as tf
import base64

def find_tce(kepid, tce_plnt_num, filenames):
    for filename in filenames:
        for record in tf.compat.v1.python_io.tf_record_iterator(filename):
            ex = tf.train.Example.FromString(record)
            if (ex.features.feature["kepid"].int64_list.value[0] == kepid and
                ex.features.feature["tce_plnt_num"].int64_list.value[0] == tce_plnt_num):
                print("Found {}_{} in file {}".format(kepid, tce_plnt_num, filename))
                return ex
    raise ValueError("{}_{} not found in files: {}".format(kepid, tce_plnt_num, filenames))

def getLocalView(kepid, dir):
    filenames = tf.io.gfile.glob(os.path.join(dir, "*"))
    assert filenames, "No files found in {}".format(dir)
    ex = find_tce(kepid, 1, filenames)

    # Get the local view.
    local_view = np.array(ex.features.feature["local_view"].float_list.value)
    return local_view

def downloadLC_kepler(target):
    #search and download target light curve
    search_result = lk.search_lightcurve(target, author='Kepler', cadence='long')

    kep_id = search_result.target_name.data[0]
    kep_id = kep_id[4:] #substr to remove "kplr" prefix
    kep_id = int(kep_id.lstrip("0"))

    local_view = getLocalView(kep_id, "../Kepler/TFRecords")
    local_view_matrix = np.expand_dims(local_view,axis=0)
    return local_view_matrix

#error handling for downloading
def downloadLC_kaggle(target):
    light_curve = lk.search_lightcurve(target, author='Kepler', cadence='long', quarter=3).download()
    light_curve = light_curve.flatten().remove_outliers()
    flux = np.array(light_curve.flux)
    flux = np.expand_dims(flux, axis=0)
    return flux

def getTPFimg(target):
    tpf = lk.search_targetpixelfile(target, author="Kepler", cadence="long")
    tpf = tpf.download()
    tpf.plot()
    tmpfile = BytesIO()
    plt.savefig(tmpfile, format='png')
    encoded = base64.b64encode(tmpfile.getvalue())
    return str(encoded)

def getLCimg(target):
    lc = lk.search_lightcurve(target, author='Kepler', cadence='long')
    lc = lc.download()
    lc.plot()
    tmpfile = BytesIO()
    plt.savefig(tmpfile, format='png')
    encoded = base64.b64encode(tmpfile.getvalue())
    return str(encoded)
    
