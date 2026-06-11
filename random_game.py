import random




print("Выберите режим(1|2|3|4):\n\n1)Классический\n2)Сложный\n3)Двойной\n4)Ознакомления\n")

mode = int(input("Выбрать:"))



if mode == 1:

 print("\n" * 100)
 print("#<Вы выбрали режим: Классический>#")


 r_classic = random.randint(0, 10)

 attempts = 3


 print("=" * 44)
 print("1) Правило:  Можно написать число от 0 до 10\n2) Правило:  Число должно быть целым!\n3) Правило: У вас всего 3 попытки")
 print("=" * 44)


 while attempts > 0:


  try:

    x = int(input("Введите свое число:"))

  except ValueError:

     print("\n" * 100)
     print("+-" * 17)
     print("!#ДОПУСТИМ ВВОД ЛИШЬ ЦЕЛЫХ ЧИСЕЛ#!")
     print("+-" * 17)

     continue


  if x < 0:

    print("\n" * 100) 
    print("*" * 25)
    print("Допустимый диапозон 0-10!")
    print("*" * 25)

    continue

  elif x > 10:

    print("\n" * 100)
    print("/" * 25)
    print("Допустимый диапозон 0-10!")
    print("/" * 25)

    continue


  if x < r_classic:

        print("\n" * 100)
        print("+" * 24)
        print("ВАШЕ ЧИСЛО МЕНЬШЕ МОЕГО!")
        print("+" * 24)
        print("#" * 28)

        attempts -= 1

        print(f"Текущее количество попыток:{attempts}")
        print("#" * 28)

  elif x > r_classic:

        print("\n" * 100)
        print("+" * 24)
        print("ВАШЕ ЧИСЛО БОЛЬШЕ МОЕГО!")
        print("+" * 24)
        print("#" * 28)

        attempts -= 1

        print(f"Текущее количество попыток:{attempts}")
        print("#" * 28)


  if attempts == 0:

        print("\n" * 50)
        print("[Вы проиграли!]")

        break

  elif x == r_classic:

        print("\n" * 50)
        print("[Вы победили!]")

        break



elif mode == 2:

 print("\n" * 100)
 print("\n#<Вы выбрали режим: Сложный>#\n")
 print("=" * 45)
 print("1) Правило:  Можно написать число от 0 до 100\n2) Правило:  Число должно быть целым!\n3) Правило:  У вас всего 7 попыток")
 print("=" * 45)


 r_hardcore = random.randint(0, 100)

 h_attempts = 7

 while h_attempts > 0:


  try:

      h_x = int(input("Введите своё число:"))

  except ValueError:

     print("\n" * 100)
     print("+-" * 17)
     print("!#ДОПУСТИМ ВВОД ЛИШЬ ЦЕЛЫХ ЧИСЕЛ#!")
     print("+-" * 17)

     continue


  if h_x < 0:

    print("\n" * 100) 
    print("*" * 25)
    print("Допустимый диапозон 0-100!")
    print("*" * 25)

    continue

  elif h_x > 100:

    print("\n" * 100)
    print("/" * 25)
    print("Допустимый диапозон 0-100!")
    print("/" * 25)

    continue


  if h_x < r_hardcore:

        print("\n" * 100)
        print("+" * 24)
        print("ВАШЕ ЧИСЛО МЕНЬШЕ МОЕГО!")
        print("+" * 24)
        print("#" * 28)

        h_attempts -= 1

        print(f"Текущее количество попыток:{h_attempts}")
        print("#" * 28)

  elif h_x > r_hardcore:

        print("\n" * 100)
        print("+" * 24)
        print("ВАШЕ ЧИСЛО БОЛЬШЕ МОЕГО!")
        print("+" * 24)
        print("#" * 28)

        h_attempts -= 1

        print(f"Текущее количество попыток:{h_attempts}")
        print("#" * 28)


  if h_attempts == 0:

      print("\n" * 50)
      print("[Вы проиграли!]")

      break

  elif h_x == r_hardcore:

      print("\n" * 50)
      print("[Вы победили!]")

      break
 


elif mode == 3:


      print("\n" * 100)
      print("\n#<Вы выбрали режим: Двойной игры!>#\n")
      print("=" * 45)
      print("1) Правило:  Можно написать число от 0 до 20\n2) Правило:  Число должно быть целым!\n3) Правило: У каждого по 5 попыток")
      print("=" * 45)


      d_attempts1 = 5

      d_attempts2 = 5

      d_attempts = d_attempts1 + d_attempts2


      d_random = random.randint(0, 20)


      name_1 = str(input("[1]Игрок - ваше имя:"))

      name_2 = str(input("[2]Игрок - ваше имя:"))


      while d_attempts > 0:


              try:

               d_x1 = int(input(f"\n[{name_1}]Введите своё число:"))


               if d_x1 < d_random:

                   print("\n" * 5)
                   
                   d_attempts1 -= 1
                   
                   print(f"[{name_1}]Tекущее количество попыток:{d_attempts1}")


               elif d_x1 > d_random:  

                   print("\n" * 5)

                   d_attempts1 -= 1
                   
                   print(f"[{name_1}]Tекущее количество попыток:{d_attempts1}")


               if d_x1 < 0:

                print("\n" * 5) 
                print("*" * 24)
                print("Допустимый диапозон 0-20!")
                print("*" * 24)

                continue

               elif d_x1 > 20:

                print("\n" * 5) 
                print("*" * 24)
                print("Допустимый диапозон 0-20!")
                print("*" * 24)

                continue


               d_x2 = int(input(f"\n[{name_2}]Введите своё число:"))


               if d_x2 < d_random:

                   print("\n" * 5)

                   d_attempts2 -= 1
                   
                   print(f"[{name_2}]Текущее количество попыток:{d_attempts2}")

               elif d_x2 > d_random:

                   print("\n" * 5)

                   d_attempts2 -= 1
                   
                   print(f"[{name_2}]Tекущее количество попыток:{d_attempts2}")

               if d_x2 < 0:

                print("\n" * 5) 
                print("*" * 24)
                print("Допустимый диапозон 0-20!")
                print("*" * 24)

                continue

               elif d_x2 > 20:

                print("\n" * 5) 
                print("*" * 24)
                print("Допустимый диапозон 0-20!")
                print("*" * 24)

                continue


              except ValueError:

               print("\n" * 100)
               print("+-" * 17)
               print("!#ДОПУСТИМ ВВОД ЛИШЬ ЦЕЛЫХ ЧИСЕЛ#!")
               print("+-" * 17)

               continue 
                   

              if d_attempts == 0:

                  print("\nИГРА ОКОНЧЕНА: (НИКТО НЕ ВЫИГРАЛ)")

                  break

              elif d_x1 == d_random:

                  print(f"ПОБЕДИЛ:[{name_1}]")

                  break

              elif d_x1 == d_random:
            
                  print(f"ПОБЕДИЛ:[{name_1}]")

                  break




elif mode == 4:

 print("\n" * 100)
 print("#" * 100)
 print("\n1) Режим классический - это режим игры где из 10 чисел вам даётся всего 3 шанса на угад угадать!\n\n", "#" * 95) 
 print("\n2) Режим Сложный - это режим игры где у вас 100 чисел и всего дано 7 шансов на ошибку\n\n", "#" * 95)
 print("\n3) Режим двойной - это режим игры в котором можно играть в двоём, отличие от классического:\n\n - Всего 20 чисел\n - Каждому игроку даётся 5 шансов вместо 3\n")
 print("#" * 100)
