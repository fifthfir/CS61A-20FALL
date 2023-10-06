(define (cddr s)
  (cdr (cdr s))
)

(define (cadr s)
  (car (cdr s))
)

(define (caddr s)
  (car (cdr (cdr s)))
)

(define (sign num)
  (cond ((> 0 num) -1) ((= 0 num) 0) (else 1))
)

(define (square x) (* x x))

(define (pow x y)
  (cond ((= 1 y) x) 
        ((even? y) (pow (square x) (/ y 2)))
        (else (* x (pow (square x) (/ (- y 1) 2))))
  )
)

