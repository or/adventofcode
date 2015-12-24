(ns aoc.9.solution
  (:require [clojure.java.io :as io])
  (:gen-class))

(defn read-file [file]
  (with-open [rdr (io/reader file)]
    (doall (line-seq rdr))))

(def nodes (atom #{}))
(def graph (atom {}))

(defn add-node [node]
  (swap! nodes conj node))

(defn set-distance [node1 node2 distance]
  (do (swap! graph assoc [node1 node2] distance)
      (swap! graph assoc [node2 node1] distance)))

(defn parse-file [file]
  (doall
   (for [line (read-file file)
         :let [match (re-matches #"^(.+) to (.+) = (\d+)" line)
               node1 (match 1)
               node2 (match 2)
               distance (read-string (match 3))]
         :when (= (count match) 4)]
     (do
       (println node1 node2 distance)
       (add-node node1)
       (add-node node2)
       (set-distance node1 node2 distance)))))

(defn solve [func nodes-left graph current]
  (if (empty? nodes-left)
    0
    (reduce
     func
     (filter
      (comp not nil?)
      (for [node nodes-left]
        (let [leg (if (nil? current) 0 (graph [current node]))
              dist (when-not (nil? leg) (solve func (disj nodes-left node) graph node))]
          (when every? (comp not nil?) [leg dist] (+ leg dist))))))))

(defn -main [file]
  (do
    (parse-file file)
    (println @nodes)
    (println @graph)
    (println (solve min @nodes @graph nil))
    (println (solve max @nodes @graph nil))))
