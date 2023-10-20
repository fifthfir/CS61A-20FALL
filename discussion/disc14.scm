(define (deep-map fn lst)
  (if (null? lst) lst
      (cons (fn (car lst)) (deep-map fn (cdr lst)))
  )
)
