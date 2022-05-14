program brown
    implicit none

    real, dimension(2) :: v, x
    real :: t, dt
    integer :: i, j, steps

    open(10, file="data.txt")

    steps = 100
    t = 0.0
    dt = 0.01
    v = [0.1, 0.1]
    x = [0.5, 0.5]

    do j = 1, steps
        write(10,*) t, v(1), v(2), x(1), x(2)

        ! update position and time
        x = x + dt * v
        t = t + dt

        ! reflect velocity components as needed
        do i = 1, 2
            if (v(i) >= 1.0 .or. v(i) <= 0.0) then
                v(i) = -v(i)
            end if
        end do 
    end do

end program brown