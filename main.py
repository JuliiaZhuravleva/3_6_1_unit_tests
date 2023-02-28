import data
from pprint import pprint


def filter_geo_logs_by_country(geo_logs, country):
    filtered_geo_logs = [visit for visit in geo_logs if list(visit.values())[0][1] == country]
    return filtered_geo_logs


def get_unique_geo_ids(ids):
    uniq_ids = list(set(geo_id for ids_list in ids.values() for geo_id in ids_list))
    return uniq_ids


def get_percent(value: int, total: int):
    return f'{round(value * 100 / total)}%'


def get_queries_stats(queries):
    queries_lengths = [len(query.split()) for query in queries]
    queries_lengths_stats = {length: get_percent(queries_lengths.count(length),
                                                 len(queries_lengths)) for length in set(queries_lengths)}
    return queries_lengths_stats


if __name__ == '__main__':
    required_geo_logs = filter_geo_logs_by_country(data.geo_logs, 'Россия')
    pprint(required_geo_logs)
    unique_geo_ids = get_unique_geo_ids(data.ids)
    print(unique_geo_ids)
    queries_stats = get_queries_stats(data.queries)
    print(queries_stats)