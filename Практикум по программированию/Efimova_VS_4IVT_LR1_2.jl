using DataFrames, Query
import CSV

csv_file = CSV.File("/Users/vasan/OneDrive/Рабочий стол/sharaga/Практикум по программированию/Efimova_VS_4IVT_LR1/altadatacovid_19.csv")
covid_data = DataFrame(csv_file)

data_portugal = @from entry in covid_data begin
                @where entry.country_region == "Portugal"
                @select {entry.reported_date,
                         entry.confirmed,
                         entry.active,
                         entry.deaths,
                         entry.recovered,
                         entry.mortality_rate,
                         entry.incident_rate}
                @collect DataFrame
              end

data_portugal = sort!(data_portugal)
data_portugal_tail = tail(data_portugal, 10)
println("Latest statistics in portugal:\n$data_portugal_tail")

println("Some statistical data description in portugal:")
describe(data_portugal, :min, :max, :mean, :std, :median)

plot(data_portugal.reported_date,
     [data_portugal.active,
    data_portugal.deaths],
    title = "Portugal - COVID-19",
    label = ["active" "deaths"])
