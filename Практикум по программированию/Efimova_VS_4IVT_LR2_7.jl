#= 3.7. Потренируйтесь с массивами массивов («списками» «списков»). Отфильтруйте массив
товарных позиций file_data, оставив только те позиции, у которых количество штук на складе
больше 10. Результат запишите в переменную file_data_filtered. =#


file_data = [
    ["100412", "Alpine ski boots ATOMIC Hawx Prime 100", 9],
    ["100728", "Skateboard Jdbug RT03", 32],
    ["100732", "Rollersurf Razor RipStik Bright", 11],
    ["100803", "Snowboard Boots DC Tucknee", 20],
    ["100898", "Pedometer Omron HJA-306", 2],
    ["100934", "Heart rate monitor Beurer PM62", 17],
]

file_data_filtered = []

for i in file_data
    if i[3] > 10
        push!(file_data_filtered, i)
    end
end

for (index, name, number) in file_data_filtered
    println("$(index) - $(name) - $(number)")
end
