from entity.shop import Shop
from entity.store import Store
from entity.request import Request
from exceptions import RequestError, InvalidRequest, InvalidStorage, CourierError

store = Store(
    items={
        "печенька": 25,
        "собака": 23,
        "елка": 12,
        "пончик": 5,
        "зонт": 7,
        "ноутбук": 2,
    }
)

shop = Shop(
    items={
        "печенька": 2,
        "собака": 1,
        "елка": 2,
        "пончик": 3,
        "зонт": 2,
    }
)
storages = {
    "магазин": shop,
    "склад": store,
}


def main():
    print('\nДобрый день\n')

    while True:
        for storage_name in storages:
            print(f'Сейчас в {storage_name}:\n{storages[storage_name].get_items()}')

        user_input = input(
            'Введите запрос в формате "Доставить 3 печеньки из склад в магазин"\n'
            'Введите "стоп" или "stop" если хотите закончить:\n'
        )
        if user_input in ('стоп','stop'):
            break
        try:
            request = Request(request=user_input, storages=storages)
        except RequestError as error:
            print(error.message)
            continue
        try:
            storages[request.departure].remove(request.product, request.amount)
            print(f"Курьер забрал {request.amount} {request.product} из {request.departure}")
        except CourierError as error:
            print(error.message)
            continue
        try:
            print(f"Курьер доставил {request.amount} {request.product} в {request.destination}")
            storages[request.destination].add(request.product, request.amount)
        except CourierError as error:
            print(error.message)
            storages[request.departure].add(request.product, request.amount)
            print(f"Курьер вернул {request.amount} {request.product} в {request.departure}")
            continue


if __name__ == '__main__':
    main()