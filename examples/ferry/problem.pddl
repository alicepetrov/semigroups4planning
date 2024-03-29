(define (problem ferry-l3-c2)
(:domain ferry)
(:objects l0 l1 l2
          c0
)
(:init
	(location l0)
	(location l1)
	(location l2)
	(sight l2)
	(car c0)
	(not-eq l0 l1)
	(not-eq l1 l0)

	(not-eq l2 l1)
	(not-eq l1 l2)
	
	(empty-ferry)
	(at c0 l1)
	(at-ferry l0)
)
(:goal
(and 
	(at c0 l0)
	(at-ferry l2)
	)
))