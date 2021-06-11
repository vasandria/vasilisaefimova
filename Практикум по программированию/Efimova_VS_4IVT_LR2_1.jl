#=
3.1. Даны три одномерных массива вещественных чисел A[1 . . . 6], B[1 . . . 8] и C[1 . . . 7].
Найти общую сумму положительных элементов в массивах. Нахождение суммы элементов в массиве оформить функцией.
=#

function users_sum(mas)
  sum = 0
  for i in mas
    if i > 0
      sum += i
    end
  end
  return sum
end

A = [1:6;]
B = [1:8;]
C = [1:7;]

for i in [A, B, C]
  println("sum of $i: ", users_sum(i))
end
