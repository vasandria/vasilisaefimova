# 4th Order Runge-Kutta
using Plots

function f1(t::Float64,x::Array{Float64,1})
    return x[1]
end

f=Function[]
push!(f,f1)

function RK4(f::Array{Function,1},t0::Float64,x::Array{Float64,1},h::Float64)
    d=length(f)

    hk1=zero(x)
    hk2=zero(x)
    hk3=zero(x)
    hk4=zero(x)

    for ii in 1:d
        hk1[ii]=h*f[ii](t0,x)
    end
    for ii in 1:d
        hk2[ii]=h*f[ii](t0+h/2,x+hk1/2)
    end
    for ii in 1:d
        hk3[ii]=h*f[ii](t0+h/2,x+hk2/2)
    end
    for ii in 1:d
        hk4[ii]=h*f[ii](t0+h,x+hk3)
    end

    return t0+h,x+(hk1+2*hk2+2*hk3+hk4)/6
end

function Solver(f::Array{Function,1},Method::Function,t0::Float64, x0::Array{Float64,1},h::Float64,N::Int64)
    d=length(f)
    ts=zeros(Float64,N+1)
    xs=zeros(Float64,d,N+1)

    ts[1]=t0
    xs[:,1]=x0

    for i in 2:(N+1)
        ts[i],xs[:,i]=Method(f,ts[i-1],xs[:,i-1],h)
    end

    return ts,xs
end

N=1000
xf=10
t0=0.
x0=[1.]
dt=(xf-t0)/N

tRK4,xRK4=Solver(f,RK4,t0,x0,dt,N)

xi = tRK4
yi = []

for i in xi
    push!(yi, exp(i))
end

plot(tRK4, [yi, transpose(xRK4)],
     title = "Runge-Kutta (4th Order)",
     label = ["e" "rk4"], lw = [10 4])
