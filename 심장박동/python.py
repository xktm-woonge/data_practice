import re
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
plt.style.use('dark_background')

file_path = '내보내기/apple_health_export/export_cda.xml'

df = pd.DataFrame([], columns=['data', 'bpm'])

pattern = '^.*IdentifierHeartRate".*startDate="(.{19}).*value=")[0-9]*).*$'

with open(file_path, 'r') as f:
    for line in f:
        search = re.search(pattern, line)
        if search is not None:

            df = df.append({
                'date' : search.group(1),
                'bpm':search.group(2)
            }, ignore_index=True)

df.date = pd.to_datetime(df.date)
df.bpm = pd.to_numeric(df.bpm)

df = df.set_index('date')
df = df.sort_index()

df.head()