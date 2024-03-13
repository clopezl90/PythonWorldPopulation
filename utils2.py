import read_csv
import charts

def run():
    data = read_csv.read_csv('data.csv')
    data = list(filter(lambda row: row['Continent'] == 'North America', data))
    countries = list(map(lambda row: row['Country/Territory'],data))
    percentages = list(map(lambda row: row['World Population Percentage'], data))
    print(countries)
    charts.generate_pie_chart(countries,percentages)
        
      


def population_by_country(data, country):
    
  result = list(filter(lambda item: item['Country/Territory'] == country, data))
  return result

def get_population(country_dict):
    population_dict = {
        '2022' : int(country_dict['2022 Population']),
        '2020' : int(country_dict['2020 Population']),        
        '2015' : int(country_dict['2015 Population']),
        '2010' : int(country_dict['2010 Population']),
        '2000' : int(country_dict['2000 Population']),
        '1990' : int(country_dict['1990 Population']),
        '1980' : int(country_dict['1980 Population'])
        
    }
    labels = population_dict.keys()
    values = population_dict.values()
    return labels, values

if __name__ == "__main__":
    run()