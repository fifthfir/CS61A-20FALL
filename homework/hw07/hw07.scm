;;; Q1
(define (filter-lst fn lst)
    (if (null? lst)
        lst
        (if (fn (car lst))
            (cons (car lst)  (filter-lst fn (cdr lst)))
            (filter-lst fn (cdr lst))
        )
    )
)

;;; Tests
(define (even? x)
  (= (modulo x 2) 0))
(filter-lst even? '(0 1 1 2 3 5 8))
; expect (0 2 8)

;;; Q2
(define (interleave first second)
    (if (or (null? second) (null? first))
        (append first second)
        (cons (car first) (cons (car second) (interleave (cdr first) (cdr second))))
        
    )
)

(interleave (list 1 3 5) (list 2 4 6))
; expect (1 2 3 4 5 6)

(interleave (list 1 3 5) nil)
; expect (1 3 5)

(interleave (list 1 3 5) (list 2 4))
; expect (1 2 3 4 5)

;;; Q3
(define (accumulate combiner start n term)
    (if (= 0 n)
        start
        (accumulate combiner (combiner start (term n)) (- n 1) term)
    )
)

;;; Q4
(define (member item items)
    (cond
        ((null? items) #f)
        ((equal? item (car items)) #t)
        (else (member item (cdr items)))
    )
)

(define (no-repeats lst)
    (if (null? lst)
        lst
        (if (member (car lst) (cdr lst))
            (cons (car lst) (no-repeats (filter-lst (lambda (x) (not (= x (car lst)))) (cdr lst))))
            ;;;(no-repeats (cdr lst))
            (cons (car lst) (no-repeats (cdr lst)))
        )
    )
)
