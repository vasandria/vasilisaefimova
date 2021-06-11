#= 3.8. Отфильтруйте словарь draw_dict, перебрав все его записи (entries), оставив
в нем только страны группы A. Отфильтрованный результат запишите в новый словарь draw_new. =#


draw_dict = Dict{AbstractString, AbstractString}(
            "Russia" => "A",
            "Portugal" => "B",
            "France" => "C",
            "Denmark" => "C",
            "Egypt" => "A"
)

draw_new = Dict{AbstractString, AbstractString}()

for (key, value) in draw_dict
    if value == "A"
        get!(draw_new, key, value)
    end
end

for (key, value) in draw_new
    println("$(key)")
end
