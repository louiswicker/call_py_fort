program example
use callpy_mod
implicit none

real(8) :: a(4,4)
real(8) :: b(4,4)

a(:,1) = 1.0
a(:,2) = 2.0
a(:,3) = 3.0
a(:,4) = 4.0

call set_state("a", a)

call call_function("my_functions", "run_function")

call get_state("a", b)

print *, b(:,1)
end program example
