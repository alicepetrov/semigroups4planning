(define (problem DRIVE-REVERSABLE-1-4)

(:domain DRIVE)

(:objects loc-1 loc-2 loc-3 loc-4)

(:init (at loc-1) 
    (connected loc-1 loc-2) 
    (connected loc-2 loc-1) 
    (connected loc-1 loc-3) 
    (connected loc-3 loc-1) 
    (connected loc-2 loc-4) 
    (connected loc-4 loc-2) 
    (connected loc-3 loc-4)
    (connected loc-4 loc-3))

(:goal (at loc-4)))