from .prediction import *
def details_list():
    data=pd.read_csv("flood/kerala.csv")

    year_list=data["YEAR"]
    year_list.tolist()
    year_list=list(year_list)
    # year_list.reverse()
    print(year_list)
    rain_list=data["ANNUAL RAINFALL"]
    rain_list.tolist()
    rain_list=list(rain_list)
    # rain_list.reverse()
    return year_list,rain_list

