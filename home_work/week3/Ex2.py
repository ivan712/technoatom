class ICache:
    def __init__(self, capacity: int=10) -> None:
        self.size = capacity #размер словаря
        self.d = {} 
        self.n = 0 #количество элементов в словаре

        
    def get(self, key: str) -> str:
        if key in self.d:
            return self.d[key]
        else:
            return f'have not element with key {key}'

        
    def set(self, key: str, value: str) -> None:
        if key in self.d:
            self.d[key] = value
        else:
            if self.n + 1<= self.size:
                self.n += 1
                self.d[key] = value
            else:
                print('Size exceeded')

                
    def dell(self, key: str) -> None: #метод был переименован, так как при использовании del выдается ошибка
        if key in self.d:
            self.n -= 1
            del self.d[key]
        else:
            print('have not element with key ',key)
