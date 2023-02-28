import unittest
from random import choice
from unittest import TestCase

import data
from main import filter_geo_logs_by_country, get_unique_geo_ids, get_percent, get_queries_stats


class TestFilterGeoLogsByCountry(TestCase):
    def test_russia_country(self):
        res = filter_geo_logs_by_country(data.geo_logs, 'Россия')
        self.assertListEqual(res, data.test_geo_logs_russia)

    def test_if_only_one_country(self):
        res = filter_geo_logs_by_country(data.geo_logs, 'Россия')
        res_countries = set([log[list(log)[0]][1] for log in res])
        self.assertLessEqual(len(res_countries), 1,
                             msg='В отфильтрованном списке должно не больше одной страны')

    def test_if_only_russia_country(self):
        res = filter_geo_logs_by_country(data.geo_logs, 'Россия')
        res_countries = set([log[list(log)[0]][1] for log in res])
        res_country = list(res_countries)[0]
        self.assertEqual(res_country, 'Россия',
                         msg='В отфильтрованном списке должна быть страна: Россия')

    def test_france_country(self):
        res = filter_geo_logs_by_country(data.geo_logs, 'Франция')
        self.assertListEqual(res, data.test_geo_logs_france)
        res_countries = set([log[list(log)[0]][1] for log in res])
        self.assertEqual(len(res_countries), 1,
                         msg='В отфильтрованном списке должно не больше одной страны')
        res_country = list(res_countries)[0]
        self.assertEqual(res_country, 'Франция',
                         msg='В отфильтрованном списке должна быть страна: Франция')

    def test_country_not_in_list(self):
        res = filter_geo_logs_by_country(data.geo_logs, 'Япония')
        self.assertListEqual(res, [],
                             msg='При фильтрации по отсутствующей в списке стране должен вернуться пустой список')


class TestGetUniqueGeoIds(TestCase):
    def test_full_case(self):
        res = get_unique_geo_ids(data.ids)
        self.assertEqual(res, data.test_unique_ids_res)

    def test_unique_ids(self):
        res = get_unique_geo_ids(data.ids)
        random_id = choice(res)
        count_repeat = res.count(random_id)
        self.assertEqual(count_repeat, 1, msg=f'Идентификатор {random_id} не уникальный')


class TestGetPercent(TestCase):
    def test_simple_numbers(self):
        res = get_percent(5, 10)
        self.assertEqual('50%', res)

    @unittest.expectedFailure
    def test_not_numbers(self):
        res = get_percent('1', 10)
        self.assertEqual('10%', res)


class TestGetQueriesStats(TestCase):
    def test_full_case(self):
        res = get_queries_stats(data.queries)
        self.assertDictEqual(res, data.test_queries_res)



