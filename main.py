import pandas as pd

if __name__ == '__main__':
    loyalties_exchange = pd.read_csv("assets/SkyTeam-Exchange.card.csv", sep=",")
    flight_exchange = pd.read_csv("assets/SkyTeam-Exchange.flight.csv", sep=",")
    sit_exchange = pd.read_csv("assets/SkyTeam-Exchange.sit.csv", sep=",")
    print('CSV opened')
    exchange_merged = pd.merge(flight_exchange, loyalties_exchange, how='outer', on='flight_id')
    print('flight_exchange, loyalties_exchange')
    exchange_merged = pd.merge(exchange_merged, sit_exchange, how='outer', on='card_id')
    exchange_merged.to_csv('assets/merged/SkyTeam-Exchange.sit.csv')
