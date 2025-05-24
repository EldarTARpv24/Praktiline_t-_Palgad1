import PalgadModule

p = [1200, 2500, 750, 395, 1200]
i = ["Andrei", "´Pavel", "Sergei", "Daniel", "Eva"]

while True:
            print("Tere, sekretär!")
            print("\n")
            print("Palun valige: ")
            print("\n")
            print("1 - Добавить еще несколько человек и зарплат: ") 
            print("2 - Удалить человека и его зарплату: ") 
            print("3 - Посмотреть самую большую зарплату и кто ее получает: ") 
            print("4 - Кто получает самую маленькую зарплату и какую именно: ") 
            print("5 -  Упорядочить зарплаты в порядке возрастания и убывания вместе с именами: ") 
            print("6 - Узнать, кто получает одинаковую зарплату, найти сколько таких людей вывести их данные на экран: ") 
            print("7 - Сделать поиск зарплаты по имени человека: ") 
            print("8 - Вывести список людей(с зарплатами), кто получает больше/меньше чем указанная сумма: ")
            print("9 -  Тop самых бедных и самых богатых человека: ") 
            print("10 - Посмтореть среднюю зарплату и имя человека ее получающего:  ")
            print("11 - Вычислить зарплату, которую человек получит на руки после вычисления подоходного налога: ")
            print("\n")
            try:
                choice = int(input("Mida te tahate tegeleda?: "))
            except ValueError:
                print("\n")
                print("Введите только значения предложенные выше!")
                continue  

            
            if choice == 1:
                PalgadModule.Lisa(p, i)
            elif choice == 2:
                PalgadModule.kustumine(p, i)
            elif choice == 3:
                PalgadModule.Suurim(p, i)
            elif choice == 4:
                PalgadModule.väiksem(p, i)
            elif choice == 6:
                PalgadModule.Võrsed_palgad(p, i)
            elif choice == 7:
                PalgadModule.otsi(p, i)
            elif choice == 9:
                PalgadModule.Top(p, i)