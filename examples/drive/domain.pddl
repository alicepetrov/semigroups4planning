;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;;      4 State Drive Example       ;;;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

(define (domain DRIVE)
  (:requirements :strips)
  (:predicates (at ?x)(connected ?x ?y))

  (:action drive-x-y
	     :parameters (?x ?y)
	     :precondition (and (at ?x) (connected ?x ?y))
	     :effect
	     (and (not (at ?x)) (at ?y))))