-- #-----------------------------------------------------------
-- # URL    : https://www.codewars.com/kata/5818bde9559ff58bd90004a2
-- # Notes  : tag-codewars, tag-kyu-4
-- #-----------------------------------------------------------

WITH ActorAndFilm (actor_id, actor, title) AS
  (SELECT af.actor_id,
          af.actor,
          film.title
   FROM film,

     (SELECT a.actor_id,
             CONCAT(a.first_name, ' ', a.last_name) AS actor,
             fa.film_id
      FROM film_actor fa,
           actor a
      WHERE a.actor_id = fa.actor_id ) af
   WHERE film.film_id = af.film_id ),
     ActorAndFilm2 (first_actor, second_actor, title) AS
  (SELECT a.actor AS first_actor,
          b.actor AS second_actor,
          a.title
   FROM ActorAndFilm a
   INNER JOIN ActorAndFilm b ON a.title = b.title
   WHERE a.actor != b.actor
     AND a.actor_id < b.actor_id ),
     ActorAndFilm3 (first_actor, second_actor, allJoined) AS
  (SELECT t.first_actor,
          t.second_actor,
          COUNT(t.title) AS allJoined
   FROM ActorAndFilm2 t
   GROUP BY CONCAT(t.first_actor, t.second_actor),
            first_actor,
            second_actor
   ORDER BY allJoined DESC
   LIMIT 1)
SELECT af3.first_actor,
       af3.second_actor,
       af2.title
FROM ActorAndFilm2 af2,
     ActorAndFilm3 af3
WHERE CONCAT(af2.first_actor, af2.second_actor) = CONCAT(af3.first_actor, af3.second_actor)