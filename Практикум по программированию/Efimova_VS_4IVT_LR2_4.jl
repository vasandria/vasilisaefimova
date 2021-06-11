#= 3.4. Дана матрица целых чисел D[1 . . . 3, 1 . . . 5]. Используя функцию, найти
среднее геометрическое значение для каждого столбца матрицы. =#

function mean_geometric(mas)
  multiply = 1
  n = 0
  for i in mas
    if i > 0
      multiply *= i
      n += 1
    end
  end
  return multiply ^ (1/n)
end

D = [1 2 3 4 5 6; 2 3 4 5 6 7]

for i in eachcol(D)
  println("Для $(i) среднее геометрическое равно $(mean_geometric(i))")
end
