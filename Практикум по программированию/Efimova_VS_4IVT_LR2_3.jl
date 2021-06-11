#= 3.3. Дана матрица целых чисел D[1 . . . 6, 1 . . . 5]. Найти наименьшую из сумм неотрицательных
элементов строк матрицы. Для вычисления суммы использовать подпрограмму (функцию). =#

function users_sum(mas)
  sum = 0
  for i in mas
    if i > 0
      sum += i
    end
  end
  return sum
end

D = [1 2 3 4 5 6; 2 3 4 5 6 7]

min_in_mas = []

for i in eachrow(D)
  push!(min_in_mas, users_sum(i))
end

print("Наименьшая сумма в массиве равна ", min(min_in_mas...))
