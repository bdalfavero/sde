program brown
    implicit none

    real, dimension(2) :: v, x
    real :: t, dt
    integer :: i, j, steps

    open(10, file="data.csv")

    steps = 1000
    t = 0.0
    dt = 0.01
    v = [0.1, 0.1]
    x = [0.5, 0.5]

    ! write a header to the csv file
    write (10,*)"time,vx,vy,x,y"

    do j = 1, steps
        write(10,'(*(G0.6,:,","))') t, v(1), v(2), x(1), x(2)

        ! update position and time
        x = x + dt * v
        t = t + dt

        ! reflect velocity components as needed
        do i = 1, 2
            if (x(i) >= 1.0 .or. x(i) <= 0.0) then
                v(i) = -v(i)
            end if
        end do 
    end do

end program brown