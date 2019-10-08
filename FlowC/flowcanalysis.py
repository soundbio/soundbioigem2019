from FlowCytometryTools import FCMeasurement
import matplotlib.pyplot as plt

def avg(a):
    return sum(a)/len(a)

i=1
filepath=r'C:\Users\hari8\Desktop\20191007_154820'
# change this to your file path to the unzipped folder with fcs data
well=[0] # indexing will be from 1 for well and filtered data

a=0.25 # the lower percentile cutoff for FSC and SSC
b=0.75 # the higher percentile cutoff for FSC and SSC

count=24 # number of wells/files total


while i<=12: # replaced with count if all files in one location
    well.append(FCMeasurement(ID='well{}'.format(i), datafile=filepath+'\A{}.fcs'.format("%02d" % i)).data)
    i=i+1;
i=1

while i<=12:
    well.append(FCMeasurement(ID='well{}'.format(i), datafile=filepath+'\E{}.fcs'.format("%02d" % i)).data)
    i=i+1;
    
    
renamed=[well[i].rename(columns={"SSC-A" : "SSCA", "FSC-A" : "FSCA"}) for i in range(1, count+1)]
# dashes in names don't work in the query step

slowcutoff = [renamed[i]['SSCA'].quantile(a) for i in range(0, count)] # SSC low cutoff value for each well
shighcutoff = [renamed[i]['SSCA'].quantile(b) for i in range(0, count)]# SSC high cutoff value for each well

flowcutoff = [renamed[i]['FSCA'].quantile(a) for i in range(0, count)]# FSC low cutoff value for each well
fhighcutoff = [renamed[i]['FSCA'].quantile(b) for i in range(0, count)]# FSC high cutoff value for each well
i=0
filtered=[0]

while i<count:
    
    highf=fhighcutoff[i]
    lowf=flowcutoff[i]
    highs=shighcutoff[i]
    lows=slowcutoff[i]
    
    filtered.append(renamed[i].query('@lowf <= FSCA <= @highf & @lows <= SSCA <= @highs')) # the filtering
    i=i+1
    
    
mean=[0]
meanf=[0]
[mean.append(sum(well[i]['FL1-A'])/len(well[i]['FL1-A'])) for i in range(1, count+1)] # mean of FL1-A of unfiltered
[meanf.append(sum(filtered[i]['FL1-A'])/len(filtered[i]['FL1-A'])) for i in range(1, count+1)] # mean of FL1-A of filtered

# NOTE : mean and meanf are indexed from 1 again

plt.figure(1)
plt.title("Avg. FL1-A across wells - all data")
plt.bar([i for i in range(1, count+1)], mean[1:])
plt.xticks([i for i in range(1, count+1)])
plt.grid(True)

plt.figure(2)
plt.title("Avg. FL1-A across wells - between {} and {} percentile FSC & SSC".format(a, b))
plt.bar([i for i in range(1, count+1)], meanf[1:])
plt.xticks([i for i in range(1, count+1)])
plt.grid(True)

# this last graph should be formatted according to each experiment's wells

plt.figure(3)
plt.title("Avg. FL1-A across group - between {} and {} percentile FSC & SSC".format(a, b))
plt.bar([i for i in range(1, 7)], [avg([meanf[i], meanf[i+1], meanf[i+12], meanf[i+13]]) for i in range(1, 12, 2)])
plt.xticks([i for i in range(1, 7)])