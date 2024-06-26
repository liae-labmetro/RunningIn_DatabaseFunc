# Call functions from root folder
import sys, os
sys.path.append(os.path.abspath('.'))

from source.waveformConversion import Waveform
import seaborn as sns
import matplotlib.pyplot as plt

wvf = Waveform.read_labview_waveform("D:\Dados - Thaler\Documentos\Amaciamento\RunningIn_DatabaseFunc\corr2511.dat",0)

sns.relplot(kind="line", x=wvf.time, y=wvf.data)
plt.show()