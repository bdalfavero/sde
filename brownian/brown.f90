program brown
    implicit none

    real, dimension(2) :: v, x
    real :: t, dt 
    real :: lambda, eta
    real :: wx, wy, r1, r2, mag
    integer :: i, j, steps

    open(10, file="data.csv")
    open(11, file="input.dat")

    read(11,*) steps
    read(11,*) lambda
    read(11,*) eta
    read(11,*) dt
    read(11,*) v(1), v(2)
    read(11,*) x(1), x(2)

    t = 0.0

    ! write a header to the csv file
    write(10,'(a)') "t,vx,vy,x,y"

    do j = 1, steps
        write(10,'(*(G0.6,:,","))') t, v(1), v(2), x(1), x(2)

        ! draw the random variables
        ! use the box-muller transform
        ! nb we must subtract one from the uniform
        ! numbers, because they do not go up to one.
        call random_number(r1)
        call random_number(r2)
        r1 = 1.0 - r1 
        r2 = 1.0 - r2
        mag = dt * sqrt(-2.0 * log(r1))
        wx = mag * cos(2 * 3.14 * r2)
        wy = mag * sin(2 * 3.14 * r2)

        ! update position and time
        x = x + dt * v
        v = v - dt * lambda * v
        v(1) = v(1) + eta * wx
        v(2) = v(2) + eta * wy
        t = t + dt

        ! reflect velocity components as needed
        do i = 1, 2
            if (x(i) >= 1.0 .or. x(i) <= 0.0) then
                v(i) = -v(i)
            end if
        end do 
    end do

    close(10)

end program brown