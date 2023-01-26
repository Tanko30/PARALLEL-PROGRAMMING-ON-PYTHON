#!/home/mrpinformcc/anaconda3/bin/python

#####################################################################################################################################################
 #
 # [Author]:(CCI, 2021) Group 3, [BAYA Ernest Kwame, BOUBAKAR Zourkalaini, JAWLA Haddy]
 # [Date]: Thu Jun 17, 2021 
 # [Goal]: Compute mean and max temperature from csv time series dataset
 # [Version]: 2.0 (last version)
 # [Execution]: /home/mrpinformcc/anaconda3/bin/python
 #
 ########################################################################################################################################################

#packages 
import numpy as np#to convert dataframe to numpy array
import pandas as pd #to read the csv dataset
import multiprocessing as mp#for multiprocessing task
from tabulate import tabulate#for the final result displaying

############################ Reading and cleaning dataset ###################################################
temp_by_city = pd.read_csv('GlobalLandTemperaturesByCity.csv',parse_dates=[0], infer_datetime_format=True)#8599212 rows × 7 columns
temp_by_city = temp_by_city.dropna()#drop rows with NaN
#############################################################################################################

###################### Start Function: MeanTemp() #################################################
def MeanTemp(temp):
    """perfom average temperature on temperature data for each country"""

    #make series of country
    temp_country = temp['Country'].unique()
    temp_mean_array=[]

    for i in range(len(temp_country)):
        #transform df to np.array and compute global average temperature
        temp_mean=(temp.loc[temp['Country']==temp_country[i]]['AverageTemperature'].to_numpy()).mean()
    
        #add new global average temperature value to the list
        temp_mean_array=np.append(temp_mean_array, temp_mean)

    #create DataFrame from results
    country_temp_mean =  pd.DataFrame({'Country' : temp_country, 'AverageTemperature' : temp_mean_array } )
    return country_temp_mean
############################# end Function: MeanTemp() ######################################


############################ Start Function: MaxTemp() #######################################
def MaxTemp(temp):
    """find max temperature on temperature data for each country"""

    #make series of country
    temp_country = temp['Country'].unique()
    country_array =[]
    temp_max_array=[]
    city_array=[]
    date_array=[]
    

    for i in range(len(temp_country)):
        #find max temperature and transform df to np.array
        temp_data=(temp.loc[temp['Country']==temp_country[i]][['Country','AverageTemperature','City','dt']].max()).to_numpy()
    
        country_array=np.append(country_array, temp_data[0])
        temp_max_array=np.append(temp_max_array, temp_data[1])
        city_array=np.append(city_array, temp_data[2])
        date_array=np.append(date_array, temp_data[3])

    #create DataFrame from results
    country_temp_max =  pd.DataFrame({'Country' : temp_country, 'AverageTemperature' : temp_max_array, 'City' : city_array, 'dt' : date_array } )
    return country_temp_max
########################## End Function: MaxTemp() ################################################################

########################## Start Function: Parallelize() ###########################################################
def Parallelize(dataframe, func):
    dataframe_split = np.array_split(dataframe, partitions)
    pool = mp.Pool(cores)
    dataframe_return = pd.concat(pool.map(func, dataframe_split), ignore_index=True)
    pool.close()
    return dataframe_return
########################### End Function: Parallelize() ###########################################################

###################################################################################################################
########################### Main Function #########################################################################
###################################################################################################################
if __name__ == '__main__':
    cores = mp.cpu_count()#get the number of cores 
    partitions = cores

    #Global Average Temperature for each country
    mean_parallel_dataframe = Parallelize(temp_by_city, MeanTemp) #648 rows × 2 columns with cores = 8 on this computer
    mean_temp = MeanTemp(mean_parallel_dataframe)
    mean_temp =  mean_temp.rename(columns = {'AverageTemperature':'GlobalAverageTemperature'})#rename the column
    print(tabulate(mean_temp, headers='keys', tablefmt='grid', numalign='center', stralign='center'))
    print('')
    #Maximum Temperature for each country
    print('')
    max_parallel_dataframe = Parallelize(temp_by_city, MaxTemp) #648 rows × 2 columns with cores = 8 on this computer
    max_temp = MaxTemp(max_parallel_dataframe)
    max_temp =  max_temp.rename(columns = {'AverageTemperature':'HighestTemperature', 'dt':'Date'})#rename the column
    print(tabulate(max_temp, headers='keys', tablefmt='grid', numalign='center', stralign='center'))

