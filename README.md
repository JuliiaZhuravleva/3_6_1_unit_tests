# Домашнее задание к лекции 4.«Tests»

## Решение задачи №1 

### [Задача №1 unit-tests](https://github.com/JuliiaZhuravleva/3_6_1_unit_tests)
Из курса «Python: программирование на каждый день и сверхбыстрое прототипирование» нужно написать тесты на любые 3 задания из [Лекции 4](https://github.com/netology-code/py-homeworks-basic/tree/master/4.collections).
Необходимо использовать своё решение домашнего задания.

* При написании тестов не забывайте использовать параметризацию.
  
Рекомендации по тестам.
1. Если у вас в функциях информация выводилась(print), то теперь её лучше возвращать(return) чтобы можно было протестировать.

### [Задача №2 Автотест API Яндекса](https://github.com/JuliiaZhuravleva/3_6_2_yadisk_create_folder_test)
Проверим правильность работы Яндекс.Диск REST API. Написать тесты, проверяющий создание папки на Диске.  
Используя библиотеку requests напишите unit-test на верный ответ и возможные отрицательные тесты на ответы с ошибкой

Пример положительных тестов:
* Код ответа соответствует 200.
* Результат создания папки - папка появилась в списке файлов.

### [Задача №3. Дополнительная (не обязательная)](https://github.com/JuliiaZhuravleva/3_6_3_test_yandex_auth)
Применив selenium, напишите unit-test для авторизации на Яндексе по url: https://passport.yandex.ru/auth/
