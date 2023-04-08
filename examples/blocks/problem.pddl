(define (problem BLOCKS-4-0)

(:domain BLOCKS)

(:objects B A - block 
          L - light)

(:init 
    (CLEAR A) 
    (CLEAR B)  
    (ONTABLE A) 
    (ONTABLE B) 
    (HANDEMPTY))

(:goal (AND  
    (ON B A)
    (not (light-on L))))
)