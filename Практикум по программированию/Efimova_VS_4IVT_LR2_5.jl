#= 3.5. Вычислить скорость электрона, вырванного из данного материала при
фотоэффекте под воздействием излучения частоты ν (греческая буква «ню»). =#

using PhysicalConstants
using Unitful

h = PhysicalConstants.CODATA2018.h
mₑ = PhysicalConstants.CODATA2018.m_e
c = PhysicalConstants.CODATA2018.SpeedOfLightInVacuum

function user_V(A, ν)
    h = PhysicalConstants.CODATA2018.h
    mₑ = PhysicalConstants.CODATA2018.m_e

    return √((2 / mₑ) * (h*ν - uconvert(u"J", A)))
end

λ = 2.5e-7u"m"
ν = c / λ

A = [4.3u"eV" 2.9u"eV"; "Ag" "Li"]

for i in eachcol(A)
  println("$(i[2]): ", uconvert(u"m*s^-1", user_V(i[1], ν)))
end
