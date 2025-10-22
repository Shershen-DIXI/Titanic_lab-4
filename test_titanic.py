import pandas as pd
import pytest

def filter_titanic_data(df, pclass_filter=None, fare_range=None, sex='female', survived=1):
    """
    Основная функция фильтрации данных Титаника
    """
    # Применяем базовые фильтры
    filtered_df = df[df['Sex'] == sex]
    filtered_df = filtered_df[filtered_df['Survived'] == survived]
    
    # Применяем фильтр по классу
    if pclass_filter:
        filtered_df = filtered_df[filtered_df['Pclass'].isin(pclass_filter)]
    
    # Применяем фильтр по цене билета
    if fare_range:
        min_fare, max_fare = fare_range
        filtered_df = filtered_df[
            (filtered_df['Fare'] >= min_fare) & 
            (filtered_df['Fare'] <= max_fare)
        ]
    
    return filtered_df

# Тестовые данные
def create_test_data():
    """Создание тестового набора данных"""
    data = {
        'PassengerId': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        'Survived': [1, 0, 1, 1, 0, 1, 1, 0, 1, 0],
        'Pclass': [1, 3, 1, 2, 3, 1, 2, 3, 1, 2],
        'Sex': ['female', 'male', 'female', 'female', 'male', 'female', 'female', 'male', 'female', 'male'],
        'Fare': [50.0, 10.0, 100.0, 30.0, 15.0, 80.0, 25.0, 20.0, 90.0, 35.0]
    }
    return pd.DataFrame(data)

# Тест 1: Базовый фильтр (только выжившие женщины)
def test_basic_filter():
    """Тестирование базового фильтра - только выжившие женщины"""
    df = create_test_data()
    result = filter_titanic_data(df)
    
    # Проверяем, что все записи - выжившие женщины
    assert len(result) == 6
    assert all(result['Sex'] == 'female')
    assert all(result['Survived'] == 1)

# Тест 2: Фильтр по классу
def test_class_filter():
    """Тестирование фильтрации по классу пассажира"""
    df = create_test_data()
    
    # Фильтруем только 1 класс
    result = filter_titanic_data(df, pclass_filter=[1])
    assert len(result) == 4
    assert all(result['Pclass'] == 1)
    
    # Фильтруем 1 и 2 класс
    result = filter_titanic_data(df, pclass_filter=[1, 2])
    assert len(result) == 5
    assert all(result['Pclass'].isin([1, 2]))

# Тест 3: Фильтр по цене билета
def test_fare_filter():
    """Тестирование фильтрации по цене билета"""
    df = create_test_data()
    
    # Фильтруем по диапазону цен
    result = filter_titanic_data(df, fare_range=(40.0, 90.0))
    assert len(result) == 3
    assert all(result['Fare'] >= 40.0)
    assert all(result['Fare'] <= 90.0)
