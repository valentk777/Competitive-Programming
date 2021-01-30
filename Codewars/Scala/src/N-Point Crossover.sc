/** -----------------------------------------------------------
 * URL    : https://www.codewars.com/kata/57339a5226196a7f90001bcf/train/scala
 * Notes  : tag-codewars
 * ----------------------------------------------------------- */

@scala.annotation.tailrec
def crossover[T](ns: List[Int], xs: List[T], ys: List[T]): (List[T], List[T]) = ns.distinct match {
  case Nil => (xs, ys)
  case n :: nss => crossover(nss, xs.take(n) ::: ys.drop(n), ys.take(n) ::: xs.drop(n))
}

crossover(Nil, List(1, 1, 1, 1, 1), List(2, 2, 2, 2, 2)) == (List(1, 1, 1, 1, 1), List(2, 2, 2, 2, 2))
crossover(List(1), List(1, 1, 1, 1, 1), List(2, 2, 2, 2, 2)) == (List(1, 2, 2, 2, 2), List(2, 1, 1, 1, 1))
crossover(List(1, 1), List(1, 1, 1, 1, 1), List(2, 2, 2, 2, 2)) == (List(1, 2, 2, 2, 2), List(2, 1, 1, 1, 1))
crossover(List(1, 3), List(1, 1, 1, 1, 1), List(2, 2, 2, 2, 2)) == (List(1, 2, 2, 1, 1), List(2, 1, 1, 2, 2))
crossover(List(1, 3, 5), List(1, 1, 1, 1, 1, 1, 1), List(2, 2, 2, 2, 2, 2, 2)) == (List(1, 2, 2, 1, 1, 2, 2), List(2, 1, 1, 2, 2, 1, 1))
crossover(List(3, 5, 1), List(1, 1, 1, 1, 1, 1, 1), List(2, 2, 2, 2, 2, 2, 2)) == (List(1, 2, 2, 1, 1, 2, 2), List(2, 1, 1, 2, 2, 1, 1))
