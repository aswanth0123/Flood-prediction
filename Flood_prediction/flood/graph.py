from .prediction import *
def details_list():
    data=pd.read_csv("flood/kerala.csv")

    year_list=data["YEAR"]
    year_list.tolist()
    year_list=list(year_list)
    rain_list=data["ANNUAL RAINFALL"]
    rain_list.tolist()
    rain_list=list(rain_list)
    return year_list,rain_list

