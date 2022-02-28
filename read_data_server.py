import json
from datetime import time, datetime, timedelta

from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)
all_data = pd.read_excel('Sample.xlsx', sheet_name="Sample")


@app.route('/search_api', methods=['POST'])
def search_api():
    data = request.json
    df_filter = all_data.loc[()]
    if 'number' in data.keys():
        df_filter = df_filter.loc[(all_data['Express Number'] == data['number'])]
    elif 'time' in data.keys():
        # time deal ,example utc-8
        df_filter = all_data[
            (all_data['Expected Delivery'] >= datetime.strptime('2022' + data['time'] + ' 00:00', '%Y%b%d %H:%M'))
            & (all_data['Expected Delivery'] <= datetime.strptime('2022' + data['time'] + ' 23:59', '%Y%b%d %H:%M'))]

    elif 'location' in data.keys():
        df_filter = df_filter.loc[(all_data['Current position'].str.contains(data['location']))]
    result_data_array = []
    time_zone = data['time_zone'].split('+')[0].split('-')[0]
    time_zone_value = int(data['time_zone'].replace(time_zone, ''))
    for item in df_filter.iterrows():
        time_format = item[1]['Expected Delivery'] + timedelta(hours=time_zone_value)
        time_result = time_format.strftime("%H:%M %b%d") + "\n(" + time_zone + ")"
        result_data_array.append({"express_num": item[1]['Express Number'],
                                  "current_pos": item[1]['Current position'],
                                  "expect_delivery": time_result})
    return json.dumps(
        {"result": result_data_array})


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
