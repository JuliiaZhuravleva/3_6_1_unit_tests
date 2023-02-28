import data
from main import filter_geo_logs_by_country, get_unique_geo_ids, get_percent, get_queries_stats

import pytest


@pytest.mark.parametrize(
    'geo_logs, country, result', [
        (data.geo_logs, 'Россия', data.test_geo_logs_russia),
        (data.geo_logs, 'Франция', data.test_geo_logs_france),
        (data.geo_logs, 'Япония', [])
    ]
)
def test_filter_geo_logs_by_country_full(geo_logs, country, result):
    res = filter_geo_logs_by_country(geo_logs, country)
    assert res == result


@pytest.mark.parametrize(
    'country', [('Россия'), ('Франция'), ('Индия'), ('Португалия')]
)
def test_filter_geo_logs_only_one_country(country):
    res = filter_geo_logs_by_country(data.geo_logs, country)
    res_countries = set([log[list(log)[0]][1] for log in res])
    assert len(res_countries), 1


@pytest.mark.parametrize(
    'country', [('Россия'), ('Франция'), ('Индия'), ('Португалия')]
)
def test_filter_geo_logs_check_country(country):
    res = filter_geo_logs_by_country(data.geo_logs, country)
    res_countries = set([log[list(log)[0]][1] for log in res])
    res_country = list(res_countries)[0]
    assert res_country == country


@pytest.mark.parametrize(
    'geo_ids, result', [
        (data.ids, data.test_unique_ids_res),
        ({'user1': [213]}, [213]),
        ({'user1': [213],
          'user2': [213]}, [213])
    ]
)
def test_get_unique_geo_ids_full(geo_ids, result):
    res = get_unique_geo_ids(geo_ids)
    assert res == result


@pytest.mark.parametrize(
    'value, total, result', [
        (5, 10, '50%'),
        (5, 4, '125%'),
        (3, 900, '0%'),
        (3, 70, '4%'),
        (1, 70, '1%'),
    ]
)
def test_get_percent_full(value, total, result):
    res = get_percent(value, total)
    assert res == result


@pytest.mark.parametrize(
    'queries, result', [
        (data.queries, data.test_queries_res),
        ('1', {1: '100%'}),
        (['1 2 3'], {3: '100%'}),
        (['1', '1 2'], {1: '50%', 2: '50%'})
    ]
)
def test_get_queries_stats_full(queries, result):
    res = get_queries_stats(queries)
    assert res == result
