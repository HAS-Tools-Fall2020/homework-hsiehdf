# Team Functions
# ~~~~~~
# This is a script we can read put all of our functions and read into
# the main forecast script

# This is where I will be living for the next couple days
# -Danielle

# %%
import numpy as np
import pandas as pd
import datetime as dt
from sklearn.linear_model import LinearRegression
import json
import urllib.request as req
import urllib
import fiona


# %% Functions
def AR_model_estimate(df, initial_train_date, final_train_date, time_shifts):
    """ Estimate the parameters of an Auto Regressive Model (AR)

    Parameters:
    ----------
    df: Dataframe containing the flow information.
    initial_date: Initial date for the training period in format 'YYYY-MM-DD'.
    final_date: Final date for the training period in format 'YYYY-MM-DD'.
    time_shifts: Number of time shifts to consider in the AR model.

    Returns:
    ---------
    model_intercept: The intercept of the AR Model
    model_coefficients: The coefficients of the AR Model (size=[time_shifts,1])
    r_sq: Determination Coefficient R2 of the AR Model
    """

    # Define the type of model to use
    model_LR = LinearRegression()

    # Start the shift listing with the string 'Flow'
    shift_list = ['flow']

    # Create additional columns to the dataframe to include desired time \
    # shifts
    for i in range(1, time_shifts+1):
        num_shift = 'flow_tm'+str(i)
        df[num_shift] = df['flow'].shift(i)
        shift_list.append(num_shift)

    # Create a dataframe of training data including all columns of df
    train_data = df[initial_train_date:final_train_date][shift_list]

    # Create the dependent array for the AR model
    y_data = train_data['flow']

    # Create the set of independent variables for the AR Model.
    x_data = train_data[shift_list[1:len(shift_list)]]

    # Fit the corresponding AR Model
    model_LR.fit(x_data, y_data)

    # Save the results of the AR Model
    r_sq = np.round(model_LR.score(x_data, y_data), 4)
    model_intercept = np.round(model_LR.intercept_, 2)
    model_coefficients = np.round(model_LR.coef_, 2)

    # Print the results to the user
    print('AR Model with ', time_shifts, ' shifts')
    print('coefficient of determination:', r_sq)
    print('intercept:', model_intercept)
    print('slope:', model_coefficients)

    return model_intercept, model_coefficients, r_sq


def forecast_flows(flow_daily, time_shifts, start_train_date, end_train_date,
                   start_for_date, end_for_date, seasonal):
    """ Forecast the flows for a given number of periods based on flow timeseries

    Parameters:
    -----------
    flow_daily: Dataframe containing the daily flow information. The index of \
            the df should be the date and this df should only include 'flow'.
    time_shifts: Number of time shifts to consider in the AR Model
    start_train_date: Initial date for the training period in format
                      'YYYY-MM-DD'.
    end_train_date: Final date for the training period in format 'YYYY-MM-DD'.
    start_for_date: Initial date for the forecast in format 'YYYY-MM-DD'.
    end_for_date: Final date for the forecast in format 'YYYY-MM-DD'.
    seasonal: Binary condition telling the scale of time of the forecast.

    Returns:
    -----------
    flow_daily: Dataframe with the forecasts in a daily basis
    flow_weekly: Dataframe with the forecasts in a weekly basis
    model_intercept: Intercept from the AR Model
    model_coefficients: List of coefficients from the AR Model
    """

    # Get the location (index) for the day before the start forecasting \
    # date in the original dataframe (data)

    temp_data = flow_daily
    temp_data = temp_data.reset_index()
    temp_data['datetime'] = flow_daily.index  # .strftime('%Y-%m-%d')

    if seasonal == 'week':
        date_before_start = (pd.to_datetime(start_for_date) +
                             dt.timedelta(days=-1)).date()
        index_lag1 = temp_data.loc[temp_data.datetime == str(
            date_before_start)].index[0]
    elif seasonal == 'seasonal':
        flow_daily = flow_daily.resample("W-SUN", closed='left', label='left')\
            .mean()
        index_lag1 = flow_daily.shape[0]-1
        print(index_lag1)
    else:
        print('Please choose a valid time horizon for forecast')

    # Create a list of dates (daily) for the forecast period
    if seasonal == 'week':
        forecast_period = pd.date_range(start=start_for_date,
                                        end=end_for_date, freq='D')
    elif seasonal == 'seasonal':
        forecast_period = pd.date_range(start=start_for_date,
                                        end=end_for_date, freq='W')

    # Estimate the parameters for the best-fit AR Model
    model_intercept, model_coefficients, r_sq = AR_model_estimate(
        flow_daily, start_train_date, end_train_date, time_shifts)

    # Calculate the Forecasts for the indicated time range based on the \
    # selected timeshifts.
    # "lag_i" is used to extract the flow value based on the order of the \
    # AR Model using the index located for the day before the start of \
    # forecast.
    lag_i = index_lag1+1

    # Initialize the variable for the forecasts
    forecast_val = 0

    # Using two loops, the forecasts are calculated between \
    # the desired range of dates, and then appended to the dataframe

    for i in range(0, forecast_period.shape[0]):
        for k in range(0, time_shifts):
            forecast_val += model_coefficients[k] * \
                flow_daily.iloc[lag_i-(k+1)]['flow']
        forecast_val += model_intercept
        lag_i += 1
        flow_daily.loc[forecast_period[i], ['flow']] = forecast_val
        forecast_val = 0

    # Resampling the forecast in a weekly basis, starting on Sundays and \
    # setting the labels and closed interval at the left
    if seasonal == 'week':
        flow_weekly = flow_daily.loc[start_for_date:end_for_date][['flow']].\
            resample("W-SUN", closed='left', label='left').mean()
    elif seasonal == 'seasonal':
        flow_weekly = flow_daily.loc[start_for_date:end_for_date][['flow']]

    # Print the forecasts for the competition
    for i in range(flow_weekly.shape[0]):
        print('\n Week #', str(i+1), '-', flow_weekly.iloc[i].name, '(cfs): ',
              np.round(flow_weekly.iloc[i]['flow'], 2))

    return flow_daily, flow_weekly, model_intercept, model_coefficients


# %%
# Function for Mesowest Temperature & Precipitation data


def prec_temp_data(end_date):

    """ Obtaining Precipitation and Air Temperature from the Mesowest website.


    Parameters
    ----------
    end_date : updated date, to obtain the latest values.

    Returns
    ------
    data_Meso : dataframe with precipitation and temperature per hour
    data_Meso_D : dataframe with the means of precipitation and temperature \
                  per day
    data_Meso_W : dataframe with the means of precipitation and temperature \
                  per week

    """

    # This is the base url that will be the start our final url
    base_url = "http://api.mesowest.net/v2/stations/timeseries"

    # Specific arguments for the data that we want
    args = {
            'start': '199701010000',
            'end': end_date,
            'obtimezone': 'UTC',
            'vars': 'air_temp,precip_accum',
            'stids': 'QVDA3',
            'units': 'temp|C,precip|mm',
            'token': 'demotoken'}

    # Takes your arguments and paste them together into a string for the api
    apiString = urllib.parse.urlencode(args)

    # add the API string to the base_url
    fullUrl = base_url + '?' + apiString
    print('The Mesowest data is obtained from: ', fullUrl)

    # Request the data
    response = req.urlopen(fullUrl)

    # What we need to do now is read this data. The complete format of this:
    responseDict = json.loads(response.read())

    # Create a dictionary. Keys shows the main elements of it.
    responseDict.keys()

    # Get the data we want:
    dateTime = responseDict['STATION'][0]['OBSERVATIONS']['date_time']
    airT = responseDict['STATION'][0]['OBSERVATIONS']['air_temp_set_1']
    precip = responseDict['STATION'][0]['OBSERVATIONS']['precip_accum_set_1']

    # Creating the pandas dataframe
    data_Meso = pd.DataFrame({'Temperature': airT, 'Precipitation': precip},
                             index=pd.to_datetime(dateTime))
    data_Meso_D = data_Meso.resample('D').mean().round(2)
    data_Meso_W = data_Meso.resample('W-SUN').mean().round(2)

    return data_Meso, data_Meso_D, data_Meso_W
